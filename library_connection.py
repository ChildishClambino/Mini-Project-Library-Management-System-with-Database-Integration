import mysql.connector

def connect_database():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Like214!',
        database='library_system'
    )
    return connection