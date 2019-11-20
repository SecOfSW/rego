import winreg
import REGO_reg
import data

# JSON file format
"""
[
    {
        "HIVE": string,
        "PATH": string,
        "TYPE": string,
        "VULN_VAL": list,
        "SAFE_VAL": list
    }
]
"""

MAX_NUM = 100000
class REGO_reg_scan(REGO_reg.REGO_reg):
    def __init__(self):
        pass
    
    def scan(self):
        # Information of registries with vulnerable value
        scan_result = []
        for i, m in zip(range(MAX_NUM),data.sec_reg.reg_info_list):
            HIVE = m.HIVE
            PATH = m.PATH
            ATTRIBUTE = m.ATTRIBUTE
            VULN_VAL = m.VULN_VAL
            SAFE_VAL = m.SAFE_VAL
            DESC = m.DESC
            
            attList = []
            try:
                attList =  self.getReg(HIVE=HIVE, PATH=PATH)
            except Exception as e:
                print("[{0}] {1:130} - NOT found".format(str(i), REGO_reg.hiveIntToStr(HIVE)+"\\"+str(PATH)+"\\"+str(ATTRIBUTE)))
                continue

            for _ in attList:
                if _[0] == ATTRIBUTE:
                    print("[{0}] {1:130} - <CURRENT_VAL>: {2:>10}, <SAFE_VAL>: {3:>10}, <VULN_VAL>: {4:>10}, <DESC>: {5}".format(str(i), REGO_reg.hiveIntToStr(HIVE)+"\\"+str(PATH)+"\\"+str(ATTRIBUTE), _[1], str(SAFE_VAL), str(VULN_VAL), DESC)) 
                    if _[1] not in SAFE_VAL:
                        scan_result.append({
                                            "HIVE": REGO_reg.hiveIntToStr(HIVE), 
                                            "PATH": PATH, 
                                            "ATTRIBUTE": ATTRIBUTE,
                                            "CURRENT_VALUE": _[1],
                                            "SAFE_VALUE": SAFE_VAL
                                            })
                    break
        return scan_result
        