import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("example.db")
cursor = connection.cursor()

# Create a sample users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")
connection.commit()

# Sample function to authenticate users
def authenticate_user(username, password):
    # Vulnerable SQL query (using string formatting directly)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing query: {query}")  # Debug output to show the executed query

    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        print("Authentication successful!")
    else:
        print("Authentication failed!")

# Simulating user input
user_input_username = input("Enter username: ")
user_input_password = input("Enter password: ")

# Call the vulnerable function
authenticate_user(user_input_username, user_input_password)

# Close the connection
connection.close()
