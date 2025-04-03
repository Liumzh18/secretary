import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class AppTheme:
    @staticmethod
    def setup():
        # 创建浅色主题
        style = ttk.Style("litera")  # 使用类似 Notion 的亮色主题
        
        # 自定义颜色
        style.configure('primary.TButton', 
                       font=('SF Pro Display', 11),
                       padding=10)
        
        style.configure('TNotebook', 
                       background='#ffffff',
                       tabmargins=[2, 5, 2, 0])
        
        style.configure('TNotebook.Tab', 
                       padding=[15, 5],
                       font=('SF Pro Display', 11))
        
        style.configure('Treeview', 
                       font=('SF Pro Display', 11),
                       rowheight=40)
        
        style.configure('Treeview.Heading', 
                       font=('SF Pro Display', 11, 'bold'))
        
        return style