from object import Object


class BoolObject(Object):
    def __init__(self, bool_value):
        super().__init__(fields={"value": bool_value}, types=["object", "bool"])
