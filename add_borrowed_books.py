from connection_to_db import connect_database    # functional and integrated

# Function that adds borrowed books to the database as such

def add_borrowed_books(user_id, book_id, borrow_date, return_date):   # Parameters for adding any books to the database
    conn = connect_database()
    
    if conn is not None:
        
        try:
            cursor = conn.cursor()
            query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date, return_date) VALUES(%s,%s,%s,%s)"   # Query allows for books to be added to the "borrowed_books" table in the databse
            cursor.execute(query, (user_id, book_id, borrow_date, return_date))
            conn.commit()
            print("Book has been successfully uploaded! ")
        
        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()