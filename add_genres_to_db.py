from connection_to_db import connect_database    #fully functional and integrated

# Function that adds genres to the SQL database

def add_genres_to_db(name, description):     # Parameters for adding genres to the database
    conn = connect_database()
    
    if conn is not None:
    
        try:
            cursor = conn.cursor()
            query = "INSERT INTO genres (name, description) VALUES(%s,%s)"     # Query adds genres into the "genres" table in the database
            cursor.execute(query, (name, description))
            conn.commit()
            print("Successfully added a new genre! ")
    
        finally:
            cursor.close()
            conn.close()
          
