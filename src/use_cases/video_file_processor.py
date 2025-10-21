"""
视频文件处理用例

清洁架构的用例层，实现具体的业务逻辑，依赖于核心层的端口接口。
"""

from typing import List, Optional
from src.core.entities import VideoFile, FilterCriteria, FileOperationResult
from src.core.ports import VideoFileRepository, FileSystemService


class VideoFileProcessor:
    """
    视频文件处理器
    
    实现视频文件的查找、过滤、复制和移动等核心业务逻辑。
    """
    
    def __init__(self, 
                 video_repository: VideoFileRepository,
                 file_system_service: FileSystemService):
        """
        初始化视频文件处理器
        
        Args:
            video_repository: 视频文件仓库接口
            file_system_service: 文件系统服务接口
        """
        self.video_repository = video_repository
        self.file_system_service = file_system_service
    
    def get_videos_from_directory(self, directory: str) -> List[VideoFile]:
        """
        从目录获取视频文件列表
        
        Args:
            directory: 要搜索的目录
            
        Returns:
            List[VideoFile]: 视频文件列表
        """
        return self.video_repository.find_mp4_files(directory)
    
    def filter_videos_by_duration(self, 
                                 videos: List[VideoFile],
                                 min_duration: float = 0.0,
                                 max_duration: float = float('inf')) -> List[VideoFile]:
        """
        按时长过滤视频文件
        
        Args:
            videos: 要过滤的视频文件列表
            min_duration: 最小时长（左开区间）
            max_duration: 最大时长（右闭区间）
            
        Returns:
            List[VideoFile]: 符合条件的视频文件列表
        """
        criteria = FilterCriteria(min_duration, max_duration)
        return [video for video in videos if criteria.matches(video)]
    
    def copy_filtered_videos(self, 
                           input_dir: str,
                           output_dir: str,
                           min_duration: float = 0.0,
                           max_duration: float = float('inf'),
                           progress_callback=None) -> FileOperationResult:
        """
        复制符合条件的视频文件
        
        Args:
            input_dir: 输入目录
            output_dir: 输出目录
            min_duration: 最小时长
            max_duration: 最大时长
            progress_callback: 进度回调函数 (可选)
            
        Returns:
            FileOperationResult: 操作结果
        """
        try:
            # 确保输出目录存在
            if not self.file_system_service.ensure_directory_exists(output_dir):
                return FileOperationResult(False, "无法创建输出目录")
            
            # 检查目录是否相同
            if self.file_system_service.paths_are_equal(input_dir, output_dir):
                return FileOperationResult(False, "输入目录和输出目录不能相同")
            
            # 获取并过滤视频文件
            videos = self.get_videos_from_directory(input_dir)
            filtered_videos = self.filter_videos_by_duration(
                videos, min_duration, max_duration
            )
            
            # 如果没有符合条件的文件
            if not filtered_videos:
                return FileOperationResult(True, "没有符合要求的文件", 0)
            
            # 执行复制操作
            success_count = 0
            for video in filtered_videos:
                destination = f"{output_dir}\{video.filename}"
                if self.file_system_service.copy_file(video.path, destination):
                    success_count += 1
                    if progress_callback:
                        progress_callback(video, success_count)
            
            return FileOperationResult(
                True, 
                f"成功复制 {success_count} 个文件",
                success_count
            )
            
        except Exception as e:
            return FileOperationResult(False, f"发生错误: {str(e)}")
    
    def move_filtered_videos(self, 
                           input_dir: str,
                           output_dir: str,
                           min_duration: float = 0.0,
                           max_duration: float = float('inf'),
                           progress_callback=None) -> FileOperationResult:
        """
        移动符合条件的视频文件
        
        Args:
            input_dir: 输入目录
            output_dir: 输出目录
            min_duration: 最小时长
            max_duration: 最大时长
            progress_callback: 进度回调函数 (可选)
            
        Returns:
            FileOperationResult: 操作结果
        """
        try:
            # 确保输出目录存在
            if not self.file_system_service.ensure_directory_exists(output_dir):
                return FileOperationResult(False, "无法创建输出目录")
            
            # 检查目录是否相同
            if self.file_system_service.paths_are_equal(input_dir, output_dir):
                return FileOperationResult(False, "输入目录和输出目录不能相同")
            
            # 获取并过滤视频文件
            videos = self.get_videos_from_directory(input_dir)
            filtered_videos = self.filter_videos_by_duration(
                videos, min_duration, max_duration
            )
            
            # 如果没有符合条件的文件
            if not filtered_videos:
                return FileOperationResult(True, "没有符合要求的文件", 0)
            
            # 执行移动操作
            success_count = 0
            for video in filtered_videos:
                destination = f"{output_dir}\{video.filename}"
                if self.file_system_service.move_file(video.path, destination):
                    success_count += 1
                    if progress_callback:
                        progress_callback(video, success_count)
            
            return FileOperationResult(
                True, 
                f"成功移动 {success_count} 个文件",
                success_count
            )
            
        except Exception as e:
            return FileOperationResult(False, f"发生错误: {str(e)}")