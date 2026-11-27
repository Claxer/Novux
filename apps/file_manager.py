import os

from pathlib import Path

from PySide6.QtCore import QDir, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTreeView,
    QFileSystemModel,
    QHeaderView,
    QMessageBox,
)


class FileManager(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName("fileManager")

        self.current_path = str(Path.home())
        self.history = [self.current_path]
        self.history_index = 0

        self.setup_ui()
        self.setup_file_system()
        self.navigate_to(self.current_path)

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(22, 20, 22, 20)
        main_layout.setSpacing(14)

        # Header
        header_layout = QVBoxLayout()

        title = QLabel("File Manager")
        title.setObjectName("fileManagerTitle")

        subtitle = QLabel(
            "Browse and manage files on your computer"
        )
        subtitle.setObjectName("fileManagerSubtitle")

        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)

        main_layout.addLayout(header_layout)

        # Navigation controls
        navigation_layout = QHBoxLayout()
        navigation_layout.setSpacing(8)

        self.back_button = QPushButton("←")
        self.back_button.setToolTip("Go Back")
        self.back_button.clicked.connect(self.go_back)

        self.forward_button = QPushButton("→")
        self.forward_button.setToolTip("Go Forward")
        self.forward_button.clicked.connect(self.go_forward)

        self.up_button = QPushButton("↑")
        self.up_button.setToolTip("Go to Parent Folder")
        self.up_button.clicked.connect(self.go_up)

        self.refresh_button = QPushButton("⟳")
        self.refresh_button.setToolTip("Refresh")
        self.refresh_button.clicked.connect(self.refresh)

        self.path_input = QLineEdit()
        self.path_input.setObjectName("fileManagerPath")
        self.path_input.setPlaceholderText("Enter folder path...")
        self.path_input.returnPressed.connect(
            self.open_path_from_input
        )

        navigation_layout.addWidget(self.back_button)
        navigation_layout.addWidget(self.forward_button)
        navigation_layout.addWidget(self.up_button)
        navigation_layout.addWidget(self.path_input, 1)
        navigation_layout.addWidget(self.refresh_button)

        main_layout.addLayout(navigation_layout)

        # Current location
        self.location_label = QLabel()
        self.location_label.setObjectName(
            "fileManagerLocation"
        )

        main_layout.addWidget(self.location_label)

        # File and folder table
        self.file_view = QTreeView()
        self.file_view.setObjectName("fileManagerTree")
        self.file_view.setAlternatingRowColors(True)
        self.file_view.setSortingEnabled(True)
        self.file_view.setAnimated(True)
        self.file_view.setIndentation(20)

        self.file_view.doubleClicked.connect(
            self.open_selected_item
        )

        main_layout.addWidget(self.file_view, 1)

        # Footer
        self.status_label = QLabel("Ready")
        self.status_label.setObjectName("fileManagerStatus")

        main_layout.addWidget(self.status_label)

    def setup_file_system(self):
        self.file_model = QFileSystemModel(self)

        self.file_model.setRootPath(
            QDir.rootPath()
        )

        self.file_model.setFilter(
            QDir.Filter.AllEntries
            | QDir.Filter.NoDotAndDotDot
            | QDir.Filter.AllDirs
            | QDir.Filter.Files
        )

        self.file_view.setModel(self.file_model)

        self.file_view.setColumnWidth(0, 350)
        self.file_view.setColumnWidth(1, 100)
        self.file_view.setColumnWidth(2, 120)

        header = self.file_view.header()
        header.setSectionResizeMode(
            0, QHeaderView.ResizeMode.Stretch
        )

        header.setSectionResizeMode(
            1, QHeaderView.ResizeMode.ResizeToContents
        )

        header.setSectionResizeMode(
            2, QHeaderView.ResizeMode.ResizeToContents
        )

        header.setSectionResizeMode(
            3, QHeaderView.ResizeMode.ResizeToContents
        )

    def navigate_to(self, path, add_history=True):
        target = Path(path).expanduser()

        if not target.exists() or not target.is_dir():
            QMessageBox.warning(
                self,
                "Invalid Location",
                "The selected folder does not exist."
            )
            return

        self.current_path = str(target.resolve())

        index = self.file_model.index(
            self.current_path
        )

        self.file_view.setRootIndex(index)

        self.path_input.setText(self.current_path)
        self.location_label.setText(
            f"Location: {self.current_path}"
        )

        if add_history:
            if self.history_index < len(self.history) - 1:
                self.history = self.history[
                    :self.history_index + 1
                ]

            if self.history[-1] != self.current_path:
                self.history.append(self.current_path)

            self.history_index = len(self.history) - 1

        self.update_navigation_buttons()

        self.status_label.setText(
            f"Browsing: {self.current_path}"
        )

    def open_path_from_input(self):
        self.navigate_to(self.path_input.text())

    def open_selected_item(self, index):
        path = self.file_model.filePath(index)

        if os.path.isdir(path):
            self.navigate_to(path)
        else:
            success = QDesktopServices.openUrl(
                QUrl.fromLocalFile(path)
            )

            if not success:
                QMessageBox.warning(
                    self,
                    "Unable to Open File",
                    "Windows could not open this file."
                )

    def go_back(self):
        if self.history_index > 0:
            self.history_index -= 1

            self.navigate_to(
                self.history[self.history_index],
                add_history=False
            )

    def go_forward(self):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1

            self.navigate_to(
                self.history[self.history_index],
                add_history=False
            )

    def go_up(self):
        parent = str(Path(self.current_path).parent)

        if parent != self.current_path:
            self.navigate_to(parent)

    def refresh(self):
        self.file_model.setRootPath(QDir.rootPath())

        self.navigate_to(
            self.current_path,
            add_history=False
        )

    def update_navigation_buttons(self):
        self.back_button.setEnabled(
            self.history_index > 0
        )

        self.forward_button.setEnabled(
            self.history_index < len(self.history) - 1
        )

        self.up_button.setEnabled(
            str(Path(self.current_path).parent)
            != self.current_path
        )
