import re

def strify(obj):
        if type(obj) is int:
            return str(obj)
        elif type(obj) is str:
            return "'" + obj + "'"
        else:
            return str(obj)
        

def valid_id(string):
    reg = re.compile('(A-Za-z0-9)*')
    return bool(reg.match(string))