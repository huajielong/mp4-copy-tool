"""
视频仓库适配器

实现 VideoFileRepository 接口，提供视频文件的查找和时长获取功能。
"""

import os
import cv2
from typing import List
from src.core.entities import VideoFile
from src.core.ports import VideoFileRepository


class OpenCVVideoRepositoryAdapter(VideoFileRepository):
    """
    OpenCV 视频仓库适配器
    
    使用 OpenCV 库实现视频文件的查找和时长获取。
    """
    
    def get_video_duration(self, file_path: str) -> float:
        """
        获取视频文件的时长
        
        Args:
            file_path: 视频文件路径
            
        Returns:
            float: 视频时长（秒），失败返回0
        """
        try:
            # 创建视频捕获对象
            cap = cv2.VideoCapture(file_path)
            
            # 获取视频帧率
            fps = cap.get(cv2.CAP_PROP_FPS)
            
            # 获取视频总帧数
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            # 释放视频捕获对象
            cap.release()
            
            # 计算并返回时长（秒）
            if fps > 0 and frame_count > 0:
                return frame_count / fps
            return 0.0
            
        except Exception:
            return 0.0
    
    def find_mp4_files(self, directory: str) -> List[VideoFile]:
        """
        查找目录中的所有MP4文件
        
        Args:
            directory: 要搜索的目录
            
        Returns:
            List[VideoFile]: 找到的视频文件列表
        """
        video_files = []
        
        try:
            # 递归遍历目录
            for root, _, files in os.walk(directory):
                for file in files:
                    # 检查是否为MP4文件
                    if file.lower().endswith('.mp4'):
                        file_path = os.path.join(root, file)
                        # 获取视频时长
                        duration = self.get_video_duration(file_path)
                        # 创建视频文件实体
                        video_file = VideoFile(
                            path=file_path,
                            duration=duration,
                            filename=file
                        )
                        video_files.append(video_file)
        except Exception:
            # 如果发生错误，返回已收集的文件列表
            pass
        
        return video_files