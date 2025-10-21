"""
GUI适配器

实现 UserInterfaceService 接口，提供基于Tkinter的用户界面功能。
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import time
from typing import Optional
from src.core.ports import UserInterfaceService


class TkinterGUIAdapter(UserInterfaceService):
    """
    Tkinter GUI适配器
    
    使用Tkinter库实现用户界面交互功能。
    """
    
    def __init__(self):
        """
        初始化GUI适配器
        
        创建一个隐藏的根窗口用于显示对话框。
        """
        self.root = None
    
    def _ensure_root_window(self):
        """
        确保根窗口存在
        
        如果根窗口不存在，则创建一个隐藏的根窗口。
        """
        if self.root is None or not self.root.winfo_exists():
            self.root = tk.Tk()
            self.root.withdraw()  # 隐藏根窗口
    
    def select_directory(self, title: str) -> Optional[str]:
        """
        显示目录选择对话框
        
        Args:
            title: 对话框标题
            
        Returns:
            Optional[str]: 选择的目录路径，取消返回None
        """
        self._ensure_root_window()
        return filedialog.askdirectory(title=title)
    
    def show_message(self, title: str, message: str, message_type: str = "info") -> None:
        """
        显示消息框
        
        Args:
            title: 消息框标题
            message: 消息内容
            message_type: 消息类型 ("info", "warning", "error")
        """
        self._ensure_root_window()
        
        if message_type == "warning":
            messagebox.showwarning(title, message)
        elif message_type == "error":
            messagebox.showerror(title, message)
        else:  # 默认 info
            messagebox.showinfo(title, message)
    
    def format_duration(self, seconds: float) -> str:
        """
        格式化时长显示
        
        Args:
            seconds: 秒数
            
        Returns:
            str: 格式化后的时长字符串 (HH:MM:SS)
        """
        try:
            return time.strftime("%H:%M:%S", time.gmtime(seconds))
        except Exception:
            return "00:00:00"