"""
应用程序主入口

负责组装所有组件，实现依赖注入，启动应用程序。
"""

import tkinter as tk
from src.use_cases.video_file_processor import VideoFileProcessor
from src.interfaces.file_system_adapter import PythonFileSystemAdapter
from src.interfaces.video_repository_adapter import OpenCVVideoRepositoryAdapter
from src.interfaces.gui_adapter import TkinterGUIAdapter
from src.frameworks.gui_app import MP4CopyToolApp


def main():
    """
    程序主入口函数
    
    实现依赖注入，创建并组装所有组件，启动GUI应用。
    """
    # 创建适配器实例（外部框架实现）
    file_system_service = PythonFileSystemAdapter()
    video_repository = OpenCVVideoRepositoryAdapter()
    ui_service = TkinterGUIAdapter()
    
    # 创建用例实例，注入依赖（依赖抽象接口）
    video_processor = VideoFileProcessor(
        video_repository=video_repository,
        file_system_service=file_system_service
    )
    
    # 创建Tkinter主窗口
    root = tk.Tk()
    
    # 创建GUI应用，注入用例和UI服务
    app = MP4CopyToolApp(
        master=root,
        video_processor=video_processor,
        ui_service=ui_service
    )
    
    # 启动主事件循环
    root.mainloop()


if __name__ == "__main__":
    main()