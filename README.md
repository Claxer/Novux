# Novux — Futuristic Desktop Environment

Novux is a Python-based desktop environment inspired by Linux operating systems. Designed with a futuristic aesthetic, it aims to provide a custom desktop experience with its own interface, application navigation, system utilities, and desktop management features.

Built using **Python 3.14 and PySide6**, Novux is designed to evolve into a customizable desktop environment that simulates essential operating system functionality while running as a desktop application on Windows.

The project is currently under active development, with its initial desktop interface successfully implemented.

## Current Features

### Desktop Environment
- Full-screen desktop interface
- Custom Novux branding
- Futuristic dark-themed design
- Desktop shortcuts
- Interactive application buttons

### System Panel
- Custom top navigation panel
- System status indicators
- Live clock and date display
- Novux system branding

### Application Dock
- Floating bottom application dock
- Application shortcut buttons
- Hover effects and tooltips
- Application launch placeholders

### Interface and Styling
- Custom Qt Stylesheets (QSS)
- Dark charcoal and navy color palette
- Neon cyan accents
- Rounded interface components
- Consistent desktop styling

## Planned Features

The following features are planned for future development:

- **Window Management** — Draggable, resizable, minimizable, and maximizable application windows.
- **Application Management** — Launch and manage multiple applications simultaneously.
- **System Dashboard** — CPU, RAM, storage, and hardware monitoring.
- **Process Manager** — View, search, sort, and manage running processes.
- **File Manager** — Browse, organize, move, rename, and delete files.
- **Novux Terminal** — Custom terminal interface with system and file commands.
- **System Settings** — Desktop customization, appearance, and preferences.
- **Notification Center** — System alerts and application notifications.
- **Taskbar Integration** — Display and switch between open applications.

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
| Window management | Planned |
| System monitoring | Planned |
| Process management | Planned |
| File manager | Planned |
| Custom terminal | Planned |

## Project Status

**Currently in development.**

Novux is being developed incrementally, with each component implemented and tested before moving on to the next stage.

The next development milestone focuses on building the window management system, allowing multiple applications to open, move, minimize, maximize, and close within the Novux desktop environment.

## License

This project is currently under development. Licensing information will be added in a future update.
