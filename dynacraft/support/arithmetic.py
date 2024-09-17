from dynacraft.objects.object import Object


class ContextFunctions:
    def __init__(self):
        self.values = {}

    def add(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        ##print(result[0].types)

        if (result[0].types == ['object', 'string'] or result[1].types == ['object', 'string']):
            add_result_value = str(result[0].get_public_field("value")) + str(result[1].get_public_field("value"))
            add_result = Object({"value": add_result_value}, types=["object", "string"])
        elif (result[0].types == ['object', 'float'] or result[1].types == ['object', 'float']):
            add_result_value = result[0].get_public_field("value") + result[1].get_public_field("value")
            add_result = Object({"value": add_result_value}, types=["object", "float"])
        else:
            add_result_value = result[0].get_public_field("value") + result[1].get_public_field("value")
            add_result = Object({"value": add_result_value}, types=["object", "int"])
        ##print("@@the add res is ", add_result)
        return add_result

    def sub(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        if (result[0].types == ['object', 'float'] or result[1].types == ['object', 'float']):
            sub_result_value = result[0].get_public_field("value") - result[1].get_public_field("value")
            sub_result = Object({"value": sub_result_value}, types=["object", "float"])
        else:
            sub_result_value = result[0].get_public_field("value") - result[1].get_public_field("value")
            sub_result = Object({"value": sub_result_value}, types=["object", "int"])
        return sub_result

    def mul(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        if (result[0].types == ['object', 'float'] or result[1].types == ['object', 'float']):
            mul_result_value = result[0].get_public_field("value") * result[1].get_public_field("value")
            mul_result = Object({"value": mul_result_value}, types=["object", "float"])
        else:
            mul_result_value = result[0].get_public_field("value") * result[1].get_public_field("value")
            mul_result = Object({"value": mul_result_value}, types=["object", "int"])
        return mul_result

    def power(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))

        # Retrieve the values from the visited children
        base_value = result[0].get_public_field("value")  # First value is the base
        exponent_value = result[1].get_public_field("value")  # Second value is the exponent

        # Calculate the power (base raised to the exponent)
        power_result_value = base_value ** exponent_value
        #print("----pow res", power_result_value)
        # Create the result object with the calculated value
        power_result = Object({"value": power_result_value}, types=["object", "float"])

        return power_result

    def div(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        if result[1].get_public_field("value") == 0:
            raise ValueError("Division by zero")
        div_result_value = result[0].get_public_field("value") / result[1].get_public_field("value")
        if isinstance(div_result_value, int):
            div_result = Object({"value": div_result_value}, types=["object", "int"])
        else:
            div_result = Object({"value": div_result_value}, types=["object", "float"])
        return div_result

    def smaller_equal_than(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        if result[0].get_public_field("value") <= result[1].get_public_field("value"):
            comp_result = Object({"value": 'true'}, types=["object", "bool"])
        else:
            comp_result = Object({"value": 'false'}, types=["object", "bool"])
        return comp_result

    def smaller_than(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        if result[0].get_public_field("value") < result[1].get_public_field("value"):
            comp_result = Object({"value": 'true'}, types=["object", "bool"])
        else:
            comp_result = Object({"value": 'false'}, types=["object", "bool"])
        return comp_result


    def bigger_equal_than(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        if result[0].get_public_field("value") >= result[1].get_public_field("value"):
            comp_result = Object({"value": 'true'}, types=["object", "bool"])
        else:
            comp_result = Object({"value": 'false'}, types=["object", "bool"])
        return comp_result

    def bigger_than(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        if result[0].get_public_field("value") > result[1].get_public_field("value"):
            comp_result = Object({"value": 'true'}, types=["object", "bool"])
        else:
            comp_result = Object({"value": 'false'}, types=["object", "bool"])
        return comp_result

    def equal(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        if result[0].get_public_field("value") == result[1].get_public_field("value"):
            comp_result = Object({"value": 'true'}, types=["object", "bool"])
        else:
            comp_result = Object({"value": 'false'}, types=["object", "bool"])
        return comp_result

    def not_equal(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        if result[0].get_public_field("value") != result[1].get_public_field("value"):
            comp_result = Object({"value": 'true'}, types=["object", "bool"])
        else:
            comp_result = Object({"value": 'false'}, types=["object", "bool"])
        return comp_result