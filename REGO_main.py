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

import struct
import sys
from binascii import unhexlify
from datetime import datetime, timedelta

import os

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

# Scanning thread used in ScanClass 
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
        self.countSignal.emit("[+] (Scan Finished) Please check 'report.docx'.\n")
        self.doneSignal.emit(True)

# Declare a class for Scan Window        
class ScanClass(QDialog, form_scan):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        # self.buttonToSettings.clicked.connect(self.settingsBtnFunc)
        self.buttonToStart.clicked.connect(self.startBtnFunc)
        
        self.th = ScanWorker()
        self.th.countSignal.connect(self.textUpdate)
        self.th.changeValue.connect(self.progressBar.setValue)
        self.th.doneSignal.connect(self.buttonToStart.setEnabled)

    # def settingsBtnFunc(self):
    #     pass

    # function for Start button
    def startBtnFunc(self):
        self.th.start()
        self.th.working = True
        self.buttonToStart.setDisabled(True)
        self.scanText.clear()

    def textUpdate(self, msg):
        self.scanText.append(msg)
    
# Monitoring thread used in MonitorClass
class MonitorWorker(QThread):
    countSignal = pyqtSignal(str)
    def __init__(self):
        super().__init__()

    def run(self):
        rm = REGO_reg_monitor.REGO_reg_monitor()
        rm.monitor()
        while self.working: # check the values at 5 second intervals
            result = rm.monitor_start()
            self.countSignal.emit(str(result))
            self.sleep(5)

