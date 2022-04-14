from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 542)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 0, 311, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo-ifrn-grande.png"))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 130, 181, 31))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 520, 301, 16))
        self.label_3.setObjectName("label_3")

        self.btn_calc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calc.setGeometry(QtCore.QRect(230, 350, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_calc.setFont(font)
        self.btn_calc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_calc.setStyleSheet("border-radius: 20px;\nbackground-color: rgb(41, 204, 55);")
        self.btn_calc.setObjectName("btn_calc")

        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(80, 350, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reset.setFont(font)
        self.btn_reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_reset.setStyleSheet("border-radius: 20px;\nbackground-color: white;")
        self.btn_reset.setObjectName("btn_reset")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 180, 291, 151))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.bimesters = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bimesters.setFont(font)
        self.bimesters.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bimesters.setStyleSheet("color: white;\nbackground-color: green;")
        self.bimesters.setObjectName("bimesters")
        self.bimesters.addItem("")
        self.bimesters.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bimesters)

        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)

        self.le_grade1 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_grade1.setFont(font)
        self.le_grade1.setStyleSheet("color: white;\nbackground-color: green;")
        self.le_grade1.setObjectName("le_grade1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_grade1)

        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setStyleSheet("color: white;")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)

        self.le_grade2 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_grade2.setFont(font)
        self.le_grade2.setStyleSheet("color: white;\nbackground-color: green;")
        self.le_grade2.setObjectName("le_grade2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_grade2)

        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setStyleSheet("color: white;")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)

        self.le_grade3 = QtWidgets.QLineEdit(self.widget)
        self.le_grade3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_grade3.setFont(font)
        self.le_grade3.setStyleSheet("color: white;\nbackground-color: green;")
        self.le_grade3.setObjectName("le_grade3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_grade3)

        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setStyleSheet("color: white;")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)

        self.le_grade4 = QtWidgets.QLineEdit(self.widget)
        self.le_grade4.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_grade4.setFont(font)
        self.le_grade4.setStyleSheet("color: white;\nbackground-color: green;")
        self.le_grade4.setObjectName("le_grade4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.le_grade4)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(40, 420, 362, 89))
        self.widget1.setObjectName("widget1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget1)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")

        self.label_9 = QtWidgets.QLabel(self.widget1)
        self.label_9.setStyleSheet("color: white;\n")
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)

        self.final_grade = QtWidgets.QLineEdit(self.widget1)
        self.final_grade.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.final_grade.setFont(font)
        self.final_grade.setStyleSheet("color: white;\nbackground-color: green;")
        self.final_grade.setObjectName("final_grade")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.final_grade)

        self.label_10 = QtWidgets.QLabel(self.widget1)
        self.label_10.setStyleSheet("color: white;")
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)

        self.situation = QtWidgets.QLineEdit(self.widget1)
        self.situation.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.situation.setFont(font)
        self.situation.setStyleSheet("color: white;\nbackground-color: green;")
        self.situation.setObjectName("situation")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.situation)

        self.label_11 = QtWidgets.QLabel(self.widget1)
        self.label_11.setStyleSheet("color: white;")
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)

        self.final_test = QtWidgets.QLineEdit(self.widget1)
        self.final_test.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.final_test.setFont(font)
        self.final_test.setStyleSheet("color: white;\nbackground-color: green;")
        self.final_test.setObjectName("final_test")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.final_test)
        MainWindow.setCentralWidget(self.centralwidget)

        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())

        # Calling methods
        self.bimesters.currentIndexChanged.connect(self.changing_fields)
        self.btn_calc.clicked.connect(self.calc)
        self.btn_reset.clicked.connect(self.reset)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.bimesters, self.le_grade1)
        MainWindow.setTabOrder(self.le_grade1, self.le_grade2)
        MainWindow.setTabOrder(self.le_grade2, self.le_grade3)
        MainWindow.setTabOrder(self.le_grade3, self.le_grade4)
        MainWindow.setTabOrder(self.le_grade4, self.btn_calc)
        MainWindow.setTabOrder(self.btn_calc, self.btn_reset)
        MainWindow.setTabOrder(self.btn_reset, self.final_grade)
        MainWindow.setTabOrder(self.final_grade, self.situation)
        MainWindow.setTabOrder(self.situation, self.final_test)

    def changing_fields(self):
        if int(self.bimesters.currentText()) == 2:
            self.le_grade3.setEnabled(False)
            self.le_grade4.setEnabled(False)
        else:
            self.le_grade3.setEnabled(True)
            self.le_grade4.setEnabled(True)
        self.reset()

    def reset(self):
        self.le_grade1.setText("")
        self.le_grade2.setText("")
        self.le_grade3.setText("")
        self.le_grade4.setText("")
        self.final_grade.setText("")
        self.situation.setText("")
        self.final_test.setText("")

    def calc(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Erro")

        if int(self.bimesters.currentText()) == 2:
            try:
                num1, num2 = int(self.le_grade1.text()), int(self.le_grade2.text())
                average = int(round(((num1*2 + num2*3)/5), 0))
                self.final_grade.setText(str(average))
                if average >= 60:
                    self.situation.setText("Aprovado")
                elif average < 40:
                    self.situation.setText("Reprovado")
                else:
                    self.situation.setText("Em recuperação")

                if 40 <= average < 60:
                    grade_final = 120 - average
                    self.final_test.setText(str(grade_final))
                else:
                    self.final_test.setText("-")
            except ValueError:
                msg.setText("Números Incorretos!")
                msg.exec()
        else:
            try:
                num1, num2 = int(self.le_grade1.text()), int(self.le_grade2.text()),
                num3, num4 = int(self.le_grade3.text()), int(self.le_grade4.text())
                average = int(round(((num1*2 + num2*2 + num3*3 + num4*3)/10), 0))
                self.final_grade.setText(str(average))
                if average >= 60:
                    self.situation.setText("Aprovado")
                elif average < 40:
                    self.situation.setText("Reprovado")
                else:
                    self.situation.setText("Em recuperação")

                if 40 <= average < 60:
                    grade_final = 120 - average
                    self.final_test.setText(str(grade_final))
                else:
                    self.final_test.setText("-")
            except ValueError:
                msg.setText("Números Incorretos!")
                msg.exec()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora IFRN"))

        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; "
                                                      "font-weight:600; color:#ffffff;\">CALCULADORA IFRN</span></p>"
                                                      "</body></html>"))

        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#319331;\">As notas "
                                                      "devem ser inseridas utilizando a notação de 0 a 100</span></p>"
                                                      "</body></html>"))

        self.btn_calc.setText(_translate("MainWindow", "CALCULAR"))
        self.btn_calc.setShortcut(_translate("MainWindow", "Return, Enter"))

        self.btn_reset.setText(_translate("MainWindow", "ZERAR"))

        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Quant. "
                                                      "de bimestres:</span></p></body></html>"))

        self.bimesters.setItemText(0, _translate("MainWindow", "4"))
        self.bimesters.setItemText(1, _translate("MainWindow", "2"))

        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nota do "
                                                      "1º Bimestre:</span></p></body></html>"))

        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nota do "
                                                      "2º Bimestre:</span></p></body></html>"))

        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nota do "
                                                      "3º Bimestre:</span></p></body></html>"))

        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nota do "
                                                      "4º Bimestre:</span></p></body></html>"))

        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Média "
                                                      "Final:</span></p></body></html>"))

        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">"
                                                       "Situação:</span></p></body></html>"))

        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nota "
                                                       "necessária na Prova Final:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
