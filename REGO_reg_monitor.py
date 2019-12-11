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
        # self.key_input = []
        # self.attr_input = []

        self.key_input = data.mon_reg.key_input
        self.attr_input = data.mon_reg.attr_input

    # INITIALIZE key_dict & attr_dict before monitoring starts
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

    # Start Monitoring 
    def monitor_start(self):
        output = ""
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
                output += "[*] HIVE : {0}\nPATH : {1}\\{2}\n".format(REGO_reg.hiveIntToStr(HIVE), PATH, __[0])
                # if new key is ADDED
                if __[0] not in attr_dict.keys():
                    output += "VALUE : {0}\t****NEW****\n\n".format(__[1])
                # elif key is MODIFIED
                elif __[1] != attr_dict[__[0]]:
                    output += "VALUE : {0}\t****Modified****\n\n".format(__[1])
                # else (DEFAULT)
                else:
                    output += "VALUE : {0}\n\n".format(__[1])
            
        # Attr Check
        for _ in self.attr_input:
            HIVE = _[0]
            PATH = _[1]
            ATTRIBUTENAME = _[2]
            try:
                attributeList = self.getReg(HIVE, PATH)
            except:
                continue
            output += "[*] HIVE : {0}\nPATH : {1}\\{2}\n".format(REGO_reg.hiveIntToStr(HIVE), PATH, ATTRIBUTENAME)
            for __ in attributeList:
                if __[0] == ATTRIBUTENAME:
                    # if attribute is MODIFIED
                    if __[1] != self.attr_dict[(HIVE, PATH, ATTRIBUTENAME)]:
                        output += "VALUE : {0}\t****Modified****\n\n".format(__[1])
                    # else (DEFAULT)
                    else:
                        output += "VALUE : {0}\n\n".format(__[1])
        return output
