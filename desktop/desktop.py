from datetime import datetime

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QMdiArea,
    QMdiSubWindow,
)

from apps.system_monitor import SystemMonitor
from apps.process_manager import ProcessManager
from apps.file_manager import FileManager


class NovuxDesktop(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Novux")
        self.setObjectName("novuxDesktop")
        self.setMinimumSize(900, 600)

        self.setup_ui()
        self.start_clock()

    # ==========================================
    # MAIN DESKTOP
    # ==========================================

    def setup_ui(self):

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(24, 16, 24, 18)
        main_layout.setSpacing(14)

        main_layout.addWidget(self.create_top_panel())

        workspace_layout = QHBoxLayout()
        workspace_layout.setSpacing(15)

        workspace_layout.addWidget(
            self.create_desktop_icons()
        )

        self.workspace = QMdiArea()
        self.workspace.setObjectName("workspace")

        self.workspace.setViewMode(
            QMdiArea.ViewMode.SubWindowView
        )

        self.workspace.setBackground(
            QColor("#0B1020")
        )

        self.workspace.setOption(
            QMdiArea.AreaOption.DontMaximizeSubWindowOnActivation,
            True
        )

        workspace_layout.addWidget(
            self.workspace,
            1
        )

        main_layout.addLayout(
            workspace_layout,
            1
        )

        main_layout.addWidget(
            self.create_dock(),
            alignment=Qt.AlignmentFlag.AlignHCenter
        )

    # ==========================================
    # TOP SYSTEM PANEL
    # ==========================================

    def create_top_panel(self):

        panel = QFrame()
        panel.setObjectName("topPanel")
        panel.setFixedHeight(58)

        layout = QHBoxLayout(panel)
        layout.setContentsMargins(20, 0, 20, 0)
        layout.setSpacing(18)

        logo = QLabel("✦  NOVUX")
        logo.setObjectName("logo")

        system_label = QLabel("SYSTEM ONLINE")
        system_label.setObjectName("systemStatus")

        layout.addWidget(logo)
        layout.addSpacing(15)
        layout.addWidget(system_label)

        layout.addStretch()

        cpu_label = QLabel("CPU  •  MONITORING")
        cpu_label.setObjectName("statusLabel")

        ram_label = QLabel("MEMORY  •  MONITORING")
        ram_label.setObjectName("statusLabel")

        self.clock_label = QLabel()
        self.clock_label.setObjectName("clockLabel")

        layout.addWidget(cpu_label)
        layout.addWidget(ram_label)
        layout.addSpacing(15)
        layout.addWidget(self.clock_label)

        return panel

    # ==========================================
    # DESKTOP SHORTCUTS
    # ==========================================

    def create_desktop_icons(self):

        container = QWidget()
        container.setObjectName("desktopIcons")
        container.setFixedWidth(105)

        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 10, 0, 10)
        layout.setSpacing(16)

        applications = [
            ("▣", "My Files", "files"),
            ("⌘", "Terminal", "terminal"),
            ("▤", "Processes", "processes"),
            ("◉", "System Monitor", "monitor"),
            ("⚙", "Settings", "settings"),
        ]

        for icon, name, app_id in applications:

            button = QPushButton(f"{icon}\n{name}")
            button.setObjectName("desktopIcon")
            button.setFixedSize(100, 78)

            button.clicked.connect(
                lambda checked=False, key=app_id:
                self.open_application(key)
            )

            layout.addWidget(button)

        layout.addStretch()

        return container

    # ==========================================
    # APPLICATION DOCK
    # ==========================================

    def create_dock(self):

        dock = QFrame()
        dock.setObjectName("dock")
        dock.setFixedHeight(82)

        layout = QHBoxLayout(dock)
        layout.setContentsMargins(15, 10, 15, 10)
        layout.setSpacing(12)

        applications = [
            ("⌂", "Home", "home"),
            ("▣", "Files", "files"),
            ("⌘", "Terminal", "terminal"),
            ("▤", "Processes", "processes"),
            ("◉", "Monitor", "monitor"),
            ("⚙", "Settings", "settings"),
        ]

        for icon, name, app_id in applications:

            button = QPushButton(icon)
            button.setObjectName("dockButton")
            button.setToolTip(name)
            button.setFixedSize(54, 54)

            button.clicked.connect(
                lambda checked=False, key=app_id:
                self.open_application(key)
            )

            layout.addWidget(button)

        return dock

    # ==========================================
    # APPLICATION WINDOW CONTENT
    # ==========================================

    def create_application_content(self, app_id):

        applications = {
            "home": {
                "title": "Novux Dashboard",
                "description": "Welcome to your Novux desktop environment.",
                "features": [
                    "Desktop Environment",
                    "Application Management",
                    "System Utilities",
                    "Personalized Workspace",
                ],
            },

            "terminal": {
                "title": "Novux Terminal",
                "description": "Your command-line environment.",
                "features": [
                    "Custom Commands",
                    "Directory Navigation",
                    "System Information",
                    "Command Execution",
                ],
            },

            "settings": {
                "title": "System Settings",
                "description": "Configure your Novux environment.",
                "features": [
                    "Appearance Settings",
                    "Desktop Preferences",
                    "System Configuration",
                    "User Preferences",
                ],
            },
        }

        data = applications.get(app_id)

        if data is None:
            return QWidget()

        content = QWidget()
        content.setObjectName("appWindowContent")

        layout = QVBoxLayout(content)
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(15)

        title = QLabel(data["title"])
        title.setObjectName("appTitle")

        description = QLabel(data["description"])
        description.setObjectName("appDescription")
        description.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(description)

        separator = QFrame()
        separator.setObjectName("appSeparator")
        separator.setFixedHeight(1)

        layout.addWidget(separator)

        features_title = QLabel("AVAILABLE MODULES")
        features_title.setObjectName("sectionTitle")

        layout.addWidget(features_title)

        for feature in data["features"]:

            feature_label = QLabel(f"  •  {feature}")
            feature_label.setObjectName("featureLabel")

            layout.addWidget(feature_label)

        layout.addStretch()

        status = QLabel("NOVUX  /  MODULE INITIALIZED")
        status.setObjectName("appStatus")

        layout.addWidget(status)

        return content

    # ==========================================
    # WINDOW MANAGEMENT
    # ==========================================

    def open_application(self, app_id):

        for window in self.workspace.subWindowList():

            if window.property("app_id") == app_id:

                if window.isMinimized():
                    window.showNormal()

                window.show()
                window.raise_()
                window.activateWindow()

                self.workspace.setActiveSubWindow(window)

                return

        applications = {
            "home": "Novux Dashboard",
            "files": "File Manager",
            "terminal": "Novux Terminal",
            "processes": "Process Manager",
            "monitor": "System Monitor",
            "settings": "System Settings",
        }

        title = applications.get(app_id)

        if title is None:
            return

        window = QMdiSubWindow()

        window.setObjectName("applicationWindow")
        window.setProperty("app_id", app_id)
        window.setWindowTitle(title)

        # Load the selected application
        if app_id == "files":
            content = FileManager()

        elif app_id == "processes":
            content = ProcessManager()

        elif app_id == "monitor":
            content = SystemMonitor()

        else:
            content = self.create_application_content(app_id)

        window.setWidget(content)

        # Application window dimensions
        if app_id in ("files", "processes", "monitor"):
            window.setMinimumSize(750, 480)
            window.resize(950, 650)

        else:
            window.setMinimumSize(360, 260)
            window.resize(520, 380)

        window.setAttribute(
            Qt.WidgetAttribute.WA_DeleteOnClose,
            True
        )

        self.workspace.addSubWindow(window)

        open_count = len(self.workspace.subWindowList())
        offset = (open_count - 1) * 30

        window.move(
            35 + offset,
            35 + offset
        )

        window.show()
        window.raise_()
        window.activateWindow()

        self.workspace.setActiveSubWindow(window)

    # ==========================================
    # LIVE CLOCK
    # ==========================================

    def start_clock(self):

        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.update_clock
        )

        self.timer.start(1000)

        self.update_clock()

    def update_clock(self):

        now = datetime.now()

        self.clock_label.setText(
            now.strftime("%I:%M %p  |  %b %d, %Y")
        )
