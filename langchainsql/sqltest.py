import sqlite3

# Update this with the path to your downloaded Chinook SQLite database file
database_path = r'/Users/abhishekshah/Desktop/sqlllm/Chinook_Sqlite.sqlite'

# Connect to the Chinook SQLite database file
conn = sqlite3.connect(database_path)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# # Define a query (example: selecting all records from the Album table)
query = "SELECT * FROM Album;"

# # Execute the query
cursor.execute(query)

# # Fetch and print the results
results = cursor.fetchall()
for row in results:
    print(row)

# # Close the cursor and connection
cursor.close()
conn.close()