from Objects.mainObject import my_Object

class Functions: ## Name_build_ins
    # Define a generic print function
    # Define a generic print function

    # def object(self):
    #     print("Creating object")
    #     return my_Object({}, types=["object"])
    #
    # def print_object(obj, additional_arg=None):
    #     # print("MyLanguageObject:")
    #     # if isinstance(obj, my_Object):
    #     #     # Handle printing for MyLanguageObject
    #     #     print("MyLanguageObject:")
    #     #     print("Data:", obj)
    #     # else:
    #     #     # Handle printing for other types of objects
    #     #     print("Unsupported object type:", type(obj))
    #     if additional_arg is not None:
    #         print("Data:", additional_arg)
    #     else :
    #         print("No Data")

    def object(self):
        print("Creating object")
        return my_Object({}, types=["object"])

    # def create_object(fields=None, types=None):
    #     if fields is None and types is None:
    #         print("Creating default object")
    #         return my_Object()
    #     else:
    #         print("Creating object with specified fields and types")
    #         return my_Object(fields=fields, types=types)

    # Function to print details of an object
    def print_object(obj, additional_arg=None):
        # if isinstance(obj, my_Object):
        #     print("MyLanguageObject:")
        #     print("Types:", obj.types)
        #     print("All Fields:", obj.get_all_fields())
        #     print("Public Fields:", obj.get_public_set())
        #     print("Private Fields:", obj.get_private_set())
        # else:
        #     print("Unsupported object type:", type(obj))

        if additional_arg is not None:
            print("Data:", additional_arg)
            # print("MyLanguageObject:")
            # print("Types:", obj.types)
            # print("All Fields:", obj.get_all_fields())
            # print("Public Fields:", obj.get_public_set())
            # print("Private Fields:", obj.get_private_set())
        else:
            print("No Data")