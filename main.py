from PyQt5.QtWidgets import *
import gui
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    size = screen.size()
    window = gui.Window(size.width(), size.height())
    sys.exit(app.exec())