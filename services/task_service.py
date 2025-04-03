from datetime import datetime
from models.task import Task
from utils.database import Database

class TaskService:
    def __init__(self):
        self.db = Database()
        
    def add_task(self, task: Task):
        sql = '''INSERT INTO tasks (title, description, deadline, priority, 
                status, create_time, update_time)
                VALUES (?, ?, ?, ?, ?, ?, ?)'''
        self.db.cursor.execute(sql, (
            task.title,
            task.description,
            task.deadline,
            task.priority,
            task.status,
            task.create_time,
            task.update_time
        ))
        self.db.conn.commit()
        task.id = self.db.cursor.lastrowid
        return task
    
    def get_all_tasks(self):
        self.db.cursor.execute('SELECT * FROM tasks')
        rows = self.db.cursor.fetchall()
        tasks = []
        for row in rows:
            task = Task(row[1], row[2])
            task.id = row[0]
            task.deadline = row[3]
            task.priority = row[4]
            task.status = row[5]
            task.create_time = datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S.%f')
            task.update_time = datetime.strptime(row[7], '%Y-%m-%d %H:%M:%S.%f')
            tasks.append(task)
        return tasks
    
    def update_task(self, task: Task):
        sql = '''UPDATE tasks 
                SET title=?, description=?, deadline=?, priority=?, 
                    status=?, update_time=?
                WHERE id=?'''
        task.update_time = datetime.now()
        self.db.cursor.execute(sql, (
            task.title,
            task.description,
            task.deadline,
            task.priority,
            task.status,
            task.update_time,
            task.id
        ))
        self.db.conn.commit()
        
    def delete_task(self, task_id: int):
        sql = 'DELETE FROM tasks WHERE id=?'
        self.db.cursor.execute(sql, (task_id,))
        self.db.conn.commit()