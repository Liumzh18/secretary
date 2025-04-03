import customtkinter as ctk
from models.task import Task
from services.task_service import TaskService
from datetime import datetime

class TaskView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.task_service = TaskService()
        self.ai_enabled = False  # AI 功能开关，默认关闭
        self.pack(fill="both", expand=True, padx=20, pady=20)
        self.init_ui()
        self.load_tasks()

    def init_ui(self):
        # 创建工具栏
        toolbar = ctk.CTkFrame(self)
        toolbar.pack(fill="x", pady=(0, 10))  # 使用 pack 的 pady 参数设置间距

        # 搜索框
        self.search_var = ctk.StringVar()
        search_entry = ctk.CTkEntry(
            toolbar,
            textvariable=self.search_var,
            placeholder_text="搜索任务",
            width=300
        )
        search_entry.pack(side="left", padx=(0, 10))  # 使用 pack 的 padx 参数设置间距

        # 添加任务按钮
        add_btn = ctk.CTkButton(
            toolbar,
            text="+ 新建任务",
            command=self.show_add_task_dialog,
            fg_color=("#2B7539", "#0C4518"),  # (light mode, dark mode)
            hover_color="#45A049"
        )
        add_btn.pack(side="left")

        # 创建任务列表
        self.task_tree = ctk.CTkScrollableFrame(self, width=800, height=400)
        self.task_tree.pack(fill="both", expand=True, pady=(10, 0))  # 使用 pack 的 pady 参数设置间距

        # 表头
        header = ctk.CTkFrame(self.task_tree)
        header.pack(fill="x")
        for col in ["标题", "优先级", "截止日期", "状态"]:
            ctk.CTkLabel(header, text=col, width=200, anchor="center").pack(side="left", padx=5)

    def show_add_task_dialog(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title("新建任务")
        dialog.geometry("600x500")
                
        frame = ctk.CTkFrame(dialog)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
                
        # 标题输入
        title_label = ctk.CTkLabel(frame, text="任务标题", font=("SF Pro Display", 12, "bold"))
        title_label.pack(anchor="w", pady=(0, 5))
        
        title_var = ctk.StringVar()
        title_entry = ctk.CTkEntry(frame, textvariable=title_var, placeholder_text="请输入任务标题")
        title_entry.pack(fill="x", pady=(0, 15))
        
        # 描述输入
        desc_label = ctk.CTkLabel(frame, text="任务描述", font=("SF Pro Display", 12, "bold"))
        desc_label.pack(anchor="w", pady=(0, 5))
                
        desc_text = ctk.CTkTextbox(frame, height=100)
        desc_text.pack(fill="x", pady=(0, 15))
        
        # AI 规划按钮
        ai_plan_btn = ctk.CTkButton(
            frame,
            text="🤖 AI 智能规划",
            command=lambda: self.show_ai_unavailable_dialog(),
            fg_color=("#6B4EFF", "#4E37B3"),  # 紫色主题
            hover_color=("#5841CC", "#3E2D8F")
        )
        ai_plan_btn.pack(fill="x", pady=(0, 15))
        
        # 按钮区域
        btn_frame = ctk.CTkFrame(frame)
        btn_frame.pack(fill="x", pady=(15, 0))
        
        cancel_btn = ctk.CTkButton(
            btn_frame,
            text="取消",
            command=dialog.destroy,
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30")
        )
        cancel_btn.pack(side="right", padx=(5, 0))
        
        save_btn = ctk.CTkButton(
            btn_frame,
            text="保存",
            command=lambda: self.save_task(
                title_var.get(),
                desc_text.get("1.0", "end-1c"),
                dialog
            )
        )
        save_btn.pack(side="right")

    def show_ai_unavailable_dialog(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title("功能未开放")
        dialog.geometry("400x200")
        
        # 确保弹窗在主窗口中心
        dialog.transient(self)
        dialog.grab_set()
        
        frame = ctk.CTkFrame(dialog)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # 图标
        icon_label = ctk.CTkLabel(
            frame, 
            text="🚧",
            font=("SF Pro Display", 48)
        )
        icon_label.pack(pady=(0, 10))
        
        # 消息
        message_label = ctk.CTkLabel(
            frame,
            text="AI 智能规划功能即将上线\n敬请期待",
            font=("SF Pro Display", 14),
            justify="center"
        )
        message_label.pack(pady=(0, 20))
        
        # 确定按钮
        ok_btn = ctk.CTkButton(
            frame,
            text="确定",
            command=dialog.destroy,
            width=100
        )
        ok_btn.pack()

    def generate_ai_plan(self, title, description, parent):
        if not title or not description:
            self.show_error("请先填写任务标题和描述")
            return
                        
        # 显示加载状态
        loading_label = ctk.CTkLabel(
            parent,
            text="AI 正在生成规划方案...",
            text_color=("gray40", "gray60")
        )
        loading_label.pack(pady=(0, 10))
                
        # 调用 AI 服务
        from services.ai_service import AIService
        ai_service = AIService()
        result = ai_service.plan_task(title, description)
                
        # 移除加载提示
        loading_label.destroy()
                
        if result:
            # 更新显示区域
            self.ai_result_text.configure(state="normal")
            self.ai_result_text.delete("1.0", "end")
                        
            # 格式化显示 AI 建议
            plan_text = "🎯 AI 规划建议：\n\n"
            plan_text += "📋 子任务清单：\n"
            for i, task in enumerate(result['subtasks'], 1):
                plan_text += f"{i}. {task}\n"
                                
            plan_text += "\n⏱ 时间预估：\n"
            for task, time in result['estimated_times'].items():
                plan_text += f"· {task}: {time}\n"
                                
            plan_text += "\n📊 执行建议：\n"
            for step in result['sequence']:
                plan_text += f"· {step}\n"
                                
            plan_text += "\n❗ 关键注意点：\n"
            for point in result['key_points']:
                plan_text += f"· {point}\n"
                                
            self.ai_result_text.insert("1.0", plan_text)
            self.ai_result_text.configure(state="disabled")
        else:
            self.show_error("AI 规划生成失败，请稍后重试")

    def show_error(self, message):
        dialog = ctk.CTkDialogbox(self)
        dialog.title("错误")
        dialog.add_label(message)
        dialog.add_button("确定", command=dialog.destroy)

    def save_task(self, title, description, dialog):
        if not title:
            ctk.CTkMessagebox.show_error("任务标题不能为空！", "错误")
            return
        task = Task(title=title, description=description)
        self.task_service.add_task(task)
        dialog.destroy()
        self.load_tasks()

    def load_tasks(self):
        # 清空任务列表
        for widget in self.task_tree.winfo_children():
            widget.destroy()

        # 加载任务
        tasks = self.task_service.get_all_tasks()
        for task in tasks:
            row = ctk.CTkFrame(self.task_tree)
            row.pack(fill="x", pady=5)
            ctk.CTkLabel(row, text=task.title, width=200, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=task.priority, width=200, anchor="center").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=task.deadline or "无", width=200, anchor="center").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=task.status, width=200, anchor="center").pack(side="left", padx=5)