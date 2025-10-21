"""
图形用户界面应用

清洁架构的框架层，实现实际的GUI界面，依赖于接口适配器层。
"""

import tkinter as tk
import sys
from typing import List, Optional
from src.core.entities import VideoFile
from src.use_cases.video_file_processor import VideoFileProcessor
from src.core.ports import UserInterfaceService


class MP4CopyToolApp:
    """
    MP4文件拷贝工具GUI应用
    
    实现基于Tkinter的图形界面，处理用户交互并调用用例层处理业务逻辑。
    """
    
    def __init__(self, 
                 master: tk.Tk,
                 video_processor: VideoFileProcessor,
                 ui_service: UserInterfaceService):
        """
        初始化GUI应用
        
        Args:
            master: Tkinter主窗口
            video_processor: 视频文件处理器
            ui_service: 用户界面服务
        """
        self.master = master
        self.video_processor = video_processor
        self.ui_service = ui_service
        
        # 设置窗口标题
        master.title("MP4文件拷贝工具")
        
        # 初始化变量
        self.input_dir: str = ""
        self.output_dir: str = ""
        self.file_list: List[VideoFile] = []
        
        # 创建UI组件
        self._create_widgets()
        
        # 布局UI组件
        self._layout_widgets()
        
        # 绑定窗口关闭事件
        master.protocol("WM_DELETE_WINDOW", self._on_closing)
    
    def _create_widgets(self):
        """
        创建所有UI组件
        """
        # 输入目录相关组件
        self.lbl_input = tk.Label(self.master, text="输入目录：未选择")
        self.btn_input = tk.Button(self.master, text="选择输入目录", command=self.select_input)
        
        # 输出目录相关组件
        self.lbl_output = tk.Label(self.master, text="输出目录：未选择")
        self.btn_output = tk.Button(self.master, text="选择输出目录", command=self.select_output)
        
        # 文件列表相关组件
        self.listbox = tk.Listbox(self.master, width=80, height=15)  # 文件列表框
        self.scrollbar = tk.Scrollbar(self.master, orient="vertical")  # 垂直滚动条
        
        # 绑定滚动条和列表框
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        
        # 时长选择相关组件
        self.lbl_duration = tk.Label(self.master, text="时长范围（秒）:")
        self.entry_min = tk.Entry(self.master, width=8)  # 最小时长输入框
        self.entry_max = tk.Entry(self.master, width=8)  # 最大时长输入框
        self.lbl_example = tk.Label(self.master, text="示例: (0,30] 或 [55,120] 或 [56,)")  # 提示文本
        
        # 操作按钮相关组件
        self.copy_btn = tk.Button(self.master, text="开始拷贝", command=self.start_copy)
        self.move_btn = tk.Button(self.master, text="开始移动", command=self.start_move)
        self.badge = tk.Canvas(self.master, width=20, height=20, highlightthickness=0)  # 计数徽章
    
    def _layout_widgets(self):
        """
        布局所有UI组件
        """
        self.lbl_input.grid(row=0, column=0, sticky="w", padx=5)
        self.btn_input.grid(row=0, column=1, padx=5)
        self.lbl_output.grid(row=1, column=0, sticky="w", padx=5)
        self.btn_output.grid(row=1, column=1, padx=5)
        self.listbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.scrollbar.grid(row=2, column=2, sticky="ns")
        self.lbl_duration.grid(row=3, column=0, sticky="w", padx=5)
        self.entry_min.grid(row=3, column=0, padx=(70,5))
        self.entry_max.grid(row=3, column=0, padx=(120,5))
        self.lbl_example.grid(row=3, column=1, sticky="w")
        self.copy_btn.grid(row=4, column=0, pady=10)
        self.move_btn.grid(row=4, column=1, padx=(0, 40), pady=10)
        self.badge.grid(row=4, column=2)
    
    def update_badge(self, count: int):
        """
        更新计数徽章的显示
        
        Args:
            count: 要显示的文件数量
        """
        self.badge.delete("all")  # 清除现有内容
        if count > 0:
            # 创建红色圆形背景
            self.badge.create_oval(2, 2, 18, 18, fill="red", outline="")
            # 显示计数文本
            self.badge.create_text(10, 10, text=str(count), fill="white")
    
    def select_input(self):
        """
        选择输入目录
        """
        self.input_dir = self.ui_service.select_directory("选择输入目录")
        if self.input_dir:
            # 更新标签显示
            self.lbl_input.config(text=f"输入目录：{self.input_dir}")
            # 刷新文件列表
            self.refresh_file_list()
    
    def select_output(self):
        """
        选择输出目录
        """
        self.output_dir = self.ui_service.select_directory("选择输出目录")
        if self.output_dir:
            # 更新标签显示
            self.lbl_output.config(text=f"输出目录：{self.output_dir}")
    
    def refresh_file_list(self):
        """
        刷新并显示输入目录中的MP4文件列表
        """
        self.listbox.delete(0, tk.END)  # 清空列表框
        
        if not self.input_dir:
            return
        
        # 获取视频文件列表
        self.file_list = self.video_processor.get_videos_from_directory(self.input_dir)
        
        # 在列表框中显示文件
        for video in self.file_list:
            formatted_duration = self.ui_service.format_duration(video.duration)
            self.listbox.insert(tk.END, f"{video.path} | 时长: {formatted_duration}")
    
    def _parse_duration_filter(self) -> tuple:
        """
        解析时长过滤条件
        
        Returns:
            tuple: (min_duration, max_duration)
        """
        # 移除括号和方括号
        min_val = self.entry_min.get().strip('()[]')
        max_val = self.entry_max.get().strip('()[]')
        
        # 转换为浮点数，空值分别设为0和无穷大
        min_sec = float(min_val) if min_val else 0.0
        max_sec = float(max_val) if max_val else float('inf')
        
        return min_sec, max_sec
    
    def _file_progress_callback(self, video: VideoFile, count: int):
        """
        文件处理进度回调函数
        
        Args:
            video: 当前处理的视频文件
            count: 已处理的文件数量
        """
        # 查找视频在列表中的索引
        for i, v in enumerate(self.file_list):
            if v.path == video.path:
                # 高亮显示已处理的文件
                self.listbox.itemconfig(i, bg='#e0ffe0')
                break
        
        # 更新界面
        self.master.update()
    
    def start_copy(self):
        """
        开始复制符合条件的文件
        """
        # 目录校验
        if not self.input_dir:
            self.ui_service.show_message("警告", "请选择输入目录", "warning")
            return
        
        if not self.output_dir:
            self.ui_service.show_message("警告", "请选择输出目录", "warning")
            return
        
        # 解析时长过滤条件
        min_sec, max_sec = self._parse_duration_filter()
        
        # 筛选符合条件的文件
        filtered_videos = self.video_processor.filter_videos_by_duration(
            self.file_list, min_sec, max_sec
        )
        
        # 更新计数徽章
        self.update_badge(len(filtered_videos))
        
        # 检查是否有符合条件的文件
        if not filtered_videos:
            self.ui_service.show_message("提示", "没有符合要求的文件")
            return
        
        # 执行复制操作
        result = self.video_processor.copy_filtered_videos(
            self.input_dir,
            self.output_dir,
            min_sec,
            max_sec,
            self._file_progress_callback
        )
        
        # 更新计数徽章
        self.update_badge(0)
        
        # 显示结果
        if result.success:
            self.ui_service.show_message("完成", result.message)
        else:
            self.ui_service.show_message("错误", result.message, "error")
    
    def _on_closing(self):
        """
        处理窗口关闭事件
        确保程序能够完全退出
        """
        self.master.destroy()
        sys.exit(0)
    
    def start_move(self):
        """
        开始移动符合条件的文件
        """
        # 目录校验
        if not self.input_dir:
            self.ui_service.show_message("警告", "请选择输入目录", "warning")
            return
        
        if not self.output_dir:
            self.ui_service.show_message("警告", "请选择输出目录", "warning")
            return
        
        # 解析时长过滤条件
        min_sec, max_sec = self._parse_duration_filter()
        
        # 筛选符合条件的文件
        filtered_videos = self.video_processor.filter_videos_by_duration(
            self.file_list, min_sec, max_sec
        )
        
        # 更新计数徽章
        self.update_badge(len(filtered_videos))
        
        # 检查是否有符合条件的文件
        if not filtered_videos:
            self.ui_service.show_message("提示", "没有符合要求的文件")
            return
        
        # 执行移动操作
        result = self.video_processor.move_filtered_videos(
            self.input_dir,
            self.output_dir,
            min_sec,
            max_sec,
            self._file_progress_callback
        )
        
        # 更新计数徽章
        self.update_badge(0)
        
        # 显示结果
        if result.success:
            self.ui_service.show_message("完成", result.message)
            # 移动完成后刷新文件列表（因为原位置的文件已被移除）
            self.refresh_file_list()
        else:
            self.ui_service.show_message("错误", result.message, "error")