
import re
from util_log import *

def str_split_regext(line, regtext):
    return re.split(regtext, line)