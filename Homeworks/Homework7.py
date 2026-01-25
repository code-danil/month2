import sqlite3


def get_connection():
    conn1 = sqlite3.connect('books.db')
    return conn1


def create_table(conn1):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
    name TEXT,
    author TEXT,
    publication_year INTEGER,
    genre TEXT,
    number_of_pages INTEGER,
    number_of_copies INTEGER
    
    )
    """)
    conn.commit()


def insert_books(conn1):
    cursor = conn.cursor()
    books_list = [
        ('Книга 1', 'Автор 1', 2000, 'Жанр 1', 300, 5),
        ('Книга 2', 'Автор 2', 2001, 'Жанр 2', 400, 3),
        ('Книга 3', 'Автор 3', 2002, 'Жанр 3', 500, 2),
        ('Книга 4', 'Автор 4', 2003, 'Жанр 4', 600, 1),
        ('Книга 5', 'Автор 5', 2004, 'Жанр 5', 700, 6),
        ('Книга 6', 'Автор 6', 2006, 'Жанр 6', 800, 7),
        ('Книга 7', 'Автор 7', 2007, 'Жанр 7', 900, 8),
        ('Книга 8', 'Автор 8', 2008, 'Жанр 8', 100, 9),

    ]
    cursor.executemany('''
            INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)
        ''', books_list)
    conn.commit()


if __name__ == '__main__':
    conn = get_connection()
    create_table(conn)
    insert_books(conn)
    conn.close()
