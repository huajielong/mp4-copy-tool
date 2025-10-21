#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MP4文件拷贝工具

功能：从指定目录提取特定时长的MP4文件，并支持复制或移动到目标目录
支持：自定义时长过滤、可视化文件列表、实时进度显示
作者：
日期：

注意：此文件是重构后的入口文件，实际逻辑在src目录下实现。
"""

from src.frameworks.main import main


if __name__ == "__main__":
    main()