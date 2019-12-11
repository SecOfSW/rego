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

# Key to be monitored (Modification check + Attribute Addition check))   ex) Autoruns
key_input = [(HIVE, PATH), ..]

# Attribute to be monitored (Modification check)
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

# Data for Scanning
class reg_scan_data:
    def __init__(self):
        self.reg_info_list = []
     
    # add registry and its corresponding safe/vulnerable value
    def add_reg(self, NAME, HIVE, PATH, ATTRIBUTE, TYPE, VULN_VAL, SAFE_VAL, DESC):
        r = self.reg_info(NAME, HIVE, PATH, ATTRIBUTE, TYPE, VULN_VAL, SAFE_VAL, DESC)
        self.reg_info_list.append(r)
    
    # Registry Information
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

# Data for Monitoring
class reg_monitor_data:
    def __init__(self):
        self.key_input = []
        self.attr_input = []

    # add key to be monitored
    def add_key(self, HIVE, PATH):
        tup = (HIVE, PATH)
        self.key_input.append(tup)
    
    # add attribute to be monitored
    def add_attr(self, HIVE, PATH, ATTRIBUTENAME):
        tup = (HIVE, PATH, ATTRIBUTENAME)
        self.attr_input.append(tup)
