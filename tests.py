import sqlite3

import sqlite3

def inspect_schema(db_path):
    """
    Display the complete schema of a SQLite database.

    Args:
        db_path (str): Path to the SQLite database file
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query to get all tables
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' 
            ORDER BY name;
        """)
        tables = cursor.fetchall()

        print("Database Schema:")
        print("---------------")

        # For each table, get its schema
        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()

            print(f"\nTable: {table_name}")
            print("Columns:")
            for col in columns:
                # col contains: (id, name, type, notnull, default_value, primary_key)
                print(f"  - {col[1]}: {col[2]}", end="")
                if col[5] == 1:  # Is primary key
                    print(" (PRIMARY KEY)", end="")
                if col[3] == 1:  # Not null
                    print(" NOT NULL", end="")
                print()

        conn.close()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
inspect_schema('airplain.db')
