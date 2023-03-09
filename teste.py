# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.HighVoltage = QtWidgets.QFrame(self.centralwidget)
        self.HighVoltage.setGeometry(QtCore.QRect(15, 55, 178, 137))
        self.HighVoltage.setStyleSheet("QFrame{\n"
"    border-radius: 2px;\n"
"    background-color: rgb(44, 44, 44);\n"
"    background-position: center;\n"
"}")
        self.HighVoltage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HighVoltage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HighVoltage.setObjectName("HighVoltage")
        self.progressBar = QtWidgets.QProgressBar(self.HighVoltage)
        self.progressBar.setGeometry(QtCore.QRect(30, 100, 118, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(44, 44, 44);\n"
"    border-color: rgb(23, 165, 0);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"     border-radius: 5px;\n"
"     background-color: green;\n"
" }\n"
"")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.LowVoltage = QtWidgets.QFrame(self.centralwidget)
        self.LowVoltage.setGeometry(QtCore.QRect(15, 227, 178, 90))
        self.LowVoltage.setStyleSheet("QFrame{\n"
"    border-radius: 2px;\n"
"    background-color: rgb(44, 44, 44);\n"
"    background-position: center;\n"
"}")
        self.LowVoltage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LowVoltage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LowVoltage.setObjectName("LowVoltage")
        self.Motor = QtWidgets.QFrame(self.centralwidget)
        self.Motor.setGeometry(QtCore.QRect(447, 55, 178, 137))
        self.Motor.setStyleSheet("QFrame{\n"
"    border-radius: 2px;\n"
"    background-color: rgb(44, 44, 44);\n"
"    background-position: center;\n"
"}")
        self.Motor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Motor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Motor.setObjectName("Motor")
        self.System = QtWidgets.QFrame(self.centralwidget)
        self.System.setGeometry(QtCore.QRect(447, 225, 178, 90))
        self.System.setStyleSheet("QFrame{\n"
"    border-radius: 2px;\n"
"    background-color: rgb(44, 44, 44);\n"
"    background-position: center;\n"
"}")
        self.System.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.System.setFrameShadow(QtWidgets.QFrame.Raised)
        self.System.setObjectName("System")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(730, 410, 301, 301))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.Odometer = QtWidgets.QFrame(self.centralwidget)
        self.Odometer.setGeometry(QtCore.QRect(202, 79, 236, 236))
        self.Odometer.setStyleSheet("QFrame{\n"
"    background-color: rgb(44, 44, 44);\n"
"    color: #f8f8f2;\n"
"    border-radius: 120px;\n"
"}")
        self.Odometer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Odometer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Odometer.setObjectName("Odometer")
        self.Bottom = QtWidgets.QFrame(self.centralwidget)
        self.Bottom.setGeometry(QtCore.QRect(0, 370, 641, 91))
        self.Bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Bottom.setObjectName("Bottom")
        self.AutorcrossStatus = QtWidgets.QFrame(self.Bottom)
        self.AutorcrossStatus.setGeometry(QtCore.QRect(290, 60, 49, 7))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AutorcrossStatus.sizePolicy().hasHeightForWidth())
        self.AutorcrossStatus.setSizePolicy(sizePolicy)
        self.AutorcrossStatus.setStyleSheet("QFrame{\n"
"    border-radius: 2px;\n"
"    background-color: rgb(108, 108, 108);\n"
"    background-position: center;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"    background-color: rgb(23, 165, 0);\n"
"}")
        self.AutorcrossStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AutorcrossStatus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AutorcrossStatus.setObjectName("AutorcrossStatus")
        self.SkidpadStatus = QtWidgets.QFrame(self.Bottom)
        self.SkidpadStatus.setGeometry(QtCore.QRect(420, 60, 49, 7))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SkidpadStatus.sizePolicy().hasHeightForWidth())
        self.SkidpadStatus.setSizePolicy(sizePolicy)
        self.SkidpadStatus.setStyleSheet("QFrame{\n"
"    border-radius: 2px;\n"
"    background-color: rgb(108, 108, 108);\n"
"    background-position: center;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"    background-color: rgb(23, 165, 0);\n"
"}")
        self.SkidpadStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SkidpadStatus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SkidpadStatus.setObjectName("SkidpadStatus")
        self.Autocross = QtWidgets.QPushButton(self.Bottom)
        self.Autocross.setGeometry(QtCore.QRect(257, 2, 120, 77))
        self.Autocross.setStyleSheet("font: 900 12pt \"Arial Black\";")
        self.Autocross.setObjectName("Autocross")
        self.EnduranceStatus = QtWidgets.QFrame(self.Bottom)
        self.EnduranceStatus.setGeometry(QtCore.QRect(547, 60, 49, 7))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EnduranceStatus.sizePolicy().hasHeightForWidth())
        self.EnduranceStatus.setSizePolicy(sizePolicy)
        self.EnduranceStatus.setStyleSheet("QFrame{\n"
"    border-radius: 2px;\n"
"    background-color: rgb(108, 108, 108);\n"
"    background-position: center;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"    background-color: rgb(23, 165, 0);\n"
"}")
        self.EnduranceStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.EnduranceStatus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EnduranceStatus.setObjectName("EnduranceStatus")
        self.BrakeStatus = QtWidgets.QFrame(self.Bottom)
        self.BrakeStatus.setGeometry(QtCore.QRect(39, 60, 49, 7))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BrakeStatus.sizePolicy().hasHeightForWidth())
        self.BrakeStatus.setSizePolicy(sizePolicy)
        self.BrakeStatus.setAutoFillBackground(False)
        self.BrakeStatus.setStyleSheet("QFrame{\n"
"    border-radius: 2px;\n"
"    background-color: rgb(108, 108, 108);\n"
"    background-position: center;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"    background-color: rgb(23, 165, 0);\n"
"}")
        self.BrakeStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BrakeStatus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BrakeStatus.setObjectName("BrakeStatus")
        self.Brake = QtWidgets.QPushButton(self.Bottom)
        self.Brake.setGeometry(QtCore.QRect(3, 2, 120, 77))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.Brake.setFont(font)
        self.Brake.setStyleSheet("font: 900 12pt \"Arial Black\";\n"
"background-color: rgb(44, 44, 44);\n"
"\n"
"QPushButton :: hover{\n"
"\n"
"}")
        self.Brake.setObjectName("Brake")
        self.SkidPad = QtWidgets.QPushButton(self.Bottom)
        self.SkidPad.setGeometry(QtCore.QRect(384, 2, 120, 77))
        self.SkidPad.setStyleSheet("font: 900 12pt \"Arial Black\";")
        self.SkidPad.setObjectName("SkidPad")
        self.Acceleration = QtWidgets.QPushButton(self.Bottom)
        self.Acceleration.setGeometry(QtCore.QRect(130, 2, 120, 77))
        self.Acceleration.setStyleSheet("font: 900 12pt \"Arial Black\";")
        self.Acceleration.setAutoDefault(False)
        self.Acceleration.setObjectName("Acceleration")
        self.Endurance = QtWidgets.QPushButton(self.Bottom)
        self.Endurance.setGeometry(QtCore.QRect(511, 2, 120, 77))
        self.Endurance.setStyleSheet("font: 900 12pt \"Arial Black\";")
        self.Endurance.setObjectName("Endurance")
        self.AccelerationStatus = QtWidgets.QFrame(self.Bottom)
        self.AccelerationStatus.setGeometry(QtCore.QRect(163, 60, 49, 7))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccelerationStatus.sizePolicy().hasHeightForWidth())
        self.AccelerationStatus.setSizePolicy(sizePolicy)
        self.AccelerationStatus.setStyleSheet("QFrame{\n"
"    border-radius: 2px;\n"
"    background-color: rgb(108, 108, 108);\n"
"    background-position: center;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"    background-color: rgb(23, 165, 0);\n"
"}")
        self.AccelerationStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AccelerationStatus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AccelerationStatus.setObjectName("AccelerationStatus")
        self.Endurance.raise_()
        self.Acceleration.raise_()
        self.SkidPad.raise_()
        self.Brake.raise_()
        self.Autocross.raise_()
        self.AccelerationStatus.raise_()
        self.AutorcrossStatus.raise_()
        self.BrakeStatus.raise_()
        self.EnduranceStatus.raise_()
        self.SkidpadStatus.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Autocross.setText(_translate("MainWindow", "Autocross"))
        self.Brake.setText(_translate("MainWindow", "Brake"))
        self.SkidPad.setText(_translate("MainWindow", "SkidPad"))
        self.Acceleration.setText(_translate("MainWindow", "Acceleration"))
        self.Endurance.setText(_translate("MainWindow", "Endurance"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
