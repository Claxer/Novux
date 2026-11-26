import psutil

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QMessageBox,
    QFrame,
)


class ProcessManager(QWidget):

    PROTECTED_PROCESSES = {
        "system",
        "registry",
        "smss.exe",
        "csrss.exe",
        "wininit.exe",
        "services.exe",
        "lsass.exe",
        "winlogon.exe",
        "svchost.exe",
        "fontdrvhost.exe",
        "dwm.exe",
        "system idle process",
    }

    def __init__(self):
        super().__init__()

        self.setObjectName("processManager")
        self.setMinimumSize(750, 480)

        self.setup_ui()
        self.start_monitoring()

    # ==========================================
    # MAIN INTERFACE
    # ==========================================

    def setup_ui(self):

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(22, 22, 22, 22)
        main_layout.setSpacing(15)

        # HEADER
        title = QLabel("Process Manager")
        title.setObjectName("processTitle")

        subtitle = QLabel(
            "View and manage running system processes"
        )
        subtitle.setObjectName("processSubtitle")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # SUMMARY PANEL
        summary = QFrame()
        summary.setObjectName("processSummary")

        summary_layout = QHBoxLayout(summary)
        summary_layout.setContentsMargins(18, 14, 18, 14)

        self.process_count = QLabel("Processes: 0")
        self.process_count.setObjectName("processSummaryValue")

        self.update_status = QLabel("SYSTEM READY")
        self.update_status.setObjectName("processSummaryStatus")

        summary_layout.addWidget(self.process_count)
        summary_layout.addStretch()
        summary_layout.addWidget(self.update_status)

        main_layout.addWidget(summary)

        # SEARCH AND REFRESH
        controls = QHBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.setObjectName("processSearch")
        self.search_input.setPlaceholderText(
            "Search process name or PID..."
        )

        self.search_input.textChanged.connect(
            self.filter_processes
        )

        refresh_button = QPushButton("Refresh")
        refresh_button.setObjectName("processRefreshButton")
        refresh_button.clicked.connect(self.refresh_processes)

        controls.addWidget(self.search_input, 1)
        controls.addWidget(refresh_button)

        main_layout.addLayout(controls)

        # PROCESS TABLE
        self.process_table = QTableWidget()

        self.process_table.setObjectName("processTable")
        self.process_table.setColumnCount(4)

        self.process_table.setHorizontalHeaderLabels([
            "PROCESS NAME",
            "PID",
            "CPU %",
            "MEMORY",
        ])

        self.process_table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        self.process_table.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )

        self.process_table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        self.process_table.verticalHeader().setVisible(False)

        header = self.process_table.horizontalHeader()

        header.setSectionResizeMode(
            0,
            QHeaderView.ResizeMode.Stretch
        )

        for column in range(1, 4):
            header.setSectionResizeMode(
                column,
                QHeaderView.ResizeMode.ResizeToContents
            )

        main_layout.addWidget(self.process_table, 1)

        # BOTTOM CONTROLS
        bottom_layout = QHBoxLayout()

        self.selected_label = QLabel(
            "Select a process to manage it."
        )
        self.selected_label.setObjectName("processSelectedLabel")

        end_button = QPushButton("End Process")
        end_button.setObjectName("processEndButton")

        end_button.clicked.connect(
            self.end_selected_process
        )

        bottom_layout.addWidget(self.selected_label)
        bottom_layout.addStretch()
        bottom_layout.addWidget(end_button)

        main_layout.addLayout(bottom_layout)

    # ==========================================
    # PROCESS MONITORING
    # ==========================================

    def start_monitoring(self):

        # Initialize CPU measurements.
        for process in psutil.process_iter():
            try:
                process.cpu_percent(interval=None)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_processes)
        self.timer.start(3000)

        self.refresh_processes()

    def refresh_processes(self):

        search_text = self.search_input.text().strip().lower()

        processes = []

        for process in psutil.process_iter(
            ["pid", "name", "memory_info"]
        ):

            try:
                info = process.info

                pid = info["pid"]
                name = info["name"] or "Unknown"

                memory_info = info["memory_info"]

                memory_mb = (
                    memory_info.rss / (1024 * 1024)
                    if memory_info else 0
                )

                cpu = process.cpu_percent(interval=None)

                processes.append({
                    "pid": pid,
                    "name": name,
                    "cpu": cpu,
                    "memory": memory_mb,
                })

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess,
            ):
                continue

        processes.sort(
            key=lambda item: item["cpu"],
            reverse=True
        )

        self.all_processes = processes

        self.process_count.setText(
            f"Processes: {len(processes)}"
        )

        self.update_status.setText("LIVE MONITORING")

        self.display_processes(search_text)

    # ==========================================
    # DISPLAY PROCESS LIST
    # ==========================================

    def display_processes(self, search_text=""):

        filtered = []

        for process in self.all_processes:

            name = process["name"].lower()
            pid = str(process["pid"])

            if (
                search_text
                and search_text not in name
                and search_text not in pid
            ):
                continue

            filtered.append(process)

        self.process_table.setRowCount(len(filtered))

        for row, process in enumerate(filtered):

            values = [
                process["name"],
                str(process["pid"]),
                f'{process["cpu"]:.1f}%',
                f'{process["memory"]:.2f} MB',
            ]

            for column, value in enumerate(values):

                item = QTableWidgetItem(value)

                if column > 0:
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignCenter
                    )

                self.process_table.setItem(
                    row,
                    column,
                    item
                )

        self.process_table.resizeRowsToContents()

    # ==========================================
    # SEARCH
    # ==========================================

    def filter_processes(self, text):

        self.display_processes(
            text.strip().lower()
        )

    # ==========================================
    # END PROCESS
    # ==========================================

    def end_selected_process(self):

        selected_rows = (
            self.process_table.selectionModel().selectedRows()
        )

        if not selected_rows:
            QMessageBox.warning(
                self,
                "No Process Selected",
                "Please select a process first."
            )
            return

        row = selected_rows[0].row()

        pid_item = self.process_table.item(row, 1)
        name_item = self.process_table.item(row, 0)

        if pid_item is None or name_item is None:
            return

        pid = int(pid_item.text())
        name = name_item.text()

        if name.lower() in self.PROTECTED_PROCESSES:
            QMessageBox.warning(
                self,
                "Protected Process",
                "This process is protected against termination."
            )
            return

        answer = QMessageBox.question(
            self,
            "Confirm Termination",
            f"Are you sure you want to end this process?\n\n"
            f"Process: {name}\n"
            f"PID: {pid}",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if answer != QMessageBox.StandardButton.Yes:
            return

        try:
            process = psutil.Process(pid)

            process_name = process.name()

            if process_name.lower() != name.lower():
                QMessageBox.warning(
                    self,
                    "Process Changed",
                    "The selected process has changed. Refresh and try again."
                )
                self.refresh_processes()
                return

            process.terminate()

            try:
                process.wait(timeout=3)
                QMessageBox.information(
                    self,
                    "Process Terminated",
                    f"{name} was terminated successfully."
                )

            except psutil.TimeoutExpired:
                QMessageBox.warning(
                    self,
                    "Termination Pending",
                    "The process did not exit within 3 seconds."
                )

        except psutil.NoSuchProcess:
            QMessageBox.warning(
                self,
                "Process Not Found",
                "The process may have already closed."
            )

        except psutil.AccessDenied:
            QMessageBox.critical(
                self,
                "Access Denied",
                "Windows denied permission to terminate this process."
            )

        except psutil.Error as error:
            QMessageBox.critical(
                self,
                "Process Error",
                f"Could not terminate process:\n{error}"
            )

        self.refresh_processes()
