"""
文件系统适配器

实现 FileSystemService 接口，提供实际的文件系统操作。
"""

import os
import shutil
from src.core.ports import FileSystemService


class PythonFileSystemAdapter(FileSystemService):
    """
    Python 文件系统适配器
    
    使用 Python 标准库实现文件系统操作。
    """
    
    def copy_file(self, source_path: str, destination_path: str) -> bool:
        """
        复制文件
        
        Args:
            source_path: 源文件路径
            destination_path: 目标文件路径
            
        Returns:
            bool: 复制成功返回True
        """
        try:
            shutil.copy2(source_path, destination_path)
            return True
        except Exception:
            return False
    
    def move_file(self, source_path: str, destination_path: str) -> bool:
        """
        移动文件
        
        Args:
            source_path: 源文件路径
            destination_path: 目标文件路径
            
        Returns:
            bool: 移动成功返回True
        """
        try:
            shutil.move(source_path, destination_path)
            return True
        except Exception:
            return False
    
    def ensure_directory_exists(self, directory: str) -> bool:
        """
        确保目录存在，如果不存在则创建
        
        Args:
            directory: 目录路径
            
        Returns:
            bool: 目录存在或创建成功返回True
        """
        try:
            os.makedirs(directory, exist_ok=True)
            return True
        except Exception:
            return False
    
    def paths_are_equal(self, path1: str, path2: str) -> bool:
        """
        比较两个路径是否相同
        
        Args:
            path1: 第一个路径
            path2: 第二个路径
            
        Returns:
            bool: 如果路径相同返回True
        """
        try:
            return os.path.normpath(path1) == os.path.normpath(path2)
        except Exception:
            return False