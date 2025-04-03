from models.plan import Plan
from utils.database import Database

class PlanService:
    def __init__(self):
        self.db = Database()
        self.init_table()
    
    def init_table(self):
        self.db.cursor.execute('''
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
        self.db.conn.commit()