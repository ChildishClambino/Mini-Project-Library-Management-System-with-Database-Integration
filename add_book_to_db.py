from connection_to_db import connect_database

# Function adds books to SQL database
def add_book_to_db(title, author_id, genre_id, isbn, publication_date, availability):  # Parameters for adding book to the database  
    conn = connect_database()
    
    if conn is not None:
        
        try:
            cursor = conn.cursor()
            query = "INSERT INTO books (title, author_id, genre_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s, %s)"   # query that adds to the "books" table in the databse
            cursor.execute(query, (title, author_id, genre_id, isbn, publication_date, availability))
            conn.commit()
            print("New book added successfully! ")
        
        finally:
            cursor.close()
            conn.close()

