from util_str import str_split_regext 
from util_smali import type_get_java_type, judge_if_rest_modifier
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
            if not judge_if_rest_modifier(modifier) :
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
        if one_type["system"] and not one_type["base"] :
            #add import
            self.add_import(one_type["complete"]);
            self.super_class = one_type["name"]
        else :
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
        if one_type["system"] and not one_type["base"] :
            #add import
            self.add_import(one_type["complete"]);
            self.implements_classes.append(one_type["name"])
        else :
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
            self.instance_fields.append(fd)
        return True
    
    
    def add_import(self, import_calss):
        if not import_calss.startswith("java.lang.") and 0 == self.import_classes.count(import_calss):
            self.import_classes.append(import_calss)
    def get_name(self):
        return self.name
    
    def write_to_file(self, dest_file) :
        file = open(dest_file, "w")
        
        #package
        file.write("package %s\n" % (self.package) )
        file.write("\n")
        
        #import
        for import_class in self.import_classes :
            file.write( "import %s;\n" % (import_class) )
        if len(self.import_classes) > 0 :
            file.write("\n")
        
        #class
        for modifier in self.modifiers :
            file.write("%s " % (modifier) )
        file.write("class ")
        file.write(self.name)
        if self.super_class is not None and self.super_class != 'java.lang.Object' \
            and self.super_class != 'Object':
            file.write(" extends %s" % (self.super_class) )
        if len(self.implements_classes) > 0 :
            file.write(" implements")
            i=0
            for implements_class in self.implements_classes :
                if i != len(self.implements_classes)-1:
                    file.write(" %s," % (implements_class) )
                else :
                    file.write(" %s" % (implements_class) )
        file.write("{\n")
        
        #instance field
        if len(self.instance_fields) > 0 :
            file.write("\t//instance field\n")
            for field in self.instance_fields :
                field.write_to_file(file)
            file.write("\n")
        
        #static field
        if len(self.static_fileds) > 0 :
            file.write("\t//static field\n")
            for field in self.static_fileds :
                field.write_to_file(file)
            file.write("\n")
        
        #clinit method
        if len(self.clinit_methods) > 0 :
            file.write("\t//clinit method\n")
            for mth in self.clinit_methods :
                mth.write_to_file(file)
            file.write("\n")
        
        #init method
        if len(self.construct_methods) > 0 :
            file.write("\t//init method\n")
            for mth in self.construct_methods :
                mth.write_to_file(file)
            file.write("\n")
        
        #ordinary method
        if len(self.ordinary_methods) > 0 :
            file.write("\t//ordinary method\n")
            for mth in self.ordinary_methods :
                mth.write_to_file(file)
            file.write("\n")
        
        #end
        file.write("}\n")
        file.write("\n")
        
        file.close()
        return True
    