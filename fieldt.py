
from util_str import str_split_regext
from util_smali import type_get_java_type
from util_log import *

class Fieldt :
    "represent a java field"
    def __init__(self):
        self.line = None
        self.modifiers = []
        self.type = None
        self.name = None
        self.value = None
    def parse(self, classt, line):
        arr = str_split_regext(line, "[ \t]+")
        arr_len = len(arr)
        if arr is None or arr_len < 2:
           return False
        if arr[0] != '.field' :
           return False
        if arr.count("=") > 0 :
            sig = arr[arr.index("=")-1]
            self.value = arr[arr.index("=")+1]
        else :
            sig = arr[arr_len-1]
        modifiers = arr[1:arr_len-1]
        for modifier in modifiers:
            #judge
            self.modifiers.append(modifier)
        name_type_arr = str_split_regext(sig, ":")
        if len(name_type_arr) != 2 :
            return False
        self.name = name_type_arr[0]
        one_type = type_get_java_type(name_type_arr[1])
        if one_type is None :
            return False
        if one_type["system"] and not one_type["base"] :
            #add import
            classt.add_import(one_type["complete"]);
            self.type = one_type["name"]
        elif one_type["system"] and one_type["base"] :
            self.type = one_type["name"]
        else :
            self.type = one_type["complete"]
        return True
    def is_static(self):
        return self.modifiers.count("static") > 0