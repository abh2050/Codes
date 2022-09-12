import tez
import pandas as pd
from sklearn import model_selection, metrics,preprocessing
import torch
import torch.nn as nn
import numpy as np
device = torch.device("cuda")

class MovieDataset:
    def __init__(self,users,movies,ratings):
        self.users=users
        self.movies=movies
        self.ratings=ratings
    
    def __len__(self):
        return len(self.users)
    
    def __getitem__(self,item):
        user = self.users[item]
        movie = self.movies[item]
        rating = self.ratings[item]
        
        return{'user':torch.tensor(user, dtype=torch.long),
                'movie':torch.tensor(movie, dtype=torch.long),
                'rating':torch.tensor(rating, dtype=torch.float)
                }
    
class RecSysModel(tez.Model):
    def __init__(self, num_users, num_movies):
        super().__init__()
        self.user_embed =nn.Embedding(num_users,32)
        self.movie_embed =nn.Embedding(num_movies,32)
        self.out =nn.Linear(64,1)
        self.step_scheduler_after = 'epoch'
    
    def fetch_optimizer(self):
        opt=torch.optim.Adam(self.parameters(),lr=1e-3)
        return opt

    def fetch_scheduler(self):
        sch =torch.optim.lr_scheduler.StepLR(self.optimizer,step_size=3,gamma=0.7)
        return sch
    
    def monitor_metrics(self,output,rating):
        output = output.detach().cpu().numpy()
        rating = rating.detach().cpu().numpy()
        return {
            'rmse': np.sqrt(metrics.mean_squared_error(rating,output))
        }

    def forward(self,users,movies,ratings):
        user_embeds=self.user_embed(users)
        movie_embeds=self.movie_embed(movies)
        output =torch.cat([user_embeds,movie_embeds],dim=1)
        output =self.out(output)
        
        loss = nn.MSELoss()(output,ratings.view(-1,1))
        metrics = self.monitor_metrics(output, ratings.view(-1,1))
        return output,loss,metrics



def train():
    df=pd.read_csv('train.csv')
    #ID ,user,movie,rating,timestamp
    lbl_user = preprocessing.LabelEncoder()
    lbl_movie = preprocessing.LabelEncoder()

    df.user =lbl_user.fit_transform(df.user.values)
    df.movie = lbl_movie.fit_transform(df.movie.values)

    df_train,df_valid=model_selection.train_test_split(df,test_size=0.1,random_state=42,stratify=df.rating.values)

    train_dataset=MovieDataset(users=df_train.user.values,movies=df_train.movie.values,ratings=df_train.rating.values)
    valid_dataset=MovieDataset(users=df_valid.user.values,movies=df_valid.movie.values,ratings=df_valid.rating.values)

    model =RecSysModel(num_users=len(lbl_user.classes_),num_movies=len(lbl_movie.classes_))
    model.fit(train_dataset,valid_dataset,train_bs=1024,valid_bs=1024,fp16=True)

if __name__ == '__main__':
    train()