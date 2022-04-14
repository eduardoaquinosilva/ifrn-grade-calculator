from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Loading(QtWidgets.QMainWindow):
    def setupUi(self, Loading):
        Loading.setObjectName("Splash")
        Loading.resize(405, 176)
        self.centralwidget = QtWidgets.QWidget(Loading)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 30, 131, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("loading.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(17, 120, 371, 23))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("barra_progresso")
        Loading.setCentralWidget(self.centralwidget)

        # No buttons
        Loading.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)

        # GIF Animation
        movie = QtGui.QMovie("loading.gif")
        self.label.setMovie(movie)
        movie.start()

        self.retranslateUi(Loading)
        QtCore.QMetaObject.connectSlotsByName(Loading)

    def retranslateUi(self, Loading):
        _translate = QtCore.QCoreApplication.translate
        Loading.setWindowTitle(_translate("Loading", "MainWindow"))


if __name__ == "__main__":
    import sys
    import time
    from calculadora_ifrn import Ui_MainWindow
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Loading()
    ui.setupUi(Main)
    Main.show()

    for i in range(1, 101):
        ui.progress_bar.setValue(i)
        ui.progress_bar.setTextVisible(True)
        time.sleep(0.05)
        app.processEvents()

    # Calling Calculator
    Calc = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Calc)
    Calc.show()

    # Close Loading
    Main.hide()
    sys.exit(app.exec_())
