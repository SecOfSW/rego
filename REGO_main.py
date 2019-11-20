import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import time
import winreg
import REGO_reg_monitor
import REGO_reg_scan
import REGO_dump
import REGO_reg

import ui.uiDump
import ui.uiMain
import ui.uiMonitor
import ui.uiScan
import ui.uiUtil
"""
    1. 데이터 선별해서 넣기 
    2. 검사 기능 
    3. 모니터링 기능    - 비교 기준값 결정해야함
    (4). 레지스트리를 어떤 프로그램이 변경하고자 하는지 확인가능한가
    5. 잡동사니(유틸)
    -3. GUI 기본적인 구현               https://wikidocs.net/35485
    -2. 레지스트리 덤프/디프 (regipy)   https://pypi.org/project/regipy/
    -1. PPT 만들기
    --. 사용자 정의 감시 목록

"""

# load UI file
# form_main = uic.loadUiType("ui/Main.ui")[0]
# form_scan = uic.loadUiType("ui/Scan.ui")[0]
# form_monitor = uic.loadUiType("ui/Monitor.ui")[0]
# form_dump = uic.loadUiType("ui/Dump.ui")[0]
# form_util = uic.loadUiType("ui/Utility.ui")[0]
form_main = ui.uiMain.Ui_Main
form_scan = ui.uiScan.Ui_Scan
form_monitor = ui.uiMonitor.Ui_Monitor
form_dump = ui.uiDump.Ui_Dump
form_util = ui.uiUtil.Ui_Util

class ScanWorker(QThread):
    changeValue = pyqtSignal(int)
    countSignal = pyqtSignal(str)
    doneSignal = pyqtSignal(bool)
    def __init__(self):
        super().__init__()

    def run(self):
        self.changeValue.emit(0)
        rs = REGO_reg_scan.REGO_reg_scan()
        result = rs.scan()
        # print(result)
        i = 0
        for d in result:
            i += 1            
            for k in d:
                self.countSignal.emit("{}:{}".format(str(k), str(d[k])))
            self.countSignal.emit("\n")
            self.changeValue.emit(int(i * 100 / len(result)))
        self.countSignal.emit("Scan Finished\n")
        self.doneSignal.emit(True)
        
class ScanClass(QDialog, form_scan):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.buttonToSettings.clicked.connect(self.settingsBtnFunc)
        self.buttonToStart.clicked.connect(self.startBtnFunc)
        
        self.th = ScanWorker()
        self.th.countSignal.connect(self.textUpdate)
        self.th.changeValue.connect(self.progressBar.setValue)
        self.th.doneSignal.connect(self.buttonToStart.setEnabled)

    def settingsBtnFunc(self):
        pass

    def startBtnFunc(self):
        self.th.start()
        self.th.working = True
        self.buttonToStart.setDisabled(True)
        self.scanText.clear()

    def textUpdate(self, msg):
        self.scanText.append(msg)
    
class MonitorWorker(QThread):
    countSignal = pyqtSignal(str)
    def __init__(self):
        super().__init__()

    def run(self):
        rm = REGO_reg_monitor.REGO_reg_monitor()
        rm.monitor()
        while self.working:
            result = rm.monitor_start()
            self.countSignal.emit(str(result))
            self.sleep(5)

