import sys
from main_window import MainWindow
from display import Display, Info, ButtonsGrid
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH

if __name__ == "__main__":
    # make aplication
    app = QApplication(sys.argv)
    window = MainWindow()

    # icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # info
    info = Info("0")
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText("Digite")
    window.addWidgetToVLayout(display)

    # Display / Button Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Initialize
    window.adjustFixedSize()
    window.show()
    app.exec()
