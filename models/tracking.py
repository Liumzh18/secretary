from datetime import datetime

class Tracking:
    def __init__(self, task_id, status, completion_rate):
        self.id = None
        self.task_id = task_id
        self.status = status
        self.completion_rate = completion_rate
        self.create_time = datetime.now()
        self.update_time = datetime.now()