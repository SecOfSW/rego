import winreg
import datetime
import json
import jsondiff
import pprint
import REGO_reg

# HIVE Value: HKLM, HKCU, HKU
hive1 = winreg.HKEY_LOCAL_MACHINE
hive2 = winreg.HKEY_CURRENT_USER
hive3 = winreg.HKEY_USERS

class REGO_reg_dump:
    # DUMP HKCU, HKU
    def DUMP_AT_ONCE(self): 
        # Get current time to make unique file name
        cur_time = str(datetime.datetime.now()).split()
        FNAME = cur_time[0] + '-' + '-'.join(cur_time[1].split('.')[0].split(':'))
        
        self.dumpDict = {}
        reg = REGO_reg.REGO_reg()
        print("[+] DUMP START!!")
        
        # DUMP HKCU
        self.DFS_HIVE_SEARCH(reg, hive2, "")
        print("[+] HKCU FINISHED!!")

        # DUMP HKU
        self.DFS_HIVE_SEARCH(reg, hive3, "")
        print("[+] HKU FINISHED!!")

        # Save the result to `cur_time`.dump file
        with open(FNAME + ".dump", "w", encoding="utf-8") as f:
            json.dump(self.dumpDict, f, indent=4)
        print("[+] DUMP FINISHED!!")

    # Depth-First Search HIVE
    def DFS_HIVE_SEARCH(self, REG, HIVE, PATH):
        # In case of No permission, pass
        try:
            hKey = REG.openHReg(HIVE, PATH)
        except Exception as e:
            # print("[-] no Permission!")
            return

        # List of keys that belongs to HIVE/PATH
        keyList = []
        i = 0
        while True:
            try:
                keyList.append(winreg.EnumKey(hKey, i))
            except:
                break
            i += 1
        
        i = 0
        while True:
            try:
                attribute = winreg.EnumValue(hKey, i)
                if attribute[0]:
                    value = attribute[1]
                    if type(attribute[1]) == bytes:
                        value = value.hex()
                    inputString = "{0}\\{1}\\{2}".format(REGO_reg.hiveIntToStr(HIVE), PATH, attribute[0])
                    # Get the value of all attribute
                    # HIVE/PATH/Attribute: VALUE
                    self.dumpDict[inputString] = value
            except Exception as e:
                break
            i += 1
        REG.closeHReg(hKey)
        
        # Recursive Search all keys underneath
        for _ in keyList:
            newPath = PATH
            if PATH != "":
                newPath += "\\"
            newPath += _
            self.DFS_HIVE_SEARCH(REG, HIVE, newPath)

    # make diff file "reg.diff" with f_before & f_after
    def makeDiff(self, f_before, f_after):
        json_1 = None
        json_2 = None
        try:
            with open(f_before, 'r', encoding='utf-8', errors='ignore') as j1:
                json_1 = json.load(j1)
            with open(f_after, 'r', encoding='utf-8', errors='ignore') as j2:
                json_2 = json.load(j2)
        # if it's NOT json format or INVALID json format
        except ValueError as e:
            raise e
        except Exception as e:
            raise e 

        # jsondiff two files       
        d = jsondiff.diff(json_1, json_2)

        # write the result to "reg.diff" in current directory
        with open('reg.diff', 'w', encoding='utf-8') as out:
            pprint.pprint(d, stream=out)
        print("DIFF FINISHED!!")
        return d
