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

<TYPE INFORMATION>:  
    0 REG_NONE
    1 REG_SZ
    2 REG_EXPAND_SZ
    3 REG_BINARY
    4 REG_DWORD   
    (https://ko.wikipedia.org/wiki/%EC%9C%88%EB%8F%84%EC%9A%B0_%EB%A0%88%EC%A7%80%EC%8A%A4%ED%8A%B8%EB%A6%AC)
"""

from data.REGO_data import *
from winreg import HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, HKEY_USERS

# d = reg_data()
# d.add_reg("a", "a", "a", "a", "a", "a")
# for m in d.reg_info_list:
#     print(m.HIVE)

__all__ = ['REGO_data']

sec_reg = reg_scan_data()
mon_reg = reg_monitor_data()

# WEBCAM SHOULD BE TURNED OFF
sec_reg.add_reg(NAME="WEBCAM",
                HIVE=HKEY_LOCAL_MACHINE, 
                PATH="SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\webcam", 
                ATTRIBUTE="Value", 
                TYPE=REG_SZ, 
                VULN_VAL=["Allow"], 
                SAFE_VAL=["Deny"],
                DESC="webcam should be turned off"
                )

# FILE_EXT SHOULD BE REVEALED
sec_reg.add_reg(NAME="FILE_EXT",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\\Folder\\HideFileExt",
                ATTRIBUTE="CheckedValue",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="fileExt should be revealed"
                )

sec_reg.add_reg(NAME="TEST",
                HIVE=HKEY_LOCAL_MACHINE,
                PATH="Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\\FakeSubkeyToTest",
                ATTRIBUTE="CheckedValue",
                TYPE=REG_DWORD,
                VULN_VAL=[0x0],
                SAFE_VAL=[0x1],
                DESC="fake key to test exception"
                )
                
#################################################################################################
# TEST
# test_reg = reg_scan_data()

# # WEBCAM SHOULD BE TURNED OFF
# test_reg.add_reg(NAME="TEST2",
#                 HIVE=HKEY_LOCAL_MACHINE, 
#                 PATH="SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\webcam", 
#                 ATTRIBUTE="Value", 
#                 TYPE=REG_SZ, 
#                 VULN_VAL=["Allow"], 
#                 SAFE_VAL=["Deny"],
#                 DESC="webcam should be turned off"
#                 )