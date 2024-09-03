class ContextCore:
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