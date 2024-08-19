class ContextCore:
    def start(self, node):
        for child in node.children:
            self.visit(child)

    def statement(self, node):
        for child in node.children:
            result = self.visit(child)
        return result

    def semicolonstatements(self, node):
        for child in node.children:
            result = self.visit(child)
        return result

    def basicstatement(self, node):
        for child in node.children:
            result = self.visit(child)
        return result