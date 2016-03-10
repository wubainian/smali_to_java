import os
import sys
from util_log import *
from classt import Classt
from util_str import str_split_regext

input_dir="C:\\Users\\vsnake\\Desktop\\bird\\Flappy_Bird_v1_3\\smali"
dest_dir="src"
    
def mkdirs(dst_dir_name, file_full_path):
    if not os.path.exists(dst_dir_name):
        os.mkdir(dst_dir_name)
    
    relative_path = file_full_path[len(input_dir)+1:] 
    arr = relative_path.split(os.sep) 
    arr = arr[:-1]
    for dir_name in arr :
        dst_dir_name = dst_dir_name + os.sep + dir_name
        if not os.path.exists(dst_dir_name):
            os.mkdir(dst_dir_name)
    return dst_dir_name

for cur_dir, dirs, files in os.walk( input_dir ):
    is_should_break = False
    for file in files:
        file_full_path = "%s%s%s" % (cur_dir, os.sep, file)
        #parse
        cls = Classt()
        res = cls.parse(file_full_path)
        if not res :
            log_err("<main> failed to parse file : %s" % (file_full_path) )
            is_should_break = True
            break
        #dir
        dst_dir = mkdirs(dest_dir, file_full_path)
        dest_file = "%s%s%s" % (dst_dir, os.sep, file)
        #write
        cls.write_to_file(dest_file)
    if is_should_break :
        break