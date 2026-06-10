<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="v1.0"/>
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT"/>
  <img src="https://img.shields.io/badge/python-3.x-orange" alt="Python 3.x"/>
  <img src="https://img.shields.io/github/stars/huajielong/mp4-copy-tool?style=social" alt="Stars"/>
  <img src="https://img.shields.io/badge/Architecture-Clean%20Code-important" alt="Clean Architecture"/>
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey" alt="Cross-platform"/>
</p>

<h1 align="center">📁 MP4 Copy Tool</h1>
<p align="center"><b>Smart MP4 file copier — filter by duration with precision, copy or move, Clean Architecture, GUI operation</b></p>
<p align="center">
  ⏱️ Duration Filter · 📂 Recursive Scan · 🔄 Copy/Move · 🖥️ GUI
</p>

<p align="center">
  <a href="#-quick-start">🚀 Quick Start</a> •
  <a href="#-core-features">⚡ Core Features</a> •
  <a href="#-clean-architecture">🏗️ Clean Architecture</a> •
  <a href="#-faq">❓ FAQ</a>
</p>

---

## 🤔 Need to Pick Out Videos by Duration from a Huge Collection?

Manually filtering files by duration from a large pool of videos is tedious and error-prone:

| Problem You May Face | MP4 Copy Tool Solution |
|:---------------------|:-----------------------|
| ❓ Thousands of MP4 files, need only those 30-60 seconds long | ✅ **Precise duration filter** — custom min/max duration, second-level precision |
| ❓ Need to copy or move filtered files to a target directory | ✅ **Copy & Move modes** — switch freely as needed |
| ❓ Too many subdirectories, manual navigation is slow | ✅ **Recursive scan** — automatically searches all subdirectories for MP4s |
| ❓ Command-line tools are complex, colleagues struggle | ✅ **Graphical UI** — visual file list, what-you-see-is-what-you-get |
| ❓ Hard to maintain and extend the codebase | ✅ **Clean Architecture** — separation of concerns, easy to extend and test |

### 🔥 Use Cases

> **Video素材整理** → **Batch Short Video Filtering** → **Surveillance Video Archiving** → **Media File Management**

---

## 🚀 Quick Start

### Prerequisites

| Dependency | Version |
|:-----------|:-------:|
| Python | 3.x |
| Packages | See `requirements.txt` |

### Installation & Run

```bash
# Clone the repository
git clone https://github.com/huajielong/mp4-copy-tool.git
cd mp4-copy-tool

# Install dependencies
pip install -r requirements.txt

# Run
python cpymp4.py
```

You can also run the prebuilt `dist/MP4CopyTool.exe` (Windows, no installation required).

---

## ⚡ Core Features

| Feature | Description |
|:--------|:------------|
| ⏱️ **Precise Duration Filter** | Custom min/max duration with left-open right-closed interval logic |
| 📂 **Recursive Directory Scan** | Automatically discovers MP4 files in all subdirectories |
| 🔄 **Copy & Move Modes** | Copy or move files that match the criteria |
| 🖥️ **Visual File List** | Real-time display of file durations and filter results |
| 📊 **Real-time Counter** | Dynamic update of matching file count |
| 🔍 **File Highlighting** | Highlights the currently processing file during operation |
| ✅ **Directory Validation** | Automatically checks input/output directory validity |

---

## 🏗️ Clean Architecture

The project follows **Clean Architecture** principles, achieving separation of concerns and dependency inversion:

```
┌─────────────────────────────────────────────────────────────┐
│                   Frameworks Layer                           │
│   GUI Application · Entry Point · Dependency Injection      │
├─────────────────────────────────────────────────────────────┤
│                   Interface Adapters Layer                   │
│   File System Adapter · Video Repository Adapter · GUI      │
├─────────────────────────────────────────────────────────────┤
│                   Use Case Layer                             │
│   Video File Processing · Business Logic Orchestration      │
├─────────────────────────────────────────────────────────────┤
│                   Core Layer                                 │
│   Business Entities · Abstract Interfaces · Domain Rules    │
└─────────────────────────────────────────────────────────────┘
```

| Layer | Responsibility | Replaceable |
|:------|:---------------|:-----------:|
| 🏛️ **Core** | Business entities, abstract interface definitions | — |
| ⚙️ **Use Cases** | Business process orchestration | ✅ |
| 🔌 **Interface Adapters** | External system adaptation | ✅ |
| 🖥️ **Frameworks** | UI framework, dependency injection | ✅ |

