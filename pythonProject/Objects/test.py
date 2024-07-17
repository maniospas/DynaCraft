class my_Object:
    def __init__(self, fields, types):
        self.types = types
        self.fields = fields

    def __str__(self):
        #otan kanw print to object na mou leei tupe kai fieltds
        return "this is an object"

x = my_Object({"w": 5}, types=["object", "float"])

print(x)