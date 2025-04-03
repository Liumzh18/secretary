import customtkinter as ctk
from views.task_view import TaskView
from views.plan_view import PlanView
from views.tracking_view import TrackingView

class SecretaryApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # 设置应用主题
        ctk.set_appearance_mode("light")  # 可选: "light" 或 "dark"
        ctk.set_default_color_theme("green")
        
        self.title("秘书管理系统")
        self.geometry("1200x800")
        self.minsize(800, 600)
        
        # 使窗口居中
        self.center_window()
        self.init_ui()

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 1200) // 2
        y = (screen_height - 800) // 2
        self.geometry(f'+{x}+{y}')

    def init_ui(self):
        # 创建选项卡
        tab_control = ctk.CTkTabview(self)
        tab_control.pack(fill="both", expand=True, padx=10, pady=10)

        # 添加任务管理选项卡
        task_tab = TaskView(tab_control.add("任务管理"))

        # 添加任务规划选项卡
        plan_tab = PlanView(tab_control.add("任务规划"))

        # 添加任务跟踪选项卡
        tracking_tab = TrackingView(tab_control.add("任务跟踪"))

if __name__ == "__main__": 
    app = SecretaryApp()
    app.mainloop()