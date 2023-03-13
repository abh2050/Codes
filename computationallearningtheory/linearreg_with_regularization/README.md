### Regression using Regularization 

This code uses scikit-learn's pipeline, StandardScaler, PolynomialFeatures, Ridge, KFold, GridSearchCV, mean_squared_error, and matplotlib.pyplot libraries to perform a Ridge regression on a dataset.

## Usage

The dataset has two columns, yr and pop, and is split into train and test sets using iloc. A range of kF values is defined and the program then loops over these values to perform k-fold cross-validation. The program creates a pipeline that combines StandardScaler, PolynomialFeatures, and Ridge classes, uses GridSearchCV to perform hyperparameter tuning, and then fits the data using the optimal hyperparameters.

The program then computes the root mean squared error (RMSE) for each fold of each kF value and outputs a DataFrame with the RMSE for each fold. It also outputs a plot of RMSE vs kF, and a list of the optimal degree and regularization parameter for each fold. Finally, the program outputs the optimal degree and regularization parameter for the entire dataset.

To run the program, ensure that the train.dat and test.dat files are in the same directory as the code. The program is written in Python 3 and requires the numpy, pandas, scikit-learn, and matplotlib libraries to be installed.

## Files
regression_with_regularization.py
regression_without_regularization.py
README.txt

## Dependencies
This program requires Python 3 and requirement.txt

## License
This program is licensed under the MIT License.

## Credits
This program was created by Abhishek Shah for Computational Theory, University Of Michigan, 2023.

## Contact
If you have any questions or comments about this program, please contact abhishah@umich.edu

## instructions to open the file from command line
To open the tar file or zip file created using the code above, follow the instructions below:

Open the command line on your computer.

On Windows, you can open the Command Prompt or PowerShell by typing "cmd" or "powershell" in the search bar and pressing Enter.
On Mac or Linux, you can open the Terminal application.
Navigate to the directory where the compressed file is located.

Use the "cd" command followed by the path to the directory to move to the desired location.
To open the tar file, type the following command in the command line:

Copy code
`tar -xvzf regression.tar.gz`
This will extract the contents of the tar file to the current directory.

To open the zip file, type the following command in the command line:


Copy code
`unzip regression.zip`
This will extract the contents of the zip file to the current directory.

Once the extraction is complete, you should see the individual files listed in the directory.