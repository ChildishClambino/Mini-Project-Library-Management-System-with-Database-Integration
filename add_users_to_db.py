from connection_to_db import connect_database   # funtional and integrated

# Function adds users to the SQL database

def add_users_to_db(name, library_id):
    conn = connect_database()
    
    if conn is not None:
        
        try:
            cursor= conn.cursor()
            query = "INSERT INTO users (name, library_id) VALUES(%s, %s)"  # Query adds users into the "users" table in the database
            cursor.execute(query, (name, library_id))
            conn.commit()
            print("Succesfully added a new user! ")

        finally:
            cursor.close()
            conn.close()

