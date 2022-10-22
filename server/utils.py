def strify(obj):
        if type(obj) is int:
            return str(obj)
        elif type(obj) is str:
            return "'" + obj + "'"
        else:
            return str(obj)