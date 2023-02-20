from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    certification_required = db.Column(db.String(50), nullable=False)
    education_required = db.Column(db.String(50), nullable=False)
    skill_level_required = db.Column(db.String(50), nullable=False)
    experience_required = db.Column(db.Integer, nullable=False)
    work_preference = db.Column(db.String(50), nullable=False)

@app.route('/jobs', methods=['POST'])
def create_job():
    data = request.form
    new_job = Job(skill=data['skill'], location=data['location'], certification_required=data['certification_required'], 
                  education_required=data['education_required'], skill_level_required=data['skill_level_required'], 
                  experience_required=data['experience_required'], work_preference=data['work_preference'])
    db.session.add(new_job)
    db.session.commit()
    return 'Job created successfully'

if __name__ == '__main__':
    app.run(debug=True)
