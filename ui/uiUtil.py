# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Utility.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Util(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(741, 501)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 741, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.gridLayout.setSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.noWinUpdateButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noWinUpdateButton.sizePolicy().hasHeightForWidth())
        self.noWinUpdateButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.noWinUpdateButton.setFont(font)
        self.noWinUpdateButton.setObjectName("noWinUpdateButton")
        self.gridLayout.addWidget(self.noWinUpdateButton, 0, 1, 1, 1)
        self.noWebcamButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noWebcamButton.sizePolicy().hasHeightForWidth())
        self.noWebcamButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.noWebcamButton.setFont(font)
        self.noWebcamButton.setObjectName("noWebcamButton")
        self.gridLayout.addWidget(self.noWebcamButton, 1, 0, 1, 1)
        self.regeditButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regeditButton.sizePolicy().hasHeightForWidth())
        self.regeditButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.regeditButton.setFont(font)
        self.regeditButton.setObjectName("regeditButton")
        self.gridLayout.addWidget(self.regeditButton, 1, 1, 1, 1)
        self.darkmodeButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.darkmodeButton.sizePolicy().hasHeightForWidth())
        self.darkmodeButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.darkmodeButton.setFont(font)
        self.darkmodeButton.setObjectName("darkmodeButton")
        self.gridLayout.addWidget(self.darkmodeButton, 0, 0, 1, 1)
        self.computerInfoButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.computerInfoButton.sizePolicy().hasHeightForWidth())
        self.computerInfoButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.computerInfoButton.setFont(font)
        self.computerInfoButton.setObjectName("computerInfoButton")
        self.gridLayout.addWidget(self.computerInfoButton, 2, 0, 1, 1)
        self.lastShutdownTimeButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastShutdownTimeButton.sizePolicy().hasHeightForWidth())
        self.lastShutdownTimeButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lastShutdownTimeButton.setFont(font)
        self.lastShutdownTimeButton.setObjectName("lastShutdownTimeButton")
        self.gridLayout.addWidget(self.lastShutdownTimeButton, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Utility"))
        self.noWinUpdateButton.setText(_translate("Dialog", "No Auto Update"))
        self.noWebcamButton.setText(_translate("Dialog", "No Webcam"))
        self.regeditButton.setText(_translate("Dialog", "RegEdit"))
        self.darkmodeButton.setText(_translate("Dialog", "Dark Mode"))
        self.computerInfoButton.setText(_translate("Dialog", "Computer Info"))
        self.lastShutdownTimeButton.setText(_translate("Dialog", "Last off Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Util()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
