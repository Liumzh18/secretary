from models.tracking import Tracking
from utils.database import Database

class TrackingService:
    def __init__(self):
        self.db = Database()
        self.init_table()
    
    def init_table(self):
        self.db.cursor.execute('''
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
        self.db.conn.commit()