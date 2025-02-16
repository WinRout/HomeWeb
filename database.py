import sqlite3
import datetime

def setup_database():
    """Initialize the SQLite database and create tables if they don't exist."""
    with sqlite3.connect('properties.db') as conn:
        cursor = conn.cursor()
        # Create tables for properties
        cursor.execute('''CREATE TABLE IF NOT EXISTS spitogatos (id TEXT PRIMARY KEY, modified TEXT, url TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS xe (id TEXT PRIMARY KEY, modified TEXT, url TEXT)''')
        # Create table for execution log
        cursor.execute('''CREATE TABLE IF NOT EXISTS execution_log (id INTEGER PRIMARY KEY, last_execution TEXT)''')
        conn.commit()

def save_properties(properties: list, table_name: str) -> tuple:
    """Save properties to the database and return new and modified IDs."""
    with sqlite3.connect('properties.db') as conn:
        cursor = conn.cursor()
        stored_properties = {row[0]: row[2] for row in cursor.execute(f'SELECT * FROM {table_name}')}
        new_ids, modified_ids = [], []

        for prop in properties:
            if prop['id'] not in stored_properties:
                cursor.execute(f'INSERT INTO {table_name} (id, modified, url) VALUES (?, ?, ?)',
                               (prop['id'], prop['modified'], prop['url']))
                new_ids.append(prop['id'])
            elif prop['modified'] != stored_properties[prop['id']]:
                cursor.execute(f'UPDATE {table_name} SET modified = ? WHERE id = ?', (prop['modified'], prop['id']))
                modified_ids.append(prop['id'])

        conn.commit()
        return new_ids, modified_ids

def update_execution_time():
    """Update the last execution time in the database."""
    execution_time = datetime.datetime.now().isoformat()
    with sqlite3.connect('properties.db') as conn:
        cursor = conn.cursor()
        # Insert or update the execution time
        cursor.execute('INSERT OR REPLACE INTO execution_log (id, last_execution) VALUES (1, ?)', (execution_time,))
        conn.commit()

def get_last_execution_time():
    """Retrieve the last execution time from the database. If not found, return the current time."""
    with sqlite3.connect('properties.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT last_execution FROM execution_log WHERE id = 1')
        row = cursor.fetchone()
        return row[0] if row else datetime.datetime.now().isoformat()