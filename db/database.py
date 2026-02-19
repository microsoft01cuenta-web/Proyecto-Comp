import sqlite3

def initialize_database():
    # Create a new database or connect to an existing one
    conn = sqlite3.connect('sensor_database.db')
    c = conn.cursor()

    # Create sensors table
    c.execute('''CREATE TABLE IF NOT EXISTS sensors (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    type TEXT NOT NULL
                )''')

    # Create users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )''')

    # Create sensor_data table
    c.execute('''CREATE TABLE IF NOT EXISTS sensor_data (
                    id INTEGER PRIMARY KEY,
                    sensor_id INTEGER,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    value REAL,
                    FOREIGN KEY (sensor_id) REFERENCES sensors (id)
                )''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_database()