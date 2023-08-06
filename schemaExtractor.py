import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('.\scriptures-generator\lds-scriptures-sqlite3.db')

# Get a cursor object to execute SQL queries
cursor = conn.cursor()

# Retrieve the schema for each table
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
table_names = cursor.fetchall()

for table_name in table_names:
    cursor.execute(f"SELECT sql FROM sqlite_master WHERE name='{table_name[0]}'")
    create_statement = cursor.fetchone()[0]
    print(f"Table: {table_name[0]}")
    print(f"Schema: {create_statement}\n")

# Close the database connection
conn.close()