---

## 📁 Project Structure

```
mp4-copy-tool/
├── src/
│   ├── core/                # Core Layer
│   │   ├── entities.py      # Business entities (VideoFile, FilterCriteria)
│   │   └── ports.py         # Abstract interface definitions
│   ├── use_cases/           # Use Case Layer
│   │   └── video_file_processor.py  # Video file processing use case
│   ├── interfaces/          # Interface Adapters Layer
│   │   ├── file_system_adapter.py
│   │   ├── video_repository_adapter.py
│   │   └── gui_adapter.py
│   └── frameworks/          # Frameworks Layer
│       ├── gui_app.py       # GUI implementation
│       └── main.py          # Program entry point
├── cpymp4.py                # Quick-start script
├── images/                  # Screenshots
├── dist/                    # Prebuilt executable
├── requirements.txt         # Python dependencies
└── README.md                # 💡 You are here
```

---

## ❓ FAQ

<details>
<summary><b>How does the duration filter work?</b></summary>
It uses a left-open right-closed interval: e.g., (55,120] means videos with duration > 55s and ≤ 120s. Semi-infinite intervals are supported, e.g., [56,) means videos with duration ≥ 56s. Both min and max inputs can be left empty.
</details>

<details>
<summary><b>What's the difference between Copy and Move modes?</b></summary>
Copy mode: copies matching files to the output directory, source files are preserved.<br>
Move mode: moves matching files to the output directory, source files are deleted. Use move mode with caution.
</details>

<details>
<summary><b>Do I need to install FFmpeg?</b></summary>
No. This tool uses Python standard library and lightweight dependencies to read video duration — no FFmpeg installation required.
</details>

<details>
<summary><b>Can I package it as an exe for others?</b></summary>
Yes. Use PyInstaller: <code>pyinstaller MP4CopyTool.spec</code>, or use the prebuilt exe in the dist/ directory.
</details>

---

## 🤝 Contributing

Contributions of all forms are welcome — submit an Issue, Pull Request, or improve the documentation.

<a href="https://github.com/huajielong/mp4-copy-tool/graphs/contributors">
  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen" alt="Contributions Welcome"/>
</a>

## 📄 License

