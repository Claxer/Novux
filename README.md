# Novux — Futuristic Desktop Environment

Novux is a Python-based desktop environment designed to simulate a modern, futuristic operating system experience. Built using **Python 3.14 and PySide6**, the project focuses on creating an interactive desktop interface with application windows, system monitoring, and a clean, dark-themed design.

The project is currently under active development, with its desktop interface and initial system monitoring functionality implemented.

## Implemented Features

### Desktop Environment
- **Desktop Interface** — A full-screen desktop environment with a futuristic design.
- **Top Panel** — Displays system information and a live clock.
- **Desktop Shortcuts** — Provides quick access to available applications.
- **Application Dock** — A dock for launching applications.
- **Dark Theme** — A modern dark interface with cyan and blue accents.

### Window Management
- **Multiple Application Windows** — Open and manage multiple application windows.
- **Window Movement** — Drag windows around the desktop.
- **Window Resizing** — Adjust application window dimensions.
- **Minimize and Maximize** — Control application window states.
- **Window Closing** — Close individual application windows.
- **Window Reuse** — Selecting an already-open application activates its existing window.

### System Monitor
- **CPU Usage** — Displays real-time processor usage.
- **RAM Usage** — Displays memory utilization.
- **Disk Usage** — Displays system drive utilization.
- **Hardware Information** — Shows processor details, core counts, total RAM, and system drive capacity.
- **Automatic Updates** — Refreshes system statistics every second.

## Technologies Used

- **Python 3.14** — Main programming language.
- **PySide6** — Desktop application framework.
- **Qt Style Sheets (QSS)** — Interface styling and customization.
- **psutil** — System and hardware monitoring.
- **Visual Studio Code** — Development environment.

## Project Structure

```text
Novux/
├── main.py
├── apps/
│   ├── __init__.py
│   └── system_monitor.py
├── desktop/
│   ├── __init__.py
│   └── desktop.py
├── resources/
│   └── styles.qss
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Claxer/Novux.git
```

### 2. Navigate to the Project Directory

```bash
cd Novux
```

### 3. Create a Virtual Environment

```bash
py -3.14 -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Novux

```bash
python main.py
```

## Development Progress

| Component | Status |
|---|---|
| Project Setup | Completed |
| Virtual Environment | Completed |
| PySide6 Configuration | Completed |
| Desktop Interface | Completed |
| Dark Theme and Styling | Completed |
| Top Panel and Live Clock | Completed |
| Desktop Shortcuts | Completed |
| Application Dock | Completed |
| Window Management | Completed |
| System Monitor | Implemented and Tested |

## Project Status

Novux is currently in active development. The initial desktop environment, application window management, and System Monitor have been implemented and tested.

Future development will focus on expanding the desktop environment with additional built-in applications and system utilities.

## License

This project is currently under development. License details will be added in a future update.
