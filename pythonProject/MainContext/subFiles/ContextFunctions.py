from Objects.mainObject import my_Object
# class ContextFunctions():
#     def add(self, node):
#         #print("add are", node)
#         result = []
#         for child in node.children:
#             #print("The add child is", child)
#             result.append(self.visit(child))
#         #print("The add result is", result)
#         add_result_value = result[0].value + result[1].value
#         add_result = my_Object({"value": add_result_value}, types=["object", "float"])
#         return add_result
#     def sub(self, node):
#         #print("sub are", node)
#         result = []
#         for child in node.children:
#             #print("The sub child is", child)
#             result.append(self.visit(child))
#         #print("The sub result is", result)
#         sub_result_value = result[0].value - result[1].value
#         sub_result = my_Object({"value": sub_result_value}, types=["object", "float"])
#         #print("The sub return", sub_result)
#         return sub_result
#
#     def mul(self, node):
#         #print("mul are", node)
#         result = []
#         for child in node.children:
#             #print("The mul child is", child)
#             result.append(self.visit(child))
#         #print("The mul result is", result)
#         mul_result_value = result[0].value * result[1].value
#         mul_result = my_Object({"value": mul_result_value}, types=["object", "float"])
#         return mul_result
#
#     def div(self, node):
#         #print("div are", node)
#         result = []
#         for child in node.children:
#             #print("The div child is", child)
#             result.append(self.visit(child))
#         #print("The div result is", result)
#         if result[1] == 0:
#             raise ValueError("Division by zero")
#         div_result_value = result[0].value / result[1].value
#         div_result = my_Object({"value": div_result_value}, types=["object", "float"])
#         return div_result
#
#     def smaller_than(self, node):
#         print("smaller than nodes", self.values)
#         result = []
#         for child in node.children:
#             result.append(self.visit(child))
#             #print("result", result)
#             #print("The div child is", child)
#         #print(result[0].value)
#         #print(result[1].value)
#         if result[0].value <= result[1].value :
#             comp_result = my_Object({"value": 1}, types=["object", "float"])
#         else :
#             comp_result = my_Object({"value": 0}, types=["object", "float"])
#         return comp_result

class ContextFunctions:
    def __init__(self):
        self.values = {}

    def add(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        add_result_value = result[0].get_public_field("value") + result[1].get_public_field("value")
        add_result = my_Object({"value": add_result_value}, types=["object", "float"])
        return add_result

    def sub(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        sub_result_value = result[0].get_public_field("value") - result[1].get_public_field("value")
        sub_result = my_Object({"value": sub_result_value}, types=["object", "float"])
        return sub_result

    def mul(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        mul_result_value = result[0].get_public_field("value") * result[1].get_public_field("value")
        mul_result = my_Object({"value": mul_result_value}, types=["object", "float"])
        return mul_result

    def div(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        if result[1].get_public_field("value") == 0:
            raise ValueError("Division by zero")
        div_result_value = result[0].get_public_field("value") / result[1].get_public_field("value")
        div_result = my_Object({"value": div_result_value}, types=["object", "float"])
        return div_result

    def smaller_than(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        if result[0].get_public_field("value") <= result[1].get_public_field("value"):
            comp_result = my_Object({"value": 1}, types=["object", "float"])
        else:
            comp_result = my_Object({"value": 0}, types=["object", "float"])
        return comp_result

    def visit(self, node):
        # This method simulates visiting a node in a parsed tree and should be implemented based on your tree structure
        return node
