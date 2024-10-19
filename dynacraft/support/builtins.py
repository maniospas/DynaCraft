from dynacraft.objects.object import Object


def object():
    return Object({}, types=["object"], original_types = [])


sysprint = print
def print(obj = None):
    #sysprint("the obj is", obj)
    if obj is not None:
        sysprint("obj", obj)
        if "string" in obj.types or "float" in obj.types or "int" in obj.types or "bool" in obj.types:
            sysprint(obj.public_fields["value"])
        else:
            sysprint("Non-builtin object:", obj)
    else:
        sysprint("")


def custom_assert(obj = None):
    if obj is not None:
        if "bool" in obj.types:
            if obj.value == "false":
                sysprint("Faulty conditon")
            elif obj.value == "true":
                return
            else :
                raise Exception("Invalid condition datatype")
        else:
            raise Exception ("Invalid condition datatype")
    else:
        raise Exception ("Non type condition")

def _create_string_object(value):
    return Object({"value": value}, types=["object", "string"])


def tostring(obj = None):
    if obj is not None:
        if "string" in obj.types or "float" in obj.types or "int" in obj.types or "bool" in obj.types:
            return _create_string_object(obj.fields["value"])
        else:
            return _create_string_object("Non-builtin object:"+str(obj))
    else:
        return _create_string_object("")
