from datetime import datetime

class Task:
    def __init__(self, title, description, deadline=None, priority='中'):
        self.id = None
        self.title = title
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.status = '未开始'
        self.create_time = datetime.now()
        self.update_time = datetime.now()