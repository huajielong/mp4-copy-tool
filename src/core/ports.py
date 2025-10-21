"""
核心端口定义

清洁架构中的端口层，定义系统内部与外部世界交互的接口。
这些接口由外部适配器实现，内部用例层通过这些接口与外部交互。
"""

from typing import List, Optional
from abc import ABC, abstractmethod
from .entities import VideoFile, FilterCriteria, FileOperationResult


class VideoFileRepository(ABC):
    """
    视频文件仓库接口
    
    定义获取和操作视频文件的抽象方法，由外部适配器实现。
    """
    
    @abstractmethod
    def get_video_duration(self, file_path: str) -> float:
        """
        获取视频文件的时长
        
        Args:
            file_path: 视频文件路径
            
        Returns:
            float: 视频时长（秒），失败返回0
        """
        pass
    
    @abstractmethod
    def find_mp4_files(self, directory: str) -> List[VideoFile]:
        """
        查找目录中的所有MP4文件
        
        Args:
            directory: 要搜索的目录
            
        Returns:
            List[VideoFile]: 找到的视频文件列表
        """
        pass


class FileSystemService(ABC):
    """
    文件系统服务接口
    
    定义文件操作的抽象方法，由外部适配器实现。
    """
    
    @abstractmethod
    def copy_file(self, source_path: str, destination_path: str) -> bool:
        """
        复制文件
        
        Args:
            source_path: 源文件路径
            destination_path: 目标文件路径
            
        Returns:
            bool: 复制成功返回True
        """
        pass
    
    @abstractmethod
    def move_file(self, source_path: str, destination_path: str) -> bool:
        """
        移动文件
        
        Args:
            source_path: 源文件路径
            destination_path: 目标文件路径
            
        Returns:
            bool: 移动成功返回True
        """
        pass
    
    @abstractmethod
    def ensure_directory_exists(self, directory: str) -> bool:
        """
        确保目录存在，如果不存在则创建
        
        Args:
            directory: 目录路径
            
        Returns:
            bool: 目录存在或创建成功返回True
        """
        pass
    
    @abstractmethod
    def paths_are_equal(self, path1: str, path2: str) -> bool:
        """
        比较两个路径是否相同
        
        Args:
            path1: 第一个路径
            path2: 第二个路径
            
        Returns:
            bool: 如果路径相同返回True
        """
        pass


class UserInterfaceService(ABC):
    """
    用户界面服务接口
    
    定义用户交互相关的抽象方法，由外部GUI适配器实现。
    """
    
    @abstractmethod
    def select_directory(self, title: str) -> Optional[str]:
        """
        显示目录选择对话框
        
        Args:
            title: 对话框标题
            
        Returns:
            Optional[str]: 选择的目录路径，取消返回None
        """
        pass
    
    @abstractmethod
    def show_message(self, title: str, message: str, message_type: str = "info") -> None:
        """
        显示消息框
        
        Args:
            title: 消息框标题
            message: 消息内容
            message_type: 消息类型 ("info", "warning", "error")
        """
        pass
    
    @abstractmethod
    def format_duration(self, seconds: float) -> str:
        """
        格式化时长显示
        
        Args:
            seconds: 秒数
            
        Returns:
            str: 格式化后的时长字符串
        """
        pass