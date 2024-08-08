import os
import pypyodbc

file_path = os.path.join(os.path.dirname(__file__), "db_secret.txt")

def db_configuration():
    if not os.path.exists(file_path):
        open(file_path, "w")

        username_input = input("DB username:")
        password_input = input("DB password: ")
        server_input = input("Server address: ")
        database_input = input("Database name: ")

        with open("db_secret.txt", "w") as file:
            file.write(username_input)
            file.write("\n")
            file.write(password_input)
            file.write("\n")
            file.write(server_input)
            file.write("\n")
            file.write(database_input)
        print("Configuration file created")
    else:
        with open(file_path, "r") as file:
            lines = file.readlines()
            username = lines[0].strip()
            password = lines[1].strip()
            server = lines[2].strip()
            database = lines[3].strip()
        return username, password, server, database
    
def db_connection():
    username, password, server, database = db_configuration()
    conn = pypyodbc.connect(
    'Driver={ODBC Driver 18 for SQL Server};'
    f'Server={server};'
    f'Database={database};'
    f'UID={username};'
    f'PWD={password};'
    'Encrypt=no;'
    'TrustServerCertificate=yes;'
    )   
    return conn

    
