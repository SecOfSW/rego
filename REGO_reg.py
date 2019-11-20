import winreg
import sys
import time

HKEYS = dict()
HKEYS[winreg.HKEY_CLASSES_ROOT]     = "HKEY_CLASSES_ROOT"
HKEYS[winreg.HKEY_CURRENT_CONFIG]   = "HKEY_CURRENT_CONFIG"
HKEYS[winreg.HKEY_CURRENT_USER]     = "HKEY_CURRENT_USER"
HKEYS[winreg.HKEY_DYN_DATA]         = "HKEY_DYN_DATA"
HKEYS[winreg.HKEY_LOCAL_MACHINE]    = "HKEY_LOCAL_MACHINE"
HKEYS[winreg.HKEY_PERFORMANCE_DATA] = "HKEY_PERFORMANCE_DATA"
HKEYS[winreg.HKEY_USERS]            = "HKEY_USERS"

TYPE = dict()
TYPE["REG_NONE"]        = 0
TYPE["REG_SZ"]          = 1
TYPE["REG_EXPAND_SZ"]   = 2
TYPE["REG_BINARY"]      = 3
TYPE["REG_DWORD"]       = 4

def hiveIntToStr(hive: int):
    return HKEYS[hive]
    
class REGO_reg:
    def __init__(self):
        pass
    
    # Reg Path                          : Open Reg Handle
    def openHReg(self, HIVE, PATH):
        hKey = winreg.OpenKey(HIVE, PATH, access=winreg.KEY_ALL_ACCESS)
        return hKey

    # Reg Handle                        : Close Reg Handle  
    def closeHReg(self, hkey):
        winreg.CloseKey(hkey)

    # Reg Path, reg_type, new Val       : Set Reg Value
    def setReg(self, hKey, attribute, reg_type, val):
        winreg.SetValueEx(hKey, attribute, 0, reg_type, val)

    # Terminal Reg Path                 : Get Reg Value; PATH is terminal node
    def getReg(self, HIVE, PATH):
        # TODO: Check if Path is valid
        enumList = []
        hKey = self.openHReg(HIVE, PATH)  
        i = 0
        while True:
            try:
                enumList.append(winreg.EnumValue(hKey, i))
            except WindowsError:
                break
            except Exception as e:
                raise e
            i += 1
        self.closeHReg(hKey)
        return enumList    

def main():
    net = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\NetworkList\\Signatures\\Unmanaged\\010103000F0000F0080000000F0000F02BED9341AD1485616F15353D478CADC49839964D214C847CDF7E2169C693E7BD"
    reg = REGO_reg()
    keyList = reg.getReg(winreg.HKEY_LOCAL_MACHINE, net)
    print(keyList)    

    test = "Software\\TEST"
    reg = REGO_reg()
    keyList = reg.getReg(winreg.HKEY_CURRENT_USER, test)
    print(keyList)

    # reg.setReg(winreg.HKEY_CURRENT_USER, "TestValue", 1, 2)
    # keyList = reg.getReg(winreg.HKEY_CURRENT_USER, test)
    # print(keyList)

    hKey = reg.openHReg(winreg.HKEY_CURRENT_USER, test)
    while True:
        enumList = []
        i = 0
        while True:
            try:
                enumList.append(winreg.EnumValue(hKey, i))
            except WindowsError:
                break
            except Exception as e:
                print("[-] getReg():", e)
                sys.exit(-1)
            i += 1
        print(1, enumList)
        time.sleep(1)
        
# if __name__ =='__main__':
#     main()
