from class_genres import Genre_Class

from library_connection import connect_database

conn = connect_database()

genre_class = Genre_Class

genres = []

def genre_main(db_connection):
    cursor = db_connection.cursor(dictionary=True)
    while True:
        print("Genre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Back to main menu")
        choice = input("Enter choice: ")

        if choice == '1':
            add_genre(cursor, db_connection)
        elif choice == '2':
            view_genre_details(cursor)
        elif choice == '3':
            display_all_genres(cursor)
        elif choice == '4':
            break
        else:
            print("Please enter a valid number.")
    cursor.close()

def add_genre(cursor, db_connection):
    name = input("Enter genre name: ")

    # Validate genre name
    if not name.isalpha():
        print("Genre name must contain only alphabetic characters.")
        return

    cursor.execute("INSERT INTO genres (name) VALUES (%s)", (name,))
    db_connection.commit()
    print("Genre added successfully.")

def view_genre_details(cursor):
    genre_id = input("Enter genre ID: ")
    cursor.execute("SELECT * FROM genres WHERE id = %s", (genre_id,))
    genre = cursor.fetchone()
    if genre:
        print(genre)
    else:
        print("Genre not found.")

def display_all_genres(cursor):
    cursor.execute("SELECT * FROM genres")
    genres = cursor.fetchall()
    for genre in genres:
        print(genre)

def add_new_genre():
    if conn is not None:
        try:
            cursor = conn.cursor()
            name = input("Enter the new genre's name: ")
            description = input ("Enter the description: ") 
            category = input("Enter the genre category: ")
            new_genre = (name, description, category)
            query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"
            cursor.execute(query, new_genre)
            conn.commit()
            print("New genre added to the system.")
        
        except Exception as e:
            print(f"Error {e}")
        
        finally:
            cursor.close()
            conn.close()
                
def view_genres():
   if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM genres"
            cursor.execute(query)
            conn.commit()
            for row in cursor.fetchone():
                print(row)
        
        except Exception as e:
            print(f"Error {e}")
        
        finally:
            cursor.close()
            conn.close()
        

def display_genres():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "insert here"
            cursor.execute(query)
            conn.commit()
            for row in cursor.fetchall():
                print(row)
        
        except Exception as e:
            print(f"Error {e}")
        
        finally:
            cursor.close()
            conn.close()