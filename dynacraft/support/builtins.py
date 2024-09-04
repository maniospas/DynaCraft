from dynacraft.objects.object import Object


def object():
    return Object({}, types=["object"])


sysprint = print
def print(obj = None):
    sysprint("the obj is", obj)
    if obj is not None:
        if "string" in obj.types or "float" in obj.types or "int" in obj.types or "bool" in obj.types:
            sysprint(obj.fields["value"])
        else:
            sysprint("Non-builtin object:", obj)
    else:
        sysprint("")


def _create_string_object(value):
    sysprint("creating string obj")
    return Object({"value": value}, types=["object", "string"])


def tostring(obj = None):
    sysprint("into to string built in", obj)
    if obj is not None:
        sysprint("obj not none")
        if "string" in obj.types or "float" in obj.types or "int" in obj.types or "bool" in obj.types:
            sysprint("obj is string")
            temp = _create_string_object(obj.fields["value"])
            print(temp)

            return temp
        else:
            return _create_string_object("Non-builtin object:"+str(obj))
    else:
        return _create_string_object("")
