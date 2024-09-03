from dynacraft.objects.object import Object


def object():
    return Object({}, types=["object"])


sysprint = print
def print(obj = None):
    if obj is not None:
        if "string" in obj.types:
            sysprint(obj.fields["value"])
        else:
            sysprint("Non-string object:", obj)
    else:
        sysprint("")