MIT © [huajielong](https://github.com/huajielong)

---

<p align="center">
  ⭐ If this tool helps you, please give it a Star!
</p>

---

<h1 align="center">📁 MP4 Copy Tool — MP4文件智能拷贝工具</h1>
<p align="center"><b>按时长精确筛选并复制/移动MP4文件，Clean Architecture设计，图形界面操作</b></p>
<p align="center">
  ⏱️ 时长筛选 · 📂 递归扫描 · 🔄 复制/移动 · 🖥️ 图形界面
</p>

<p align="center">
  <a href="#-快速开始">🚀 快速开始</a> •
  <a href="#-核心功能">⚡ 核心功能</a> •
  <a href="#-清洁架构">🏗️ 清洁架构</a> •
  <a href="#-常见问题">❓ 常见问题</a>
</p>

---

## 🤔 从海量视频中按时长挑出需要的文件？

混在大量视频中按时长筛选特定文件，手动操作费时又容易出错：

| 你可能遇到的问题 | MP4 Copy Tool 帮你解决 |
|:-----------------|:----------------------|
| ❓ 几千个 MP4 文件要找时长 30-60 秒的 | ✅ **精准时长过滤** — 支持自定义最小/最大时长，秒级筛选 |
| ❓ 筛选后要复制/移动到指定目录 | ✅ **复制/移动双模式** — 根据需要自由切换 |
| ❓ 子目录太多，手动翻找效率低 | ✅ **递归扫描** — 自动搜索所有子目录中的 MP4 |
| ❓ 命令行操作复杂，同事不会用 | ✅ **图形界面** — 可视化文件列表，所见即所得 |
| ❓ 代码维护困难，想加功能无从下手 | ✅ **清洁架构** — 关注点分离，易扩展、易测试 |

### 🔥 适用场景

> **视频素材整理** → **短视频批量筛选** → **监控视频归档** → **媒体文件管理**

---

## 🚀 快速开始

### 环境要求

| 依赖 | 版本 |
|:-----|:----:|
| Python | 3.x |
| 依赖包 | 见 `requirements.txt` |

### 安装与运行

```bash
# 克隆项目
git clone https://github.com/huajielong/mp4-copy-tool.git
cd mp4-copy-tool

# 安装依赖
pip install -r requirements.txt

# 运行
python cpymp4.py
```

也可以直接运行 `dist/MP4CopyTool.exe`（Windows 免安装版）。

---

## ⚡ 核心功能

| 功能 | 说明 |
|:-----|:------|
| ⏱️ **时长精确过滤** | 支持最小/最大时长设置，左开右闭区间规则 |
| 📂 **递归目录扫描** | 自动搜索所有子目录中的 MP4 文件 |
| 🔄 **复制/移动双模式** | 满足条件可复制或移动文件 |
| 🖥️ **可视化文件列表** | 实时显示文件时长和筛选结果 |
| 📊 **实时计数** | 符合条件文件数量动态更新 |
| 🔍 **文件高亮** | 操作过程中高亮显示当前处理文件 |
| ✅ **目录容错** | 自动检查输入/输出目录有效性 |

---

## 🏗️ 清洁架构

项目采用 **Clean Architecture（清洁架构）** 设计，实现关注点分离和依赖倒置：

```
┌─────────────────────────────────────────────────────────────┐
│                   框架层 (Frameworks)                         │
│  GUI 应用 · 程序入口 · 依赖注入                              │
├─────────────────────────────────────────────────────────────┤
│                   接口适配器层 (Interfaces)                   │
│  文件系统适配器 · 视频仓库适配器 · GUI 适配器               │
├─────────────────────────────────────────────────────────────┤
│                   用例层 (Use Cases)                          │
│  视频文件处理 · 业务逻辑编排                                │
├─────────────────────────────────────────────────────────────┤
│                   核心层 (Core)                               │
│  业务实体 · 抽象接口 · 领域规则                             │
└─────────────────────────────────────────────────────────────┘
```

| 层 | 职责 | 可替换 |
|:---|:------|:------:|
| 🏛️ **核心层** | 业务实体、抽象接口定义 | — |
| ⚙️ **用例层** | 业务流程编排 | ✅ |
| 🔌 **接口适配器** | 外部系统适配 | ✅ |
| 🖥️ **框架层** | UI 框架、依赖注入 | ✅ |

---

## 📁 项目结构

```
mp4-copy-tool/
├── src/
│   ├── core/                # 核心层
│   │   ├── entities.py      # 业务实体（VideoFile, FilterCriteria）
│   │   └── ports.py         # 抽象接口定义
│   ├── use_cases/           # 用例层
│   │   └── video_file_processor.py  # 视频文件处理用例
│   ├── interfaces/          # 接口适配器层
│   │   ├── file_system_adapter.py
│   │   ├── video_repository_adapter.py
│   │   └── gui_adapter.py
│   └── frameworks/          # 框架层
│       ├── gui_app.py       # GUI 实现
│       └── main.py          # 程序入口
├── cpymp4.py                # 快捷启动脚本
├── images/                  # 界面截图
├── dist/                    # 打包好的 exe
├── requirements.txt         # Python 依赖
└── README.md                # 💡 你在这里
```

---

## ❓ 常见问题

<details>
<summary><b>时长过滤规则是什么样的？</b></summary>
采用左开右闭区间：如 (55,120] 表示时长 > 55 秒且 ≤ 120 秒的视频。支持半无限区间，如 [56,) 表示时长 ≥ 56 秒的视频。最小值和最大值输入框均可留空。
</details>

<details>
<summary><b>复制和移动模式有什么区别？</b></summary>
复制模式：将符合条件的文件复制到输出目录，源文件保留。<br>
移动模式：将符合条件的文件移动到输出目录，源文件被删除。请谨慎使用移动模式。
</details>

<details>
<summary><b>需要安装 FFmpeg 吗？</b></summary>
不需要。本工具使用 Python 标准库和轻量级依赖获取视频时长，无需额外安装 FFmpeg。
</details>

<details>
<summary><b>可以打包成 exe 给其他人用吗？</b></summary>
可以。使用 PyInstaller 打包：<code>pyinstaller MP4CopyTool.spec</code>，或直接使用 dist/ 目录下的现成 exe。
</details>

---

## 🤝 贡献

欢迎任何形式的贡献——提交 Issue、Pull Request 或改进文档。

<a href="https://github.com/huajielong/mp4-copy-tool/graphs/contributors">
  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen" alt="Contributions Welcome"/>
</a>

## 📄 许可证

MIT © [huajielong](https://github.com/huajielong)

---

<p align="center">
  ⭐ 如果这个工具对你有帮助，请点个 Star 支持一下！
</p>