class MonitorClass(QDialog, form_monitor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.buttonToSettings.clicked.connect(self.settingsBtnFunc)
        self.buttonToStart.clicked.connect(self.startBtnFunc)
        self.buttonToStart.status = False

        self.th = MonitorWorker()
        self.th.countSignal.connect(self.textUpdate)

    def settingsBtnFunc(self):
        pass
        # print("setting button clicked")

    def startBtnFunc(self):
        if self.buttonToStart.status:
            self.th.terminate()
            self.th.working = False
            self.buttonToStart.setText('Start')
            self.buttonToStart.status = False
        else:
            self.th.start()
            self.th.working = True
            self.buttonToStart.setText('Stop')
            self.buttonToStart.status = True

    def textUpdate(self, msg):
        self.monitorText.setText(msg)

class DumpWorker(QThread):
    doneSignal = pyqtSignal(bool)
    def __init__(self):
        super().__init__()
        self.working = False

    def run(self):
        rd = REGO_dump.REGO_reg_dump()
        try:
            rd.DUMP_AT_ONCE()
        except Exception as e:
            print(e)
        self.working = False
        self.doneSignal.emit(True)

class DiffWorker(QThread):
    doneSignal = pyqtSignal(bool)
    errorSignal = pyqtSignal(Exception)
    def __init__(self):
        super().__init__()
        self.file1 = ""
        self.file2 = ""
        self.working = False

    def run(self):
        rd = REGO_dump.REGO_reg_dump()
        try:
            rd.makeDiff(self.file1, self.file2)
        except Exception as e:
            self.working = False
            self.errorSignal.emit(e)
            self.doneSignal.emit(True)
            return

        self.working = False
        os.system("explorer.exe reg.diff")
        self.doneSignal.emit(True)

class DumpClass(QDialog, form_dump):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.dumpDir1.setReadOnly(True)
        self.dumpDir2.setReadOnly(True)

        self.dumpDirButton1.clicked.connect(self.dirFunc1)
        self.dumpDirButton2.clicked.connect(self.dirFunc2)

        self.dumpButton.clicked.connect(self.dumpFunc)
        self.diffButton.clicked.connect(self.diffFunc)
        
        self.th1 = DumpWorker()
        self.th1.doneSignal.connect(self.dumpButton.setEnabled)
        self.th1.doneSignal.connect(self.diffButton.setEnabled)

        self.th2 = DiffWorker()
        self.th2.doneSignal.connect(self.diffButton.setEnabled)
        self.th2.doneSignal.connect(self.dumpButton.setEnabled)
        self.th2.errorSignal.connect(self.errorFunc)
        
    def dumpFunc(self): 
        self.th1.working=True
        self.th1.start()
        self.dumpButton.setDisabled(True)
        self.diffButton.setDisabled(True)
            # show progress GUI while self.th1.working is True
            
    def diffFunc(self):
        file1 = self.dumpDir1.text()
        file2 = self.dumpDir2.text()
        print("file1", file1)
        print("file2", file2)

        if not (os.path.isfile(file1) and os.path.isfile(file2)):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("File path is invalid!")
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

        self.th2.file1 = file1
        self.th2.file2 = file2
        self.th2.working = True
        self.th2.start()
        self.dumpButton.setDisabled(True)
        self.diffButton.setDisabled(True)
        # show progress GUI while self.th2.working is True
        
    def errorFunc(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("File is not in a json form!")
        msg.setWindowTitle("FILE FORMAT ERROR")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def dirFunc1(self):
        dir1 = QFileDialog.getOpenFileName(self, "Open Dump", "./", "DUMP Files (*.dump)")
        self.dumpDir1.setText(dir1[0])

    def dirFunc2(self):
        dir2 = QFileDialog.getOpenFileName(self, "Open Dump", "./", "DUMP Files (*.dump)")
        self.dumpDir2.setText(dir2[0])
    
class UtilClass(QDialog, form_util):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.darkmodeButton.clicked.connect(self.darkmodeFunc)
        self.noWinUpdateButton.clicked.connect(self.noWinUpdateFunc)
        self.noWebcamButton.clicked.connect(self.noWebcamFunc)
        self.systemTimeButton.clicked.connect(self.systemTimeFunc)
        self.computerInfoButton.clicked.connect(self.computerInfoFunc)
        self.userInfoButton.clicked.connect(self.userInfoFunc)

        r = REGO_reg.REGO_reg()
        result = r.getReg(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")

        for r in result:
            if r[0] == 'AppsUseLightTheme':
                if r[1] == 0:
                    self.darkmodeButton.setText("White Mode")
                    self.dark = True
                else:
                    self.darkmodeButton.setText("Dark Mode")
                    self.dark = False
            

    def darkmodeFunc(self):
        try:
            r = REGO_reg.REGO_reg()
            hKey = r.openHReg(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            if self.dark:
                r.setReg(hKey, "AppsUseLightTheme", REGO_reg.TYPE["REG_DWORD"], 1)
                self.darkmodeButton.setText("Dark Mode")
                self.dark = False
            else:
                r.setReg(hKey, "AppsUseLightTheme", REGO_reg.TYPE["REG_DWORD"], 0)
                self.darkmodeButton.setText("White Mode")
                self.dark = True
            r.closeHReg(hKey)
        except Exception as e:
            print(e)

    def noWinUpdateFunc(self):
        pass
        
    def noWebcamFunc(self):
        pass
        
    def systemTimeFunc(self):
        pass

    def computerInfoFunc(self):
        pass

    def userInfoFunc(self):
        pass

# Declare a class for Main Window
class WindowClass(QMainWindow, form_main):
    def __init__(self, parent=None):
        super(WindowClass, self).__init__(parent=parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        # Connect each button to corresponding function
        self.buttonToScan.clicked.connect(self.scanBtnFunc)
        self.buttonToMonitor.clicked.connect(self.monitorBtnFunc)
        self.buttonToDump.clicked.connect(self.dumpBtnFunc)
        self.buttonToUtil.clicked.connect(self.utilBtnFunc)

    def scanBtnFunc(self):
        # self.setEnabled(False)
        # self.scan.show()
        self.scan = ScanClass()
        self.scan.exec_()
        # print("btn_1 Clicked")

    def monitorBtnFunc(self):
        self.monitor = MonitorClass()
        self.monitor.exec_()
        # print("btn_2 Clicked")

    def dumpBtnFunc(self):
        self.dump = DumpClass()
        self.dump.exec_()
        # print("btn_3 Clicked")

    def utilBtnFunc(self):
        self.util = UtilClass()
        self.util.exec_()
        # print("btn_4 Clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
