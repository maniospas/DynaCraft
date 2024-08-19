from dynacraft.objects.object import Object


class Functions:
    def object(self):
        return Object({}, types=["object"])

    def print_object(obj, additional_arg=None):
        if additional_arg is not None:
            print("Data:", additional_arg)
            # print("MyLanguageObject:")
            # print("Types:", obj.types)
            # print("All Fields:", obj.get_all_fields())
            # print("Public Fields:", obj.get_public_set())
            # print("Private Fields:", obj.get_private_set())
        else:
            print("No Data")