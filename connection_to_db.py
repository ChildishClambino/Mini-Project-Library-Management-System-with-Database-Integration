import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name = "library_management_system"
    user= "root"
    password= "Like214!"
    host = "localhost"

    try:
        conn=mysql.connector.connect(
            database = db_name,
            user= user,
            password= password,
            host= host
        )

        print("Connected to MySql database successfully! ")
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None