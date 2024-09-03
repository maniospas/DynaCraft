from dynacraft.objects.object import Object


class ContextFunctions:
    def __init__(self):
        self.values = {}

    def add(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        print(result[0].types)

        if (result[0].types == ['object', 'string'] or result[1].types == ['object', 'string']):
            add_result_value = str(result[0].get_public_field("value")) + str(result[1].get_public_field("value"))
            add_result = Object({"value": add_result_value}, types=["object", "string"])
        else:
            add_result_value = result[0].get_public_field("value") + result[1].get_public_field("value")
            add_result = Object({"value": add_result_value}, types=["object", "float"])
        print("@@the add res is ", add_result)
        return add_result

    def sub(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        sub_result_value = result[0].get_public_field("value") - result[1].get_public_field("value")
        sub_result = Object({"value": sub_result_value}, types=["object", "float"])
        return sub_result

    def mul(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        mul_result_value = result[0].get_public_field("value") * result[1].get_public_field("value")
        mul_result = Object({"value": mul_result_value}, types=["object", "float"])
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
        print("----pow res", power_result_value)
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
        div_result = Object({"value": div_result_value}, types=["object", "float"])
        return div_result

    def smaller_than(self, node):
        result = []
        for child in node.children:
            result.append(self.visit(child))
        if result[0].get_public_field("value") <= result[1].get_public_field("value"):
            comp_result = Object({"value": 1}, types=["object", "float"])
        else:
            comp_result = Object({"value": 0}, types=["object", "float"])
        return comp_result