# Declare a class for Monitor Window
class MonitorClass(QDialog, form_monitor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        # self.buttonToSettings.clicked.connect(self.settingsBtnFunc)
        self.buttonToStart.clicked.connect(self.startBtnFunc)
        self.buttonToStart.status = False

        self.th = MonitorWorker()
        self.th.countSignal.connect(self.textUpdate)

    # def settingsBtnFunc(self):
        # pass

    # function for Start button
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

# dumping thread used in DumpClass
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

# diffing thread used in DumpClass
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
        path="./"
        path=os.path.realpath(path)
        os.startfile(path)
        self.doneSignal.emit(True)

# Declare a class for Dump Window
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
        
    # function for DUMP button
    def dumpFunc(self): 
        self.th1.working=True
        self.th1.start()
        self.dumpButton.setDisabled(True)
        self.diffButton.setDisabled(True)
            # show progress GUI while self.th1.working is True
            
    # function for DIFF button
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

# Declare a class for Util Window 
class UtilClass(QDialog, form_util):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.darkmodeButton.clicked.connect(self.darkmodeFunc)
        self.noWinUpdateButton.clicked.connect(self.noWinUpdateFunc)
        self.noWebcamButton.clicked.connect(self.noWebcamFunc)
        self.regeditButton.clicked.connect(self.regeditFunc)
        self.computerInfoButton.clicked.connect(self.computerInfoFunc)
        self.lastShutdownTimeButton.clicked.connect(self.lastShutdownTimeFunc)

        self.noUpdate = False
        r = REGO_reg.REGO_reg()
        try:
            result = r.getReg(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize")
            for r in result:
                if r[0] == 'AppsUseLightTheme':
                    if r[1] == 0:
                        self.darkmodeButton.setText("White Mode")
                        self.dark = True
                    else:
                        self.darkmodeButton.setText("Dark Mode")
                        self.dark = False
        except: 
            self.dark = False
            self.darkmodeButton.setText("Dark Mode")
        
        
        r = REGO_reg.REGO_reg()
        try:
            result = r.getReg(winreg.HKEY_CURRENT_USER, "Software\\Policies\\Microsoft\\Windows\\WindowsUpdate")
            for r in result:
                if r[0] == 'NoAutoUpdate':
                    if r[1] == 0:
                        self.noWinUpdateButton.setText("No Auto Update")
                        self.noUpdate = True
                    else:
                        self.noWinUpdateButton.setText("Auto Update")
                        self.noUpdate = False
        except OSError as e:
            print("AutoWinUpdate registry is NOT FOUND")
            self.noUpdate = False
            self.noWinUpdateButton.setText("Auto Update")
        except Exception as e:
            print("Unexpected Exception")

        
        r = REGO_reg.REGO_reg()
        try:
            result = r.getReg(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\webcam")
            for r in result:
                if r[0] == 'Value':
                    if r[1] == "Deny":
                        self.noWebcamButton.setText("Webcam Enable")
                        self.noWebcam = True
                    else:
                        self.noWebcamButton.setText("Webcam Disable")
                        self.noWebcam = False
        except OSError as e:
            self.noWebcam = False
            self.noWebcamButton.setText("Webcam Disable")
        except Exception as e:
            print("Unexpected Exception")

    # Dark Mode Enable / Disable        
    def darkmodeFunc(self):
        try:
            r = REGO_reg.REGO_reg()
            hKey = r.openHReg(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize")
            # Disable Dark Mode
            if self.dark:
                r.setReg(hKey, "AppsUseLightTheme", REGO_reg.TYPE["REG_DWORD"], 1)
                self.darkmodeButton.setText("Dark Mode")
                self.dark = False
            # Enable Dark Mode
            else:
                r.setReg(hKey, "AppsUseLightTheme", REGO_reg.TYPE["REG_DWORD"], 0)
                self.darkmodeButton.setText("White Mode")
                self.dark = True
            r.closeHReg(hKey)
        except Exception as e:
            print(e)

    # Window AutoUpdate Enable / Disable
    def noWinUpdateFunc(self):
        try:
            r = REGO_reg.REGO_reg()
            hKey = r.openHRegCreate(winreg.HKEY_CURRENT_USER, "Software\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU")

            # Enable autoUpdate
            if self.noUpdate:
                r.setReg(hKey, "NoAutoUpdate", REGO_reg.TYPE["REG_DWORD"], 0)
                self.noWinUpdateButton.setText("No Auto Update")
                self.noUpdate = False
            
            # Disable autoUpdate
            else:
                r.setReg(hKey, "NoAutoUpdate", REGO_reg.TYPE["REG_DWORD"], 1)
                self.noWinUpdateButton.setText("Auto Update")
                self.noUpdate = True
            r.closeHReg(hKey)
        except Exception as e:
            print(e)

    # Webcam Enable / Disable      
    def noWebcamFunc(self):
        try:
            r = REGO_reg.REGO_reg()
            hKey = r.openHReg(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\webcam")

            # Enable webcam
            if self.noWebcam:
                r.setReg(hKey, "Value", REGO_reg.TYPE["REG_SZ"], "Allow")
                self.noWebcamButton.setText("Webcam disable")
                self.noWebcam = False
            
            # Disable Webcam
            else:
                r.setReg(hKey, "Value", REGO_reg.TYPE["REG_SZ"], "Deny")
                self.noWebcamButton.setText("Webcam enable")
                self.noWebcam = True
            r.closeHReg(hKey)
        except Exception as e:
            print(e)

    # Open REGEDIT
    def regeditFunc(self):
        os.system("C:\\Windows\\System32\\regedt32.exe")

    # Show Computer Name
    def computerInfoFunc(self):
        try:
            r = REGO_reg.REGO_reg()
            result = r.getReg(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\ControlSet001\\Control\\ComputerName\\ActiveComputerName")
            for r in result:
                if r[0] == 'ComputerName':
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText(r[1])
                    msg.setWindowTitle("Computer Name")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
        except Exception as e:
            print("Unexpected Exception:", e)

    # Show last Shutdown Time
    def lastShutdownTimeFunc(self):
        time_bin = ""
        try:
            r = REGO_reg.REGO_reg()
            result = r.getReg(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\ControlSet001\\Control\\Windows")
            for r in result:
                if r[0] == 'ShutdownTime':
                    for t in r[1]:
                        print(t)
                        time_bin += hex(t)[2:].zfill(2)
                    print(time_bin)
                    nt_timestamp = struct.unpack("<Q", unhexlify(time_bin))[0]
                    epoch = datetime(1601, 1, 1, 9, 0, 0)
                    nt_datetime = epoch + timedelta(microseconds=nt_timestamp / 10)

        except Exception as e:
            print("Unexpected Exception:", e)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        # msg.setText(nt_datetime.strftime("%c"))
        msg.setText(nt_datetime.strftime("%Y/%m/%d (%A) - %H:%M:%S"))
        msg.setWindowTitle("Last Shutdown Time")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        
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

    # SCAN button PUSHED
    def scanBtnFunc(self):
        self.scan = ScanClass()
        self.scan.exec_()

    # MONITOR button PUSHED
    def monitorBtnFunc(self):
        self.monitor = MonitorClass()
        self.monitor.exec_()

    # DUMP button PUSHED
    def dumpBtnFunc(self):
        self.dump = DumpClass()
        self.dump.exec_()

    # UTIL button PUSHED
    def utilBtnFunc(self):
        self.util = UtilClass()
        self.util.exec_()

if __name__ == '__main__':
    app = QApplication([])
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
