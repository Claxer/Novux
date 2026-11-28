import os
import subprocess

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QTextEdit,
    QLineEdit,
    QPushButton,
)


class Terminal(QWidget):

    def __init__(self):
        super().__init__()

        self.current_directory = os.path.expanduser("~")

        self.setObjectName("terminalApp")

        self.setup_ui()
        self.print_welcome_message()

    def setup_ui(self):

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 18, 20, 18)
        main_layout.setSpacing(12)

        # Terminal Header
        self.title = QLabel("NOVUX TERMINAL")
        self.title.setObjectName("terminalTitle")

        self.subtitle = QLabel(
            "Command-line interface | Windows Environment"
        )
        self.subtitle.setObjectName("terminalSubtitle")

        main_layout.addWidget(self.title)
        main_layout.addWidget(self.subtitle)

        # Terminal Output
        self.output = QTextEdit()
        self.output.setObjectName("terminalOutput")
        self.output.setReadOnly(True)
        self.output.setAcceptRichText(False)

        main_layout.addWidget(self.output, 1)

        # Command Input
        input_layout = QHBoxLayout()
        input_layout.setSpacing(8)

        self.prompt = QLabel("NOVUX >")
        self.prompt.setObjectName("terminalPrompt")

        self.command_input = QLineEdit()
        self.command_input.setObjectName("terminalInput")
        self.command_input.setPlaceholderText("Enter a command...")
        self.command_input.returnPressed.connect(self.execute_command)

        self.run_button = QPushButton("RUN")
        self.run_button.setObjectName("terminalRunButton")
        self.run_button.clicked.connect(self.execute_command)

        input_layout.addWidget(self.prompt)
        input_layout.addWidget(self.command_input, 1)
        input_layout.addWidget(self.run_button)

        main_layout.addLayout(input_layout)

        # Current Directory
        self.directory_label = QLabel()
        self.directory_label.setObjectName("terminalStatus")

        main_layout.addWidget(self.directory_label)

        self.update_directory_label()

    def print_welcome_message(self):

        self.write_output("========================================")
        self.write_output("          WELCOME TO NOVUX TERMINAL")
        self.write_output("========================================")
        self.write_output("Type 'help' to see available commands.")
        self.write_output("")

    def write_output(self, message):

        self.output.append(str(message))

    def update_directory_label(self):

        self.directory_label.setText(
            f"CURRENT DIRECTORY: {self.current_directory}"
        )

    def execute_command(self):

        command = self.command_input.text().strip()

        if not command:
            return

        self.write_output(
            f"\n{self.current_directory}> {command}"
        )

        self.command_input.clear()

        command_lower = command.lower()

        # Help Command
        if command_lower == "help":

            self.write_output("AVAILABLE COMMANDS")
            self.write_output("------------------")
            self.write_output("help       - Show available commands")
            self.write_output("clear/cls  - Clear terminal output")
            self.write_output("pwd        - Show current directory")
            self.write_output("dir / ls   - List files and folders")
            self.write_output("cd         - Change directory")
            self.write_output("Other commands are passed to Windows CMD.")
            return

        # Clear Command
        if command_lower in ("clear", "cls"):

            self.output.clear()
            return

        # Current Directory
        if command_lower == "pwd":

            self.write_output(self.current_directory)
            return

        # List Files and Folders
        if command_lower in ("dir", "ls"):

            try:
                items = os.listdir(self.current_directory)

                if not items:
                    self.write_output("This directory is empty.")
                else:
                    for item in sorted(items, key=str.lower):
                        full_path = os.path.join(
                            self.current_directory, item
                        )

                        if os.path.isdir(full_path):
                            self.write_output(f"[DIR]  {item}")
                        else:
                            self.write_output(f"[FILE] {item}")

            except OSError as error:
                self.write_output(f"Error: {error}")

            return

        # Change Directory
        if command_lower == "cd" or command_lower.startswith("cd "):

            path = command[2:].strip().strip('"')

            if not path:
                self.write_output(self.current_directory)
                return

            if path == "..":
                new_directory = os.path.dirname(
                    self.current_directory
                )
            elif os.path.isabs(path):
                new_directory = os.path.normpath(path)
            else:
                new_directory = os.path.normpath(
                    os.path.join(self.current_directory, path)
                )

            if os.path.isdir(new_directory):
                self.current_directory = new_directory
                self.write_output(
                    f"Directory changed to: {self.current_directory}"
                )
                self.update_directory_label()
            else:
                self.write_output("Error: Directory not found.")

            return

        # Execute Windows Commands
        try:

            result = subprocess.run(
                ["cmd.exe", "/c", command],
                cwd=self.current_directory,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=15
            )

            if result.stdout.strip():
                self.write_output(result.stdout.rstrip())

            if result.stderr.strip():
                self.write_output(result.stderr.rstrip())

            if result.returncode != 0 and not result.stdout.strip() and not result.stderr.strip():
                self.write_output(
                    f"Command finished with exit code {result.returncode}."
                )

        except subprocess.TimeoutExpired:
            self.write_output("Error: Command timed out after 15 seconds.")

        except Exception as error:
            self.write_output(f"Execution error: {error}")

