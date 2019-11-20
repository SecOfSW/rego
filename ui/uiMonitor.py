# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Monitor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Monitor(object):
    def setupUi(self, Monitor):
        Monitor.setObjectName("Monitor")
        Monitor.resize(722, 407)
        self.monitorText = QtWidgets.QTextBrowser(Monitor)
        self.monitorText.setGeometry(QtCore.QRect(25, 21, 671, 321))
        self.monitorText.setObjectName("monitorText")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Monitor)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 350, 351, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonToStart = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonToStart.setObjectName("buttonToStart")
        self.horizontalLayout_2.addWidget(self.buttonToStart)
        self.buttonToSettings = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonToSettings.setObjectName("buttonToSettings")
        self.horizontalLayout_2.addWidget(self.buttonToSettings)

        self.retranslateUi(Monitor)
        QtCore.QMetaObject.connectSlotsByName(Monitor)

    def retranslateUi(self, Monitor):
        _translate = QtCore.QCoreApplication.translate
        Monitor.setWindowTitle(_translate("Monitor", "Monitor"))
        self.buttonToStart.setText(_translate("Monitor", "Start"))
        self.buttonToSettings.setText(_translate("Monitor", "Settings"))
