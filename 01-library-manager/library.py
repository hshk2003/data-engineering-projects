import psycopg2
from psycopg2 import sql

def create_books_table():
    """Create the books table if it doesn't exist"""
    conn = connect_to_db()
    if conn is None:
        print("Failed to connect to database")
        return False
    
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS books (
                        id SERIAL PRIMARY KEY,
                        title VARCHAR(255) NOT NULL,
                        author VARCHAR(255) NOT NULL,
                        year INTEGER,
                        genre VARCHAR(100)
                    )
                """)
        print("Books table created successfully (or already exists)")
        return True
    except Exception as e:
        print(f"Error creating table: {e}")
        return False
    finally:
        conn.close()

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="books",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        return conn  # Return the connection object
    except Exception as e:
        print(f"Error connecting with database: {e}")
        return None

    
def add_book(title, author, year, genre):
    conn = connect_to_db()
    if conn is None:
        print("Failed to connect to database")
        return
    
    try:
        with conn:
            with conn.cursor() as cur:  
                cur.execute(
                    "INSERT INTO books (title, author, year, genre) VALUES (%s, %s, %s, %s)",
                    (title, author, year, genre)
                )
        print(f"Added: {title}")
    except Exception as e:
        print(f"Error adding book: {e}")
    finally:
        conn.close()
    

def search_book(query):
    conn = connect_to_db()
    if conn is None:
        print("Failed to connect to database")
        return []
    
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM books WHERE title ILIKE %s",  # ILIKE for case-insensitive search
                    (f"%{query}%",)
                )
                return cur.fetchall()
    except Exception as e:
        print(f"Error searching books: {e}")
        return []
    finally:
        conn.close()

def interface():
    # Create table on startup
    if not create_books_table():
        print("Failed to create database table. Exiting.")
        return
    
    while True:
        print("\n1. Search Book\n2. Add Book\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            query = input("Enter book title to search: ")
            results = search_book(query)
            if results:
                for book in results:
                    print(f"Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Genre: {book[4]}")
            else:
                print("No books found.")
        elif choice == '2':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter publication year: ")
            genre = input("Enter book genre: ")
            add_book(title, author, year, genre)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    interface()