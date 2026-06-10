> [🇨🇳 中文说明](README.zh.md)

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
