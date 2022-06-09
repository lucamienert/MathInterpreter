from values import Number

class Interpreter:
    def __init__(self) -> None:
        pass

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)
		
    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.a).value + self.visit(node.b).value)

    def visit_SubNode(self, node):
        return Number(self.visit(node.a).value - self.visit(node.b).value)

    def visit_MulNode(self, node):
        return Number(self.visit(node.a).value * self.visit(node.b).value)

    def visit_DivNode(self, node):
        try:
            return Number(self.visit(node.a).value / self.visit(node.b).value)
        except:
            raise Exception("Runtime math error")