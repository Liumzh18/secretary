import sqlite3
from pathlib import Path

class Database:
    def __init__(self):
        db_path = Path('D:/secretary/data/secretary.db')
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(db_path))
        self.cursor = self.conn.cursor()
        self.init_tables()
    
    def init_tables(self):
        # Tasks table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            deadline DATE,
            priority TEXT,
            status TEXT,
            create_time DATETIME,
            update_time DATETIME
        )
        ''')
        
        # Plans table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER,
            start_date DATE,
            end_date DATE,
            progress INTEGER,
            create_time DATETIME,
            update_time DATETIME,
            FOREIGN KEY (task_id) REFERENCES tasks (id)
        )
        ''')
        
        # Tracking table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS tracking (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER,
            status TEXT,
            completion_rate INTEGER,
            create_time DATETIME,
            update_time DATETIME,
            FOREIGN KEY (task_id) REFERENCES tasks (id)
        )
        ''')
        
        self.conn.commit()