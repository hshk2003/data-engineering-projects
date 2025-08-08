# Book Management System

A simple Python command-line application for managing a book database using PostgreSQL.

## Features

- **Add Books**: Store book information including title, author, publication year, and genre
- **Search Books**: Find books by title with case-insensitive partial matching
- **Database Management**: Automatically creates the required database table on startup
- **Interactive Interface**: Simple menu-driven command-line interface

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.x
- PostgreSQL database server
- psycopg2 library

## Installation

1. **Install PostgreSQL** (if not already installed):
   - Download and install PostgreSQL from [postgresql.org](https://www.postgresql.org/download/)
   - Start the PostgreSQL service

2. **Install Python dependencies**:
   ```bash
   pip install psycopg2-binary
   ```

3. **Set up the database**:
   - Create a PostgreSQL database named `books`
   - Ensure you have a PostgreSQL user with access to the database

## Database Configuration

The application connects to PostgreSQL with the following default settings:
- **Database name**: `books`
- **Username**: `postgres`
- **Password**: `postgres`
- **Host**: `localhost`
- **Port**: `5432`

To modify these settings, update the `connect_to_db()` function in the code:

```python
conn = psycopg2.connect(
    dbname="your_database_name",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)
```

## Database Schema

The application automatically creates a `books` table with the following structure:

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL PRIMARY KEY | Auto-incrementing unique identifier |
| title | VARCHAR(255) NOT NULL | Book title |
| author | VARCHAR(255) NOT NULL | Book author |
| year | INTEGER | Publication year |
| genre | VARCHAR(100) | Book genre |

## Usage

1. **Run the application**:
   ```bash
   python book_manager.py
   ```

2. **Use the interactive menu**:
   - **Option 1**: Search for books by title
   - **Option 2**: Add a new book to the database
   - **Option 3**: Exit the application

### Example Usage

```
1. Search Book
2. Add Book
3. Exit
Enter your choice: 2
Enter book title: The Great Gatsby
Enter book author: F. Scott Fitzgerald
Enter publication year: 1925
Enter book genre: Fiction
Added: The Great Gatsby

1. Search Book
2. Add Book
3. Exit
Enter your choice: 1
Enter book title to search: gatsby
Title: The Great Gatsby, Author: F. Scott Fitzgerald, Year: 1925, Genre: Fiction
```

## Functions Overview

- `connect_to_db()`: Establishes connection to PostgreSQL database
- `create_books_table()`: Creates the books table if it doesn't exist
- `add_book(title, author, year, genre)`: Adds a new book to the database
- `search_book(query)`: Searches for books by title (case-insensitive partial matching)
- `interface()`: Provides the interactive command-line interface

## Error Handling

The application includes comprehensive error handling for:
- Database connection failures
- SQL execution errors
- Invalid user input
- Missing database tables

## Security Features

- Uses parameterized queries to prevent SQL injection attacks
- Proper connection management with context managers
- Exception handling for database operations

## Troubleshooting

### Common Issues

1. **Connection Error**: 
   - Ensure PostgreSQL is running
   - Verify database credentials
   - Check if the database exists

2. **Permission Denied**:
   - Ensure the PostgreSQL user has proper permissions
   - Verify the user can create tables in the database

3. **Module Not Found Error**:
   - Install psycopg2: `pip install psycopg2-binary`

### Creating the Database

If you need to create the database manually:

```sql
-- Connect to PostgreSQL as superuser
CREATE DATABASE books;
CREATE USER your_username WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE books TO your_username;
```

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the [MIT License](LICENSE).