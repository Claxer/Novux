# Novux — Futuristic Desktop Environment

Novux is a Python-based desktop environment designed to simulate a modern, futuristic operating system experience. Built using **Python 3.14 and PySide6**, the project focuses on creating an interactive desktop interface with application windows, system monitoring, process management, file browsing, and a clean, dark-themed design.

The project is currently under active development, with its desktop interface, application window management, System Monitor, Process Manager, and File Manager implemented.

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

### Process Manager
- **Running Process List** — Displays currently running system processes.
- **Process Information** — Shows process IDs (PID), names, CPU usage, and memory consumption.
- **Process Search** — Search for processes using their names or PIDs.
- **Manual Refresh** — Refresh the process list when needed.
- **Automatic Refresh** — Updates the process list periodically.
- **End Process** — Allows users to terminate selected processes with a confirmation prompt.
- **Process Protection** — Includes basic safeguards for selected protected processes.

### File Manager
- **File and Folder Browser** — Displays files and folders from the local file system.
- **Directory Navigation** — Browse through folders and directories.
- **Back and Forward Navigation** — Move between previously visited locations.
- **Parent Directory Navigation** — Navigate to the parent folder.
- **Path Input** — Enter a directory path to navigate directly to a location.
- **File Opening** — Open files using their default Windows applications.
- **Manual Refresh** — Refresh the displayed file and folder list.
- **File System View** — Uses a tree-based interface to organize and display files and folders.

## Technologies Used

- **Python 3.14** — Main programming language.
- **PySide6** — Desktop application framework.
- **Qt Style Sheets (QSS)** — Interface styling and customization.
- **psutil** — System monitoring and process management.
- **Visual Studio Code** — Development environment.

## Project Structure

```text
Novux/
├── main.py
├── apps/
│   ├── __init__.py
│   ├── system_monitor.py
│   ├── process_manager.py
│   └── file_manager.py
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
| Process Manager | Implemented |
| File Manager | Implemented |

## Project Status

Novux is currently in active development. The desktop environment, application window management, System Monitor, Process Manager, and File Manager have been implemented.

Future development will focus on expanding the desktop environment with additional built-in applications and system utilities, improving existing functionality, and introducing more advanced desktop features.

## License

This project is currently under development. License details will be added in a future update.
