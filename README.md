# Novux — Futuristic Desktop Environment

Novux is a Python-based desktop environment inspired by Linux operating systems. Designed with a futuristic aesthetic, it aims to provide a custom desktop experience with its own interface, application navigation, system utilities, and desktop management features.

Built using **Python 3.14, PySide6, and psutil**, Novux is designed to evolve into a customizable desktop environment that simulates essential operating system functionality while running as a desktop application on Windows.

The project is currently under active development, with its desktop interface, application window management, and real-time system monitoring implemented.

## Current Features

### Desktop Environment
- Full-screen desktop interface
- Custom Novux branding
- Futuristic dark-themed design
- Interactive desktop shortcuts
- Desktop workspace for application windows

### System Panel
- Custom top system panel
- System status indicators
- Live clock and date display
- Novux system branding

### Application Dock
- Floating bottom application dock
- Application shortcut buttons
- Hover effects and tooltips
- Quick access to desktop applications

### Window Management
- Internal application windows using Qt MDI
- Multiple applications can remain open simultaneously
- Draggable and resizable application windows
- Minimize, maximize, and close controls
- Automatic window activation when selecting an already-open application
- Separate application windows within the Novux desktop workspace

### System Monitor
- Real-time CPU usage monitoring
- RAM usage and utilization percentage
- Disk usage monitoring
- Visual resource progress bars
- Operating system information
- Processor information
- Physical and logical CPU core counts
- Installed memory information
- System drive capacity
- Automatic statistics refresh every second

### Process Manager
- Initial process management module
- Running process information using psutil
- Process identification through PID
- CPU and memory usage reporting
- Process search by name or PID
- Manual and automatic process list refresh
- Process termination with confirmation
- Basic protection against termination of selected critical processes

*The Process Manager is under development and requires further integration testing.*

### Interface and Styling
- Custom Qt Stylesheets (QSS)
- Dark charcoal and navy color palette
- Neon cyan accents
- Rounded interface components
- Consistent desktop and application styling
- Custom styling for System Monitor and Process Manager interfaces

## Planned Features

The following features are planned for future development and expansion:

- **Advanced Process Manager** — Improved process sorting, resource reporting, and safer process management.
- **File Manager** — Browse, organize, move, rename, and delete files.
- **Novux Terminal** — Custom terminal interface with system and file commands.
- **System Settings** — Desktop customization, appearance, and preferences.
- **Notification Center** — System alerts and application notifications.
- **Taskbar Integration** — Display and switch between open applications.
- **System Dashboard** — A centralized overview of system resources and desktop activity.
- **Persistent Settings** — Store user preferences and application configurations.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.14 | Main programming language |
| PySide6 | Desktop GUI framework |
| Qt Stylesheets (QSS) | Interface styling |
| psutil | System monitoring and process management |
| SQLite | Planned persistent data storage |
| Visual Studio Code | Development environment |

## Project Structure

```text
Novux/
│
├── main.py
│
├── apps/
│   ├── __init__.py
│   ├── system_monitor.py
│   └── process_manager.py
│
├── desktop/
│   ├── __init__.py
│   └── desktop.py
│
├── resources/
│   └── styles.qss
│
├── requirements.txt
│
└── README.md
```

*The `.venv` directory is created locally and should not be committed to the repository.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Claxer/Novux.git
```

### 2. Navigate to the Project

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
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Run Novux

```bash
python main.py
```

## Development Progress

| Component | Status |
|---|---|
| Project setup | Completed |
| Python virtual environment | Completed |
| PySide6 integration | Completed |
| Initial desktop interface | Completed |
| Futuristic styling | Completed |
| Top system panel | Completed |
| Live clock and date | Completed |
| Desktop shortcuts | Completed |
| Application dock | Completed |
| Window management | Completed |
| System Monitor | Implemented and tested |
| Process Manager | Implemented; integration testing pending |
| File Manager | Planned |
| Custom terminal | Planned |
| System Settings | Planned |
| Notification Center | Planned |

## Project Status

**Currently in active development.**

Novux is being developed incrementally, with each component implemented and tested before moving on to the next stage.

The current development focus is expanding the Process Manager, improving application functionality, and developing additional desktop utilities while maintaining the existing Novux interface and window management system.

## License

This project is currently under development. Licensing information will be added in a future update.
