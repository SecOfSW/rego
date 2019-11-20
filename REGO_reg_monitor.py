# 보안 관련 레지스트리 값 변경 시 어떤 프로그램에서 변경했는지 확인 가능한 경우 해당 프로그램 Virustotal 에서 Scan

import time
import REGO_reg
import data
import winreg

"""
# DATA FORMAT FOR MONITORING KEYS
key_dict =
{(HIVE, PATH):
    {
        ATTIRIBUTENAME: String,
        ATTIRIBUTENAME2: String,
        ..
    },
    ..
}

# DATA FORMAT FOR MONITORING ATTRIBUTES
attr_dict = 
{
    (HIVE, PATH, ATTRIBUTENAME): string,
    (HIVE, PATH, ATTRIBUTENAME): string,
    ...
}
"""

# Class for RegMonitor
class REGO_reg_monitor(REGO_reg.REGO_reg):
    def __init__(self):
        # self.key_input = data.mon_reg.key_input
        self.key_input = [(winreg.HKEY_CURRENT_USER, 'TestValue')]
        # self.attr_input = data.mon_reg.attr_input
        self.attr_input = [(winreg.HKEY_CURRENT_USER, 'TestValue', 'asdf')]

    def monitor(self):
        # INITIALIZE key_dict
        self.key_dict = {}
        for _ in self.key_input:
            attr_dict = {}
            HIVE = _[0]
            PATH = _[1]
            try:
                a_list = self.getReg(HIVE, PATH)
            except:
                continue
            for __ in a_list:
                attr_dict[__[0]] = __[1]
            self.key_dict[(HIVE, PATH)] = attr_dict
    
        # INITIALIZE attr_dict
        self.attr_dict = {}
        for _ in self.attr_input:
            HIVE = _[0]
            PATH = _[1]
            ATTRIBUTENAME = _[2]
            try:
                a_list = self.getReg(HIVE, PATH)
            except:
                continue
            for __ in a_list:
                if __[0] == ATTRIBUTENAME:
                    self.attr_dict[(HIVE, PATH, ATTRIBUTENAME)] = __[1]
                    break

    def monitor_start(self):
        output = ""
        # monitoring start 
        # Key Check
        for _ in self.key_input:
            HIVE = _[0]
            PATH = _[1]
            try:
                attr_dict = self.key_dict[(HIVE, PATH)]
                attributeList = self.getReg(HIVE, PATH)
            except:
                continue
            for __ in attributeList:
                output += "{0}\\{1}\\{2}\t".format(HIVE, PATH, __[0])
                if __[0] not in attr_dict.keys():
                    output += "{0}\tNEW!\n".format(__[1])
                elif __[1] != attr_dict[__[0]]:
                    output += "{0}\tModified!\n".format(__[1])
                else:
                    output += "{0}\n".format(__[1])
            
        # Attr Check
        for _ in self.attr_input:
            HIVE = _[0]
            PATH = _[1]
            ATTRIBUTENAME = _[2]
            try:
                attributeList = self.getReg(HIVE, PATH)
            except:
                continue
            output += "{0}\\{1}\\{2}\t".format(HIVE, PATH, ATTRIBUTENAME)
            for __ in attributeList:
                if __[0] == ATTRIBUTENAME:
                    if __[1] != self.attr_dict[(HIVE, PATH, ATTRIBUTENAME)]:
                        output += "{0}\tModified!\n".format(__[1])
                    else:
                        output += "{0}\n".format(__[1])
    
        print()
        return output
