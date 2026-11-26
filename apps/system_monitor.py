import platform
import os

import psutil

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QProgressBar,
)


class SystemMonitor(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName("systemMonitor")
        self.setMinimumSize(550, 400)

        self.setup_ui()
        self.start_monitoring()

    # ==========================================
    # MAIN INTERFACE
    # ==========================================

    def setup_ui(self):

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(20)

        # HEADER
        title = QLabel("System Monitor")
        title.setObjectName("monitorTitle")

        subtitle = QLabel(
            "Real-time hardware performance and system information"
        )
        subtitle.setObjectName("monitorSubtitle")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # RESOURCE CARDS
        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(15)

        self.cpu_card, self.cpu_value, self.cpu_bar = (
            self.create_resource_card("CPU USAGE")
        )

        self.ram_card, self.ram_value, self.ram_bar = (
            self.create_resource_card("MEMORY USAGE")
        )

        self.disk_card, self.disk_value, self.disk_bar = (
            self.create_resource_card("DISK USAGE")
        )

        cards_layout.addWidget(self.cpu_card)
        cards_layout.addWidget(self.ram_card)
        cards_layout.addWidget(self.disk_card)

        main_layout.addLayout(cards_layout)

        # SYSTEM INFORMATION
        info_panel = QFrame()
        info_panel.setObjectName("monitorInfoPanel")

        info_layout = QVBoxLayout(info_panel)
        info_layout.setContentsMargins(20, 20, 20, 20)
        info_layout.setSpacing(14)

        info_title = QLabel("SYSTEM INFORMATION")
        info_title.setObjectName("monitorSectionTitle")

        info_layout.addWidget(info_title)

        self.os_label = QLabel()
        self.processor_label = QLabel()
        self.cpu_cores_label = QLabel()
        self.ram_total_label = QLabel()
        self.disk_total_label = QLabel()

        for label in (
            self.os_label,
            self.processor_label,
            self.cpu_cores_label,
            self.ram_total_label,
            self.disk_total_label,
        ):
            label.setObjectName("monitorInfoLabel")
            label.setWordWrap(True)
            info_layout.addWidget(label)

        main_layout.addWidget(info_panel)
        main_layout.addStretch()

        self.update_system_information()

    # ==========================================
    # RESOURCE CARD
    # ==========================================

    def create_resource_card(self, title_text):

        card = QFrame()
        card.setObjectName("monitorCard")

        layout = QVBoxLayout(card)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(12)

        title = QLabel(title_text)
        title.setObjectName("monitorCardTitle")

        value = QLabel("0%")
        value.setObjectName("monitorCardValue")

        bar = QProgressBar()
        bar.setObjectName("monitorProgress")
        bar.setRange(0, 100)
        bar.setValue(0)
        bar.setTextVisible(False)
        bar.setFixedHeight(9)

        layout.addWidget(title)
        layout.addWidget(value)
        layout.addWidget(bar)
        layout.addStretch()

        return card, value, bar

    # ==========================================
    # SYSTEM INFORMATION
    # ==========================================

    def update_system_information(self):

        memory = psutil.virtual_memory()

        disk_path = os.environ.get("SystemDrive", "C:") + "\\"

        try:
            disk = psutil.disk_usage(disk_path)
            disk_total = self.format_bytes(disk.total)
        except OSError:
            disk_total = "Unavailable"

        processor = platform.processor() or "Unknown"

        self.os_label.setText(
            f"Operating System: {platform.system()} "
            f"{platform.release()}"
        )

        self.processor_label.setText(
            f"Processor: {processor}"
        )

        self.cpu_cores_label.setText(
            f"CPU Cores: {psutil.cpu_count(logical=False) or 'Unknown'} "
            f"physical / {psutil.cpu_count(logical=True) or 'Unknown'} logical"
        )

        self.ram_total_label.setText(
            f"Installed Memory: {self.format_bytes(memory.total)}"
        )

        self.disk_total_label.setText(
            f"System Drive Capacity: {disk_total}"
        )

    # ==========================================
    # LIVE MONITORING
    # ==========================================

    def start_monitoring(self):

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_statistics)
        self.timer.start(1000)

        # Initialize CPU measurement.
        psutil.cpu_percent(interval=None)

        self.update_statistics()

    def update_statistics(self):

        # CPU
        cpu = psutil.cpu_percent(interval=None)

        self.cpu_value.setText(f"{cpu:.1f}%")
        self.cpu_bar.setValue(round(cpu))

        # MEMORY
        memory = psutil.virtual_memory()

        self.ram_value.setText(
            f"{memory.percent:.1f}%"
        )
        self.ram_bar.setValue(round(memory.percent))

        # DISK
        disk_path = os.environ.get("SystemDrive", "C:") + "\\"

        try:
            disk = psutil.disk_usage(disk_path)

            self.disk_value.setText(
                f"{disk.percent:.1f}%"
            )

            self.disk_bar.setValue(
                round(disk.percent)
            )

        except OSError:
            self.disk_value.setText("N/A")
            self.disk_bar.setValue(0)

    # ==========================================
    # UTILITIES
    # ==========================================

    @staticmethod
    def format_bytes(value):

        for unit in ("B", "KB", "MB", "GB", "TB"):
            if value < 1024:
                return f"{value:.2f} {unit}"

            value /= 1024

        return f"{value:.2f} PB"
