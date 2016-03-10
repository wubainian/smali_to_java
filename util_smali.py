
from util_log import *

smali_types_maps = {'B':'byte', 'S':'short', 'I':'int', 'J':'long', 'F':'float', 'D':'double', 'Z':'boolean', 'C':'char', 'V':'void'}

def get_type_identify(is_system, is_base):
    return {"system":is_system, "base": is_base, "package":None, "name":None, "complete":None}

def judge_if_smali_class(type):
    if None == type or 'L' != type[0] or ';' != type[len(type)-1] :
        return False
    return True

def judge_if_system_class(java_type):
    if java_type.startswith("java.") or java_type.startswith("javax.") :
        return True
    return False

def typeclass_smali_to_java(smali_type): 
    if not judge_if_smali_class(smali_type) :
        return None
    java_type = smali_type.replace("/", ".")
    java_type = java_type[1:len(java_type)-1]
    return java_type

def typeclass_get_java_class(smali_type):
    ret = get_type_identify(False, False)
    java_type = typeclass_smali_to_java(smali_type)
    if java_type is None :
        log_err("<typeclass_get_java_class> failed to get java type : %s" % (smali_type) )
        return None
    if judge_if_system_class(java_type) == True :
        ret["system"] = True
    ret["complete"] = java_type
    if -1 == java_type.rfind(".") :
        ret["package"] = ""
        ret["name"] = java_type
    else :
        ret["package"] = java_type[:java_type.rfind(".")]
        ret["name"] = java_type[java_type.rfind(".")+1:]
    return ret

def type_get_java_type(smali_type):
    ret = get_type_identify(True, True)
    if smali_types_maps.has_key(smali_type) : 
        ret["name"] = smali_types_maps[smali_type]
        ret["complete"] = smali_types_maps[smali_type]
    elif 'L' == smali_type[0]:
        ret = typeclass_get_java_class(smali_type)
    else :
        arr_count = 0
        i = 0
        while '[' == smali_type[i]: 
            arr_count = arr_count + 1
            i = i + 1
        j = 0
        arr_sufix=""
        while j < arr_count :
            arr_sufix = arr_sufix + "[]"
            j = j + 1
        if arr_count == 0 :
            log_err("<type_get_java_type> failed to parse array : %s" %(smali_type) )
            return None
        ret = type_get_java_type(smali_type[i:])
        ret["system"] = False
        ret["base"] = False
        ret["complete"] = arr_sufix + ret["complete"]
    return ret

def parse_params(smali_types):
    ret = []
    types_len = len(smali_types)
    i = 0
    while i < types_len :
        one_type = None
        if smali_types_maps.has_key(smali_types[i]) : 
            one_type = type_get_java_type(smali_types[i])
            if one_type is None :
                log_err("<parse_params> failed to parse base type : %s" % (smali_types[i]) )
                return None
            i = i + 1
        elif 'L' == smali_types[i]:
            index = smali_types.find(";", i)
            if -1 == index :
                log_err("<parse_params> failed to parse class type : %s" % (smali_types[i:]) )
            one_type = type_get_java_type(smali_types[i:index+1])
            if one_type is None :
                log_err("<parse_params> failed to parse class type : %s" % (smali_types[i:]) )
                return None
            i = index + 1
        else :
            start_index = i
            end_index = -1
            while '[' == smali_types[i] :
                i = i+1
            if 'L' == smali_types[i] :
                index = smali_types.find(";", i)
                if -1 == index :
                    log_err("<parse_params> failed to parse array type : %s" % (smali_types[start_index:]) )
                    return None
                end_index = index
            else :
                end_index = i
            one_type = type_get_java_type(smali_types[start_index:end_index+1])
            if one_type is None :
                log_err("<parse_params> failed to parse array type : %s" % (smali_types[i:]) )
                return None
            i = end_index +1
        ret.append(one_type)
    return ret
