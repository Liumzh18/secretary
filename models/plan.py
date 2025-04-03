from datetime import datetime

class Plan:
    def __init__(self, task_id, start_date, end_date):
        self.id = None
        self.task_id = task_id
        self.start_date = start_date
        self.end_date = end_date
        self.progress = 0
        self.create_time = datetime.now()
        self.update_time = datetime.now()