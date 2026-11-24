from datetime import datetime

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QMessageBox,
    QSpacerItem,
    QSizePolicy,
)


class NovaDesktop(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NOVA OS")
        self.setMinimumSize(900, 600)

        self.setup_ui()
        self.start_clock()

    def setup_ui(self):

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(24, 16, 24, 18)
        main_layout.setSpacing(0)

        # TOP PANEL
        top_panel = self.create_top_panel()
        main_layout.addWidget(top_panel)

        main_layout.addSpacing(35)

        # DESKTOP CONTENT
        content_layout = QHBoxLayout()
        content_layout.setSpacing(20)

        left_content = self.create_desktop_icons()

        content_layout.addWidget(
            left_content,
            alignment=Qt.AlignmentFlag.AlignTop
        )

        content_layout.addStretch()

        main_layout.addLayout(content_layout, 1)

        # CENTER DESKTOP MESSAGE
        center_layout = QVBoxLayout()
        center_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("NOVA")
        title.setObjectName("heroTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle = QLabel("YOUR SYSTEM. YOUR UNIVERSE.")
        subtitle.setObjectName("heroSubtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        center_layout.addWidget(title)
        center_layout.addWidget(subtitle)

        main_layout.addLayout(center_layout, 2)

        # BOTTOM DOCK
        main_layout.addStretch()

        dock = self.create_dock()
        main_layout.addWidget(
            dock,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )

    def create_top_panel(self):

        panel = QFrame()
        panel.setObjectName("topPanel")
        panel.setFixedHeight(58)

        layout = QHBoxLayout(panel)
        layout.setContentsMargins(20, 0, 20, 0)
        layout.setSpacing(18)

        logo = QLabel("✦  NOVA OS")
        logo.setObjectName("logo")

        system_label = QLabel("SYSTEM ONLINE")
        system_label.setObjectName("systemStatus")

        layout.addWidget(logo)
        layout.addSpacing(15)
        layout.addWidget(system_label)

        layout.addStretch()

        cpu_label = QLabel("CPU  •  READY")
        cpu_label.setObjectName("statusLabel")

        ram_label = QLabel("MEMORY  •  READY")
        ram_label.setObjectName("statusLabel")

        self.clock_label = QLabel()
        self.clock_label.setObjectName("clockLabel")

        layout.addWidget(cpu_label)
        layout.addWidget(ram_label)
        layout.addSpacing(15)
        layout.addWidget(self.clock_label)

        return panel

    def create_desktop_icons(self):

        container = QWidget()
        layout = QVBoxLayout(container)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        applications = [
            ("▣", "My Files", "files"),
            ("⌘", "Terminal", "terminal"),
            ("▤", "Processes", "processes"),
            ("⚙", "Settings", "settings"),
        ]

        for icon, name, app_id in applications:

            button = QPushButton(f"{icon}\n{name}")
            button.setObjectName("desktopIcon")
            button.setFixedSize(105, 85)

            button.clicked.connect(
                lambda checked=False, key=app_id:
                self.open_application(key)
            )

            layout.addWidget(button)

        layout.addStretch()

        return container

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

    def start_clock(self):

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

        self.update_clock()

    def update_clock(self):

        now = datetime.now()

        self.clock_label.setText(
            now.strftime("%I:%M %p  |  %b %d, %Y")
        )

    def open_application(self, app_id):

        applications = {
            "home": "NOVA Desktop",
            "files": "File Manager",
            "terminal": "NOVA Terminal",
            "processes": "Process Manager",
            "settings": "System Settings",
        }

        application_name = applications.get(
            app_id,
            "Unknown Application"
        )

        QMessageBox.information(
            self,
            application_name,
            f"{application_name} is not available yet.\n\n"
            "This application will be developed in a future phase."
        )

    def keyPressEvent(self, event):

        if event.key() == Qt.Key.Key_Escape:
            self.showNormal()
        else:
            super().keyPressEvent(event)
