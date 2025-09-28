#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import time

DEFAULT_DURATION = 56


def select_directory(title):
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory(title=title)


def get_video_duration(file_path):
    cap = cv2.VideoCapture(file_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()
    if fps > 0:
        return frame_count / fps
    return 0


def copy_mp4_files(input_dir, output_dir, duration=DEFAULT_DURATION):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(".mp4"):
                file_path = os.path.join(root, file)
                try:
                    file_duration = get_video_duration(file_path)
                    if file_duration - duration > 0:  # 允许1秒的误差
                        shutil.copy2(file_path, output_dir)
                        print(f"已复制: {file_path}")
                except Exception as e:
                    print(f"处理文件 {file_path} 时出错: {str(e)}")


class App:
    def __init__(self, master):
        self.master = master
        master.title("MP4文件拷贝工具")
        
        # 输入目录
        self.lbl_input = tk.Label(master, text="输入目录：未选择")
        self.btn_input = tk.Button(master, text="选择输入目录", command=self.select_input)
        
        # 输出目录
        self.lbl_output = tk.Label(master, text="输出目录：未选择")
        self.btn_output = tk.Button(master, text="选择输出目录", command=self.select_output)
        
        # 文件列表
        self.listbox = tk.Listbox(master, width=80, height=15)
        self.scrollbar = tk.Scrollbar(master, orient="vertical")
        
        # 时长选择
        self.lbl_duration = tk.Label(master, text="时长范围（秒）:")
        self.entry_min = tk.Entry(master, width=8)
        self.entry_max = tk.Entry(master, width=8)
        self.lbl_example = tk.Label(master, text="示例: (0,30] 或 [55,120] 或 [56,)")
        
        # 操作按钮
        self.copy_btn = tk.Button(master, text="开始拷贝", command=self.start_copy)
        self.move_btn = tk.Button(master, text="开始移动", command=self.start_move)
        self.badge = tk.Canvas(master, width=20, height=20, highlightthickness=0)
        
        # 布局
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
        
        # 初始化
        self.input_dir = ""
        self.output_dir = ""
        self.file_list = []
        self.update_badge(0)

    def update_badge(self, count):
        self.badge.delete("all")
        if count > 0:
            self.badge.create_oval(2,2,18,18, fill="red", outline="")
            self.badge.create_text(10,10, text=str(count), fill="white")

    def select_input(self):
        self.input_dir = select_directory("选择输入目录")
        if self.input_dir:
            self.lbl_input.config(text=f"输入目录：{self.input_dir}")
            self.refresh_file_list()

    def select_output(self):
        self.output_dir = select_directory("选择输出目录")
        if self.output_dir:
            self.lbl_output.config(text=f"输出目录：{self.output_dir}")

    def format_duration(self, seconds):
        return time.strftime("%H:%M:%S", time.gmtime(seconds))

    def refresh_file_list(self):
        self.listbox.delete(0, tk.END)
        self.file_list = []
        for root, _, files in os.walk(self.input_dir):
            for file in files:
                if file.lower().endswith(".mp4"):
                    path = os.path.join(root, file)
                    duration = get_video_duration(path)
                    self.file_list.append((path, duration))
                    self.listbox.insert(tk.END, f"{path} | 时长: {self.format_duration(duration)}")

    def start_copy(self):
        try:
            # 检查输入和输出目录是否为空
            if not self.input_dir:
                messagebox.showwarning("警告", "请选择输入目录")
                return
            
            if not self.output_dir:
                messagebox.showwarning("警告", "请选择输出目录")
                return
            
            # 检查输入和输出目录是否相同
            if os.path.normpath(self.input_dir) == os.path.normpath(self.output_dir):
                messagebox.showwarning("警告", "输入目录和输出目录不能相同")
                return
                
            min_val = self.entry_min.get().strip('()[]')
            max_val = self.entry_max.get().strip('()[]')
            
            min_sec = float(min_val) if min_val else 0
            max_sec = float(max_val) if max_val else float('inf')
            
            selected_files = [
                (path, duration) for path, duration in self.file_list
                if min_sec < duration <= max_sec
            ]
            
            self.update_badge(len(selected_files))
            
            if not selected_files:
                messagebox.showinfo("提示", "没有符合要求的文件")
                return
            
            for idx, (src, duration) in enumerate(selected_files):
                dst = os.path.join(self.output_dir, os.path.basename(src))
                shutil.copy2(src, dst)
                self.listbox.itemconfig(idx, bg='#e0ffe0')
                self.master.update()
                
            self.update_badge(0)
            messagebox.showinfo("完成", f"成功拷贝 {len(selected_files)} 个文件")
            
        except Exception as e:
            messagebox.showerror("错误", f"发生错误: {str(e)}")

    def start_move(self):
        try:
            # 检查输入和输出目录是否为空
            if not self.input_dir:
                messagebox.showwarning("警告", "请选择输入目录")
                return
            
            if not self.output_dir:
                messagebox.showwarning("警告", "请选择输出目录")
                return
            
            # 检查输入和输出目录是否相同
            if os.path.normpath(self.input_dir) == os.path.normpath(self.output_dir):
                messagebox.showwarning("警告", "输入目录和输出目录不能相同")
                return
                
            min_val = self.entry_min.get().strip('()[]')
            max_val = self.entry_max.get().strip('()[]')
            
            min_sec = float(min_val) if min_val else 0
            max_sec = float(max_val) if max_val else float('inf')
            
            selected_files = [
                (path, duration) for path, duration in self.file_list
                if min_sec < duration <= max_sec
            ]
            
            self.update_badge(len(selected_files))
            
            if not selected_files:
                messagebox.showinfo("提示", "没有符合要求的文件")
                return
            
            for idx, (src, duration) in enumerate(selected_files):
                dst = os.path.join(self.output_dir, os.path.basename(src))
                shutil.move(src, dst)
                self.listbox.itemconfig(idx, bg='#e0ffe0')
                self.master.update()
                
            self.update_badge(0)
            messagebox.showinfo("完成", f"成功移动 {len(selected_files)} 个文件")
            # 移动完成后刷新文件列表
            self.refresh_file_list()
            
        except Exception as e:
            messagebox.showerror("错误", f"发生错误: {str(e)}")

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()