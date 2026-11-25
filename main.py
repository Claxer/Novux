import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont

from desktop.desktop import NovuxDesktop


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("Novux")
    app.setOrganizationName("Novux Systems")
    app.setFont(QFont("Segoe UI", 10))

    stylesheet_path = (
        Path(__file__).parent
        / "resources"
        / "styles.qss"
    )

    if stylesheet_path.exists():
        with open(stylesheet_path, "r", encoding="utf-8") as file:
            app.setStyleSheet(file.read())

    desktop = NovuxDesktop()
    desktop.showFullScreen()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
