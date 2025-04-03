import tkinter as tk
from tkinter import ttk

class TrackingView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # 创建跟踪视图界面
        self.tracking_tree = ttk.Treeview(self, columns=('任务', '状态', '完成度', '最后更新时间'))
        self.tracking_tree.heading('任务', text='任务')
        self.tracking_tree.heading('状态', text='状态')
        self.tracking_tree.heading('完成度', text='完成度')
        self.tracking_tree.heading('最后更新时间', text='最后更新时间')
        self.tracking_tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)