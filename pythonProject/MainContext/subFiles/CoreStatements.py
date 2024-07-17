from Objects.mainObject import my_Object

# class CoreStatements():
#     def start(self, node):
#         #print("The start items are :", node)
#         #print("Visiting start node:", node.data)
#         for child in node.children:
#             self.visit(child)
#         # if isinstance(items, Tree):
#         #     return self.transform(items.children)
#         # else:
#         #     return items
#
#     def statement(self, node):
#         #print("These are the statement items!!!!", node)
#         for child in node.children:
#             result = self.visit(child)
#         print("Return from st child:", result)
#         print("Finally context values", self.values)
#         return result
#
#     def semicolonstatements(self, node):
#         #print("These are the semicolonstatements items", node)
#         for child in node.children:
#             result = self.visit(child)
#         print("Return from semi child:", result)
#         return result
#
#     def basicstatement(self, node):
#         #print("These are the basicstatement items", node)
#         for child in node.children:
#             result = (self.visit(child))
#         #print("Return from basic statement child:", result)
#         return result

class CoreStatements:
    def start(self, node):
        for child in node.children:
            self.visit(child)

    def statement(self, node):
        for child in node.children:
            result = self.visit(child)
        print("Return from statement child:", result)
        print("Finally context values", self.values)
        return result

    def semicolonstatements(self, node):
        for child in node.children:
            result = self.visit(child)
        print("Return from semicolon statement child:", result)
        return result

    def basicstatement(self, node):
        for child in node.children:
            result = self.visit(child)
        return result