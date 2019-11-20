# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dump.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dump(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(680, 380)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 661, 361))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dumpButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dumpButton.sizePolicy().hasHeightForWidth())
        self.dumpButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(50)
        self.dumpButton.setFont(font)
        self.dumpButton.setObjectName("dumpButton")
        self.horizontalLayout.addWidget(self.dumpButton)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dumpDir1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dumpDir1.sizePolicy().hasHeightForWidth())
        self.dumpDir1.setSizePolicy(sizePolicy)
        self.dumpDir1.setObjectName("dumpDir1")
        self.horizontalLayout_2.addWidget(self.dumpDir1)
        self.dumpDirButton1 = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dumpDirButton1.sizePolicy().hasHeightForWidth())
        self.dumpDirButton1.setSizePolicy(sizePolicy)
        self.dumpDirButton1.setObjectName("dumpDirButton1")
        self.horizontalLayout_2.addWidget(self.dumpDirButton1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dumpDir2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dumpDir2.sizePolicy().hasHeightForWidth())
        self.dumpDir2.setSizePolicy(sizePolicy)
        self.dumpDir2.setObjectName("dumpDir2")
        self.horizontalLayout_3.addWidget(self.dumpDir2)
        self.dumpDirButton2 = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dumpDirButton2.sizePolicy().hasHeightForWidth())
        self.dumpDirButton2.setSizePolicy(sizePolicy)
        self.dumpDirButton2.setObjectName("dumpDirButton2")
        self.horizontalLayout_3.addWidget(self.dumpDirButton2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.diffButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diffButton.sizePolicy().hasHeightForWidth())
        self.diffButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(50)
        self.diffButton.setFont(font)
        self.diffButton.setObjectName("diffButton")
        self.verticalLayout_2.addWidget(self.diffButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dump"))
        self.dumpButton.setText(_translate("Dialog", "DUMP"))
        self.dumpDirButton1.setText(_translate("Dialog", "..."))
        self.dumpDirButton2.setText(_translate("Dialog", "..."))
        self.diffButton.setText(_translate("Dialog", "DIFF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dump()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
