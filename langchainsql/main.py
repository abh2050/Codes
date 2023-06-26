import streamlit as st
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
import os
from constant import openai_key

# Set up your API key
os.environ["OPENAI_API_KEY"] = openai_key

# Connect to the Chinook database
db_path = r'/Users/abhishekshah/Desktop/sqlllm/Chinook_Sqlite.sqlite'  # Change this to the path to your Chinook SQLite database file
db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))
agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

# Streamlit app code
def main():
    st.title("SQL Query Application")

    # Input query from the user
    query = st.text_input("Enter your SQL query:")

    if st.button("Run Query"):
        # Execute the query using the SQL agent
        response = agent_executor.run(query)

        # Display the response
        st.write("Response:")
        st.code(response)

if __name__ == "__main__":
    main()
