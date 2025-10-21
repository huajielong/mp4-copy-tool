"""
核心实体定义

清洁架构的最内层，包含业务的核心数据结构和领域规则。
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class VideoFile:
    """
    视频文件实体类
    
    表示系统中的视频文件，包含文件路径和时长等核心属性。
    """
    
    path: str  # 文件路径
    duration: float  # 视频时长（秒）
    filename: Optional[str] = None  # 文件名（可选）
    
    def __post_init__(self):
        """初始化后处理，自动提取文件名"""
        if not self.filename:
            import os
            self.filename = os.path.basename(self.path)


@dataclass
class FilterCriteria:
    """
    文件过滤条件实体类
    
    定义用于筛选视频文件的条件，如时长范围。
    """
    
    min_duration: float = 0.0  # 最小时长（秒），左开区间
    max_duration: float = float('inf')  # 最大时长（秒），右闭区间
    
    def matches(self, video: VideoFile) -> bool:
        """
        判断视频文件是否满足过滤条件
        
        Args:
            video: 要检查的视频文件
            
        Returns:
            bool: 如果满足条件返回True，否则返回False
        """
        return self.min_duration < video.duration <= self.max_duration


class FileOperationResult:
    """
    文件操作结果类
    
    表示文件操作（复制、移动）的结果。
    """
    
    def __init__(self, success: bool, message: str = "", count: int = 0):
        """
        初始化操作结果
        
        Args:
            success: 操作是否成功
            message: 结果消息
            count: 成功操作的文件数量
        """
        self.success = success
        self.message = message
        self.count = count