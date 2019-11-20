import winreg
import datetime
import json
import jsondiff
import pprint
import REGO_reg

hive1 = winreg.HKEY_LOCAL_MACHINE
hive2 = winreg.HKEY_CURRENT_USER
hive3 = winreg.HKEY_USERS

class REGO_reg_dump:
    def DUMP_AT_ONCE(self): 
        cur_time = str(datetime.datetime.now()).split()
        FNAME = cur_time[0] + '-' + '-'.join(cur_time[1].split('.')[0].split(':'))
        
        self.dumpDict = {}
        reg = REGO_reg.REGO_reg()
        print("[+] DUMP START!!")
        # self.DFS_HIVE_SEARCH(reg, hive1, "")
        # print("[+] HIVE1 FINISHED!!")
        self.DFS_HIVE_SEARCH(reg, hive2, "")
        print("[+] HKCU FINISHED!!")
        self.DFS_HIVE_SEARCH(reg, hive3, "")
        with open(FNAME + ".dump", "w", encoding="utf-8") as f:
            json.dump(self.dumpDict, f, indent=4)
        print("[+] HKU FINISHED!!")
        print("[+] DUMP FINISHED!!")

    def DFS_HIVE_SEARCH(self, REG, HIVE, PATH):
        try:
            hKey = REG.openHReg(HIVE, PATH)
        except Exception as e:
            # print("[-] no Permission!")
            return

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
                    self.dumpDict[inputString] = value
                    # inputString = "\t\"{0}\\{1}\\{2}\"\t:\t\"{3}\",\r\n".format(REGO_reg.hiveIntToStr(HIVE), PATH, attribute[0], value)
                    # H_FILE.write(inputString)
                    # H_FILE.write("\r\n[{0}\\{1}]\t{2}\t{3}\r\n".format(REGO_reg.hiveIntToStr(HIVE), PATH, attribute[0], attribute[1]))
            except Exception as e:
                break
            i += 1
        
        REG.closeHReg(hKey)
        
        for _ in keyList:
            newPath = PATH
            if PATH != "":
                newPath += "\\"
            newPath += _
            self.DFS_HIVE_SEARCH(REG, HIVE, newPath)

    def makeDiff(self, f_before, f_after):
        json_1 = None
        json_2 = None
        try:
            with open(f_before, 'r', encoding='utf-8', errors='ignore') as j1:
                json_1 = json.load(j1)
            with open(f_after, 'r', encoding='utf-8', errors='ignore') as j2:
                json_2 = json.load(j2)
        except ValueError as e:
            raise e
        
        d = jsondiff.diff(json_1, json_2)
        
        with open('reg.diff', 'w', encoding='utf-8') as out:
            pprint.pprint(d, stream=out)

        print("DIFF FINISHED!!")
        return d
