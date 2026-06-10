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
