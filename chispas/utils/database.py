import sqlite3

def initialize_database():
    # Connect to SQLite database (it will create a file if it doesn't exist)
    conn = get_db_connection()

    # Create a cursor object to execute SQL queries
    c = conn.cursor()

    # Create table for users
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    native_language TEXT NOT NULL
                );''')

    # Create table for unknown words
    c.execute('''CREATE TABLE IF NOT EXISTS unknown_words (
                    word_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    word TEXT NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES users(user_id)
                );''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def store_unknown_words(user_id, unknown_words):
    # Connect to SQLite database
    conn = get_db_connection()

    # Create a cursor object to execute SQL queries
    c = conn.cursor()
    
    # Split by comma and strip the leading and trailing spaces and double quotes
    split_words_and_phrases = [word.strip().strip('"') for word in unknown_words.split(",")]

    # Store the unknown words in the database
    for word in split_words_and_phrases:
        c.execute('INSERT INTO unknown_words (user_id, word) VALUES (?, ?)', (user_id, word))

    # Commit the changes and close the connection
    conn.commit()

def get_unknown_words(user_id):
    conn = get_db_connection()
    unknown_words = conn.execute('SELECT word FROM unknown_words WHERE user_id = :user_id', { 'user_id': user_id }).fetchall()
    conn.close()
    
    if not unknown_words:
        return []
    

    # Unzip the list of one-element tuples into a list
    unquoted_words = list(zip(*unknown_words))[0]

    # Add quotes around each word
    quoted_words = [f'"{word}"' for word in unquoted_words]

    return quoted_words

def get_db_connection():
    conn = sqlite3.connect('language_learning_app.db')
    return conn


def erase_unknown_words_table():
    # Connect to SQLite database
    conn = get_db_connection()

    # Create a cursor object to execute SQL queries
    c = conn.cursor()

    # Execute SQL query to delete all entries from the unknown_words table
    c.execute('DELETE FROM unknown_words')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()