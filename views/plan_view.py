import tkinter as tk
from tkinter import ttk

class PlanView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # 创建规划视图界面
        self.plan_tree = ttk.Treeview(self, columns=('任务', '计划开始时间', '计划结束时间', '进度'))
        self.plan_tree.heading('任务', text='任务')
        self.plan_tree.heading('计划开始时间', text='计划开始时间')
        self.plan_tree.heading('计划结束时间', text='计划结束时间')
        self.plan_tree.heading('进度', text='进度')
        self.plan_tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)