from class_users import UserClass

from library_connection import connect_database


conn = connect_database()

users = []

def user_op_menu(db_connection):
    cursor = db_connection.cursor(dictionary=True)
    while True:
        print("User Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to main menu")
        choice = input("Enter choice: ")

        if choice == '1':
            add_user(cursor, db_connection)
        elif choice == '2':
            view_user_details(cursor)
        elif choice == '3':
            display_all_users(cursor)
        elif choice == '4':
            break
        else:
            print("Please enter a valid number.")
    cursor.close()

def add_user(cursor, db_connection):
    name = input("Enter user name: ")
    library_id = input("Enter library ID: ")

    # Validate user name
    if not name.replace(" ", "").isalpha():
        print("User name must contain only alphabetic characters.")
        return

    # Validate library ID
    if not library_id.isdigit():
        print("Library ID must be an integer.")
        return

    cursor.execute("INSERT INTO users (name, library_id) VALUES (%s, %s)", (name, library_id))
    db_connection.commit()
    print("User added successfully.")

def view_user_details(cursor):
    user_id = input("Enter user ID: ")
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    if user:
        print(user)
    else:
        print("User not found.")

def display_all_users(cursor):
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)
        
def add_new_user():
    if conn is not None:
        try:
            cursor = conn.cursor()
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            library_id = input("Enter library ID: ")
            new_user = (first_name, last_name, library_id)
            query = "INSERT INTO users (first_name, last_name, library_id) VALUES (%s, %s, %s)"
            cursor.execute(query, new_user)
            conn.commit()
            print("New user added to the library system.")
        
        except Exception as e:
            print(f"Error {e}")
        
        finally:
            cursor.close()
            conn.close()

def view_users():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE id = %s"
            cursor.execute(query)
            conn.commit()
            for row in cursor.fetchone():
                print(row)
        
        except Exception as e:
            print(f"Error {e}")
        
        finally:
            cursor.close()
            conn.close()


def display_all_details():
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM users"
            cursor.execute(query)
            conn.commit()
            for row in cursor.fetchall():
                print(row)
        
        except Exception as e:
            print(f"Error {e}")
        
        finally:
            cursor.close()
            conn.close()