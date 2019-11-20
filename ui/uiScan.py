# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Scan.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Scan(object):
    def setupUi(self, Scan):
        Scan.setObjectName("Scan")
        Scan.resize(721, 370)
        self.scanText = QtWidgets.QTextBrowser(Scan)
        self.scanText.setGeometry(QtCore.QRect(25, 21, 671, 281))
        self.scanText.setObjectName("scanText")
        self.progressBar = QtWidgets.QProgressBar(Scan)
        self.progressBar.setGeometry(QtCore.QRect(30, 320, 451, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Scan)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(490, 310, 201, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonToSettings = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonToSettings.setObjectName("buttonToSettings")
        self.horizontalLayout_2.addWidget(self.buttonToSettings)
        self.buttonToStart = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonToStart.setObjectName("buttonToStart")
        self.horizontalLayout_2.addWidget(self.buttonToStart)

        self.retranslateUi(Scan)
        QtCore.QMetaObject.connectSlotsByName(Scan)

    def retranslateUi(self, Scan):
        _translate = QtCore.QCoreApplication.translate
        Scan.setWindowTitle(_translate("Scan", "Scan"))
        self.buttonToSettings.setText(_translate("Scan", "Settings"))
        self.buttonToStart.setText(_translate("Scan", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Scan = QtWidgets.QDialog()
    ui = Ui_Scan()
    ui.setupUi(Scan)
    Scan.show()
    sys.exit(app.exec_())
