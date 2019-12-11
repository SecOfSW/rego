import winreg
import sys
import time

# Dictionary for HIVE value
HKEYS = dict()
HKEYS[winreg.HKEY_CLASSES_ROOT]     = "HKEY_CLASSES_ROOT"
HKEYS[winreg.HKEY_CURRENT_CONFIG]   = "HKEY_CURRENT_CONFIG"
HKEYS[winreg.HKEY_CURRENT_USER]     = "HKEY_CURRENT_USER"
HKEYS[winreg.HKEY_DYN_DATA]         = "HKEY_DYN_DATA"
HKEYS[winreg.HKEY_LOCAL_MACHINE]    = "HKEY_LOCAL_MACHINE"
HKEYS[winreg.HKEY_PERFORMANCE_DATA] = "HKEY_PERFORMANCE_DATA"
HKEYS[winreg.HKEY_USERS]            = "HKEY_USERS"

# Dictionary for TYPE value
TYPE = dict()
TYPE["REG_NONE"]        = 0
TYPE["REG_SZ"]          = 1
TYPE["REG_EXPAND_SZ"]   = 2
TYPE["REG_BINARY"]      = 3
TYPE["REG_DWORD"]       = 4

# HIVE value to String
def hiveIntToStr(hive: int):
    return HKEYS[hive]
    
class REGO_reg:
    def __init__(self):
        pass
    
    # Reg Path                          : Open Reg Handle
    def openHReg(self, HIVE, PATH):
        hKey = winreg.OpenKey(HIVE, PATH, access=winreg.KEY_ALL_ACCESS)
        return hKey

    # Reg Path                          : Open Reg Handle (if exists)
    #                                   :  Create Reg and Open Handle (else)
    def openHRegCreate(self, HIVE, PATH):
        hkey = winreg.CreateKeyEx(HIVE, PATH, access=winreg.KEY_ALL_ACCESS)
        return hkey

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
