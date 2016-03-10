from util_str import str_split_regext 
from util_smali import type_get_java_type
from util_log import *
from methodt import Methodt
from fieldt import Fieldt

class Classt:
    "represent a java class"
    def __init__(self):
        self.package = None
        self.import_classes = []
        self.modifiers = []
        self.name = None
        self.super_class = None
        self.implements_classes = []
        self.instance_fields = []
        self.static_fileds = []
        self.construct_methods = []
        self.clinit_methods = []
        self.ordinary_methods = []
    def parse(self, file_path):
        file = open(file_path, "r")
        if file is None :
            log_err("<Classt.parse> failed to open file : %s" % (file_path) )
            return False
        lines = file.readlines()
        file.close()
        res = True 
        for line in lines :
            line = line.strip()
            if line == "" :
                res = True
            elif line.startswith(".class") :
                res = self.parse_class(line)
            elif line.startswith(".super") :
                res = self.parse_super(line)
            elif line.startswith(".implements") :
                res = self.parse_implements(line)
            elif line.startswith("#") :
                res = True
            elif line.startswith(".field"):
                res = self.parse_field(line)
            elif line.startswith(".method"):
                res = self.parse_method(line)
            elif line.startswith(".end") or line.startswith(".locals") \
                or line.startswith(".catch") or line.startswith(".catchall") \
                or line.startswith(".sparse-switch") or line.startswith(".annotation") \
                or line.startswith(".packed-switch") or line.startswith(".array-data") \
                or line.startswith(".enum"):
                res = True
            elif line.startswith("."):
                log_debug("<Classt.parse> line = %s" % (line) )
                res = True
            else :
                res = True
            if not res :
                log_err("<Classt.parse> failed to parse line = %s" % (line) )
                return False
        return True
        
    def parse_class(self, line):
        arr = str_split_regext(line, "[ \t]+")
        if len(arr) < 2 :
            log_err("<Classt.parse> failed to parse .class = %s" % (line))
            return False
        modifiers_ = arr[1:len(arr)-1]
        one_type = type_get_java_type(arr[len(arr)-1])
        if one_type is None :
            log_err("<Classt.parse> failed to parse .class = %s" % (line))
            return False
        self.package = one_type["package"]
        self.name = one_type["name"]
        for modifier in modifiers_ :
            #judge
            self.modifiers.append(modifier)
        return True
    
    def parse_super(self, line) :
        arr = str_split_regext(line, "[ \t]+")
        if len(arr) != 2 :
            log_err("<Classt.parse> failed to parse .super = %s" % (line))
            return False
        one_type = type_get_java_type(arr[1])
        if one_type is None :
            log_err("<Classt.parse> failed to parse .super = %s" % (line))
            return False
        self.super_class = one_type["complete"]
        return True
    
    def parse_implements(self, line):
        arr = str_split_regext(line, "[ \t]+")
        if len(arr) != 2 :
            log_err("<Classt.parse> failed to parse .implements = %s" % (line))
            return False
        one_type = type_get_java_type(arr[1])
        if one_type is None :
            log_err("<Classt.parse> failed to parse .implements = %s" % (line))
            return False
        self.implements_classes.append(one_type["complete"])
        return True
        
    def parse_method(self, line) :
        mth = Methodt() 
        if not mth.parse(self, line) :
            log_err("<Classt.parse> failed to parse .method = %s" % (line))
            return False
        if mth.is_init() :
            self.construct_methods.append(mth)
        elif mth.is_clinit() :
            self.clinit_methods.append(mth)
        else :
            self.ordinary_methods.append(mth)
        return True
    
    def parse_field(self, line) :
        fd = Fieldt()
        if not fd.parse(self, line) :
            log_err("<Classt.parse> failed to parse .field = %s" % (line))
            return False
        if fd.is_static() :
            self.static_fileds.append(fd)
        else :
            self.construct_methods.append(fd)
        return True
    
    
    def add_import(self, import_calss):
        self.import_classes.append(import_calss)
    
    def write_to_file(self, dest_file) :
        file = open(dest_file, "w")
        file.close()
        return True
    