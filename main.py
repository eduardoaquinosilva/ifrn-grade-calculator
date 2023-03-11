from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMessageBox


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(482, 639)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Calculator.setWindowIcon(icon)
        Calculator.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 311, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/logo-ifrn-grande.png"))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 361, 51))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 180, 151, 21))
        self.label_3.setStyleSheet("color: #fff;")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 220, 151, 16))
        self.label_4.setStyleSheet("color: #fff;")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 260, 151, 21))
        self.label_5.setStyleSheet("color: #fff;")
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 300, 151, 21))
        self.label_6.setStyleSheet("color: #fff;")
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 340, 151, 21))
        self.label_7.setStyleSheet("color: #fff;")
        self.label_7.setObjectName("label_7")

        self.cb_bimesters = QtWidgets.QComboBox(self.centralwidget)
        self.cb_bimesters.setGeometry(QtCore.QRect(270, 180, 111, 22))
        self.cb_bimesters.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cb_bimesters.setStyleSheet("color: #fff;\nbackground-color: #008000; \nfont: 12pt \"MS Shell Dlg 2\";")
        self.cb_bimesters.setObjectName("cb_bimesters")
        self.cb_bimesters.addItem("")
        self.cb_bimesters.addItem("")

        self.pb_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pb_reset.setGeometry(QtCore.QRect(140, 380, 91, 41))
        self.pb_reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_reset.setStyleSheet("background-color: #fff;\nfont: 12pt \"MS Shell Dlg 2\";\nborder-radius: 10px;")
        self.pb_reset.setObjectName("pb_reset")

        self.pb_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.pb_calculate.setGeometry(QtCore.QRect(260, 380, 91, 41))
        self.pb_calculate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_calculate.setStyleSheet("color: #000;\nbackground-color: #29cc37;\nfont: 12pt \"MS Shell Dlg 2\";\n"
                                        "border-radius: 10px;")
        self.pb_calculate.setObjectName("pb_calculate")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 440, 91, 21))
        self.label_8.setStyleSheet("color: #fff;")
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 480, 91, 21))
        self.label_9.setStyleSheet("color: #fff;")
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(60, 520, 71, 21))
        self.label_10.setStyleSheet("color: #fff;")
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(60, 560, 221, 21))
        self.label_11.setStyleSheet("color: #fff;")
        self.label_11.setObjectName("label_11")

        self.le_lastGrade = QtWidgets.QLineEdit(self.centralwidget)
        self.le_lastGrade.setGeometry(QtCore.QRect(310, 440, 113, 20))
        self.le_lastGrade.setStyleSheet("color: #fff;\nbackground-color: #008000;\nfont: 12pt \"MS Shell Dlg 2\";")
        self.le_lastGrade.setReadOnly(True)
        self.le_lastGrade.setObjectName("le_lastGrade")

        self.le_average = QtWidgets.QLineEdit(self.centralwidget)
        self.le_average.setGeometry(QtCore.QRect(310, 480, 113, 20))
        self.le_average.setStyleSheet("color: #fff;\nbackground-color: #008000;\nfont: 12pt \"MS Shell Dlg 2\";")
        self.le_average.setReadOnly(True)
        self.le_average.setObjectName("le_average")

        self.le_status = QtWidgets.QLineEdit(self.centralwidget)
        self.le_status.setGeometry(QtCore.QRect(310, 520, 113, 20))
        self.le_status.setStyleSheet("color: #fff;\nbackground-color: #008000;\nfont: 12pt \"MS Shell Dlg 2\";")
        self.le_status.setReadOnly(True)
        self.le_status.setObjectName("le_status")

        self.le_finalTest = QtWidgets.QLineEdit(self.centralwidget)
        self.le_finalTest.setGeometry(QtCore.QRect(310, 560, 113, 20))
        self.le_finalTest.setStyleSheet("color: #fff;\nbackground-color: #008000;\nfont: 12pt \"MS Shell Dlg 2\";")
        self.le_finalTest.setReadOnly(True)
        self.le_finalTest.setObjectName("le_finalTest")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(100, 610, 291, 16))
        self.label_12.setStyleSheet("color: #008000;")
        self.label_12.setObjectName("label_12")

        onlyInt = QIntValidator()
        onlyInt.setRange(0, 100)

        self.le_grade1 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_grade1.setGeometry(QtCore.QRect(270, 220, 113, 20))
        self.le_grade1.setStyleSheet("color: #fff;\nbackground-color: #008000;\nfont: 12pt \"MS Shell Dlg 2\";")
        self.le_grade1.setMaxLength(100)
        self.le_grade1.setObjectName("le_grade1")
        self.le_grade1.setValidator(onlyInt)

        self.le_grade2 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_grade2.setGeometry(QtCore.QRect(270, 260, 113, 20))
        self.le_grade2.setStyleSheet("color: #fff;\nbackground-color: #008000;\nfont: 12pt \"MS Shell Dlg 2\";")
        self.le_grade2.setMaxLength(100)
        self.le_grade2.setObjectName("le_grade2")
        self.le_grade2.setValidator(onlyInt)

        self.le_grade3 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_grade3.setGeometry(QtCore.QRect(270, 300, 113, 20))
        self.le_grade3.setStyleSheet("color: #fff;\nbackground-color: #008000;\nfont: 12pt \"MS Shell Dlg 2\";")
        self.le_grade3.setMaxLength(100)
        self.le_grade3.setObjectName("le_grade3")
        self.le_grade3.setValidator(onlyInt)

        self.le_grade4 = QtWidgets.QLineEdit(self.centralwidget)
        self.le_grade4.setGeometry(QtCore.QRect(270, 340, 113, 20))
        self.le_grade4.setStyleSheet("color: #fff;\nbackground-color: #008000;\nfont: 12pt \"MS Shell Dlg 2\";")
        self.le_grade4.setMaxLength(100)
        self.le_grade4.setObjectName("le_grade4")
        self.le_grade4.setValidator(onlyInt)
        Calculator.setCentralWidget(self.centralwidget)

        Calculator.setFixedSize(Calculator.width(), Calculator.height())

        global msg
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Erro")

        # Calling methods
        self.cb_bimesters.currentIndexChanged.connect(self.changed_selection)
        self.pb_reset.clicked.connect(lambda: self.reset(True))
        self.pb_calculate.clicked.connect(self.pre_calc)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)
        Calculator.setTabOrder(self.cb_bimesters, self.le_grade1)
        Calculator.setTabOrder(self.le_grade1, self.le_grade2)
        Calculator.setTabOrder(self.le_grade2, self.le_grade3)
        Calculator.setTabOrder(self.le_grade3, self.le_grade4)
        Calculator.setTabOrder(self.le_grade4, self.pb_calculate)
        Calculator.setTabOrder(self.pb_calculate, self.pb_reset)


    def changed_selection(self):
        if int(self.cb_bimesters.currentText()) == 2:
            self.disable(True)
            self.reset(False)
        else:
            self.disable(False)
            self.reset(False)


    def disable(self, status):
        if status:
            self.le_grade3.setEnabled(False)
            self.le_grade4.setEnabled(False)
        else:
            self.le_grade3.setEnabled(True)
            self.le_grade4.setEnabled(True)


    def reset(self, status=True):
        if status:
            self.le_grade1.setText("")
            self.le_grade2.setText("")
            self.le_grade3.setText("")
            self.le_grade4.setText("")
            self.le_lastGrade.setText("")
            self.le_average.setText("")
            self.le_status.setText("")
            self.le_finalTest.setText("")
        else:
            self.le_grade3.setText("")
            self.le_grade4.setText("")


    def pre_calc(self):
        if int(self.cb_bimesters.currentText()) == 2:
            if len(self.le_grade1.text()) == 0:
                self.invalid_input()
            elif len(self.le_grade2.text()) == 0:
                self.last_grade_calc(int(self.le_grade1.text()))
            else:
                self.average_calc(self.le_grade1.text(), self.le_grade2.text())
        else:
            if len(self.le_grade1.text()) == 0 or len(self.le_grade2.text()) == 0 or len(self.le_grade3.text()) == 0:
                self.invalid_input()
            elif len(self.le_grade4.text()) == 0:
                self.last_grade_calc(int(self.le_grade1.text()), int(self.le_grade2.text()), int(self.le_grade3.text()))
            else:
                self.average_calc(self.le_grade1.text(), self.le_grade2.text(), self.le_grade3.text(),
                                  self.le_grade4.text())


    def invalid_input(self):
        global msg
        msg.setText("Entrada inválida!")
        msg.exec()


    def last_grade_calc(self, *grades):
        invalid = False
        for a in grades:
            if int(a) > 100:
                self.invalid_input()
                invalid = True
                break
        if invalid:
            return 0

        if len(grades) == 1:
            result = ((300 - (grades[0] * 2)) / 3)
            self.show_results(round(result), '-', '-', '-')
        elif len(grades) == 3:
            result = (600 - (grades[0] * 2) - (grades[1] * 2) - (grades[2] * 3)) / 3
            self.show_results(round(result), '-', '-', '-')


    def average_calc(self, *grades):
        invalid = False
        for b in grades:
            if int(b) > 100:
                self.invalid_input()
                invalid = True
                break
        if invalid:
            return 0

        if len(grades) == 2:
            result, situation = round((int(grades[0]) * 2 + int(grades[1]) * 3) / 5), None
            if result >= 60:
                situation = "Aprovado"
            elif result < 20:
                situation = "Reprovado"
            else:
                situation = "Recuperação"

            if situation == "Recuperação":
                f1 = 120 - result
                f2 = int((300 - (int(grades[1]) * 3)) / 2)
                f3 = int((300 - (int(grades[0]) * 2)) / 3)
                final_test_grade = round(min(f1, f2, f3))
            else:
                final_test_grade = "-"

            self.show_results('-', result, situation, final_test_grade)
        elif len(grades) == 4:
            result, situation = round((int(grades[0]) * 2 + int(grades[1]) * 2 + int(grades[2]) * 3 + int(grades[3]) *
                                       3) / 10),  None
            if result >= 60:
                situation = "Aprovado"
            elif result < 20:
                situation = "Reprovado"
            else:
                situation = "Recuperação"

            if situation == "Recuperação":
                f1 = 120 - result
                f2 = int(300 - int(grades[1]) - ((int(grades[2]) * 3) / 2) - ((int(grades[3]) * 3) / 2))
                f3 = int(300 - int(grades[0]) - ((int(grades[2]) * 3) / 2) - ((int(grades[3]) * 3) / 2))
                f4 = int(200 - int(grades[3]) - ((int(grades[0]) * 2) / 3) - ((int(grades[1]) * 2) / 3))
                f5 = int(200 - int(grades[2]) - ((int(grades[0]) * 2) / 3) - ((int(grades[1]) * 2) / 3))
                final_test_grade = round(min(f1, f2, f3, f4, f5))
            else:
                final_test_grade = "-"

            self.show_results('-', result, situation, final_test_grade)


    def show_results(self, v1, v2, v3, v4):
        self.le_lastGrade.setText(str(v1))
        self.le_average.setText(str(v2))
        self.le_status.setText(str(v3))
        self.le_finalTest.setText(str(v4))


    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculadora de Notas IFRN"))
        self.label_2.setText(_translate("Calculator", "<html><head/><body><p><span style=\"font-size:36pt; color:"
                                                      "#ffffff;\">Calculadora IFRN</span></p></body></html>"))
        self.label_3.setText(_translate("Calculator", "<html><head/><body><p><span style=\" font-size:12pt;\">Quant. de"
                                                      " bimestres:</span></p></body></html>"))
        self.label_4.setText(_translate("Calculator", "<html><head/><body><p><span style=\" font-size:12pt;\">Nota do "
                                                      "1º Bimestre:</span></p></body></html>"))
        self.label_5.setText(_translate("Calculator", "<html><head/><body><p><span style=\" font-size:12pt;\">Nota do "
                                                      "2º Bimestre:</span></p></body></html>"))
        self.label_6.setText(_translate("Calculator", "<html><head/><body><p><span style=\" font-size:12pt;\">Nota do "
                                                      "3º Bimestre:</span></p></body></html>"))
        self.label_7.setText(_translate("Calculator", "<html><head/><body><p><span style=\" font-size:12pt;\">Nota do "
                                                      "4º Bimestre:</span></p></body></html>"))
        self.cb_bimesters.setItemText(0, _translate("Calculator", "4"))
        self.cb_bimesters.setItemText(1, _translate("Calculator", "2"))
        self.pb_reset.setText(_translate("Calculator", "ZERAR"))
        self.pb_calculate.setText(_translate("Calculator", "CALCULAR"))
        self.label_8.setText(_translate("Calculator", "<html><head/><body><p><span style=\" font-size:12pt;\">Última "
                                                      "Nota:</span></p></body></html>"))
        self.label_9.setText(_translate("Calculator", "<html><head/><body><p><span style=\" font-size:12pt;\">Média "
                                                      "Final:</span></p></body></html>"))
        self.label_10.setText(_translate("Calculator", "<html><head/><body><p><span style=\" font-size:12pt;\">Situação"
                                                       ":</span></p></body></html>"))
        self.label_11.setText(_translate("Calculator", "<html><head/><body><p><span style=\" font-size:12pt;\">Nota "
                                                       "Necessária na Prova Final:</span></p></body></html>"))
        self.label_12.setText(_translate("Calculator", "As notas devem ser inseridas usando a notação de 0 a 100"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
