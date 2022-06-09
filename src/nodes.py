class NumberNode:
    def __init__(self, value: any) -> None:
        self.value = value

class AddNode:
    def __init__(self, a: any, b: any) -> None:
        self.a = a
        self.b = b

class SubNode:
    def __init__(self, a: any, b: any) -> None:
        self.a = a
        self.b = b

class MulNode:
    def __init__(self, a: any, b: any) -> None:
        self.a = a
        self.b = b

class DivNode:
    def __init__(self, a: any, b: any) -> None:
        self.a = a
        self.b = b

class PlusNode:
    def __init__(self, node: any) -> None:
        self.node = node

class MinusNode:
    def __init__(self, node: any) -> None:
        self.node = node