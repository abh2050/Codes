# README

## SQL Query Application with OpenAI

This project is a SQL Query Application that uses OpenAI to execute SQL queries. The interface is built with Streamlit, which makes it user-friendly and easy to use.

### Dependencies

This project uses the following dependencies:

- Streamlit
- Langchain
- OpenAI
- SQLite database

You can install these dependencies with pip:


Ensure you have SQLite installed on your system as well.

### Setup

Before running the application, make sure you have an OpenAI API key. You can get this key from the OpenAI website after registration. Add the OpenAI API key to the `constants.py` file as follows:

openai_key = "your-openai-key"

The SQLite database file should be placed in a local directory. Update the `db_path` variable in the main code with the location of your SQLite database file:

db_path = r'/path_to_your_database/your_database_file.sqlite'


### Running the Application

To run the application, use the following command in your terminal:

streamlit run app.py


Once the app is running, navigate to the localhost URL provided in your terminal (typically `http://localhost:8501/`) in your web browser.

Enter your SQL query in the input field and press the "Run Query" button. The response from the execution of the SQL query will be displayed on the same page.

Please note that this project is an illustrative example of using OpenAI to execute SQL queries, so use this in production environments with caution.

### Contribution

Feel free to fork this project, open a pull request or report any issues you find. Your contribution is always welcome!

## License

This project is open source and available under the MIT License.

