
from util_str import str_split_regext 
from util_log import *
from util_smali import type_get_java_type, parse_params, judge_if_rest_modifier

class Methodt :
    "represent a java method"
    def __init__(self):
        self.line = None
        self.modifiers = []
        self.return_type = None
        self.name = None
        self.params = []
        self.is_abstract = False
        self.is_native = False
        self.cls = None
    def parse(self, classt, line):
        self.cls = classt
        arr = str_split_regext(line, "[ \t]+")
        if arr is None or len(arr) < 2 :
            return False
        if arr[0] != ".method" :
            return False
        sig = arr[len(arr)-1]
        modifiers = arr[1:len(arr)-1]
        for modifier in modifiers : 
            if modifier == 'native' :
                self.is_native = True
            if modifier == 'abstract' :
                self.is_abstract = True
            #judge
            if not judge_if_rest_modifier(modifier) :
                self.modifiers.append(modifier)
        sig_index0 = sig.find("(")
        sig_index1 = sig.find(")")
        if -1 == sig_index0 or -1 == sig_index1 :
            return False
        name = sig[:sig_index0]
        paramss = sig[sig_index0+1:sig_index1]
        return_value = sig[sig_index1+1:]
        return_type = type_get_java_type(return_value)
        
        self.name = name
        if return_type is None :
            return False
        if return_type["system"] and not return_type["base"] :
            #add import
            classt.add_import(return_type["complete"]);
            self.return_type = return_type["name"]
        elif return_type["system"] and return_type["base"] :
            self.return_type = return_type["name"]
        else :
            self.return_type = return_type["complete"]
        
        if paramss is not None and paramss != '' :
            params_types = parse_params(paramss)
            i = 0
            if params_types is not None :
                for one_param_type in params_types:
                    if one_param_type["system"]  and not one_param_type["base"]:
                        classt.add_import(one_param_type["complete"])
                        self.params.append({"type":one_param_type["name"], "name": "a%s%d" % (one_param_type["name"], i) })
                    else :
                        self.params.append({"type":one_param_type["complete"], "name": "a%s%d" % (one_param_type["name"], i) })
        return True
    
    def is_init(self) :
        return self.name == "<init>"
    
    def is_clinit(self) :
        return self.name == "<clinit>"
    
    def write_to_file(self, file) :
        file.write("\t")
        if self.name != '<clinit>' :
            if len(self.modifiers) > 0 :
                for modifier in self.modifiers :
                    file.write("%s " % (modifier) )
            if self.name == '<init>' :
                file.write("%s(" % (self.cls.get_name()) )
            else :
                file.write("%s %s(" % (self.return_type, self.name) )
            if len(self.params) > 0 :
                i = 0
                for param in self.params :
                    if i == len(self.params)-1 :
                        file.write("%s %s" % (param["type"], param["name"]) )
                    else :
                        file.write("%s %s, " % (param["type"], param["name"]) )
                    i = i + 1
            file.write(")")
            if self.is_abstract or self.is_native :
                file.write(";\n")
            else :
                file.write("{\n\t}\n")
        else :
            file.write("static{\n\t}\n")
        
        return True
        