from home import *


def clicked_action():
    print("Button clicked")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.pushButton.clicked.connect(lambda: clicked_action())
    MainWindow.show()
    sys.exit(app.exec_())
