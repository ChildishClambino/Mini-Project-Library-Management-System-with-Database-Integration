from connection_to_db import connect_database     

# Function that adds the authors to SQL database

def add_authors_to_db(name, biography):   # Parameters for adding authors
    conn = connect_database()

    if conn is not None:
    
        try:
            cursor = conn.cursor()
            query = "INSERT INTO authors (name, biography) VALUES(%s,%s)"
            cursor.execute(query, (name, biography))
            conn.commit()
            print("Author uploaded to database successfully! ")

        finally:
            cursor.close()
            conn.close()
