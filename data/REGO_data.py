"""
# DATA FORMAT FOR SCANNING
[
    {
        (HIVE, PATH):
            {
                "TYPE": string,
                "VULN_VAL": string,
                "SAFE_VAL": string
            }
    },
    ...
]

# 감시하고자 하는 Key (변경 확인 + attribute 추가 여부 확인))   ex) Autoruns
key_input = [(HIVE, PATH), ..]

# 감시하고자 하는 Attribute (변경 확인)
attr_input = [(HIVE, PATH, ATTRIBUTENAME), ..]
"""

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

REG_NONE        = 0
REG_SZ          = 1
REG_EXPAND_SZ   = 2
REG_BINARY      = 3
REG_DWORD       = 4

# Data for scanning
class reg_scan_data:
    def __init__(self):
        self.reg_info_list = []
    
    # def add_reg(self, reg_info):
    #     self.reg_list.append(reg_info)
    
    def add_reg(self, NAME, HIVE, PATH, ATTRIBUTE, TYPE, VULN_VAL, SAFE_VAL, DESC):
        r = self.reg_info(NAME, HIVE, PATH, ATTRIBUTE, TYPE, VULN_VAL, SAFE_VAL, DESC)
        self.reg_info_list.append(r)

    class reg_info:
        def __init__(self, NAME, HIVE, PATH, ATTRIBUTE, TYPE, VULN_VAL: list, SAFE_VAL: list, DESC):
            self.NAME = NAME
            self.HIVE = HIVE
            self.PATH = PATH
            self.ATTRIBUTE = ATTRIBUTE
            self.TYPE = TYPE
            self.VULN_VAL = VULN_VAL
            self.SAFE_VAL = SAFE_VAL
            self.DESC = DESC
        def __repr__(self):
            return str(self.__dict__)

class reg_monitor_data:
    def __init__(self):
        self.key_input = []
        self.attr_input = []

    def add_key(self, HIVE, PATH):
        tup = (HIVE, PATH)
        self.key_input.append(tup)
    
    def add_attr(self, HIVE, PATH, ATTRIBUTENAME):
        tup = (HIVE, PATH, ATTRIBUTENAME)
        self.attr_input.append(tup)
    
    

