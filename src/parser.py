from token import Type
from nodes import *

class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = iter(tokens)
        self.next_token()

    def next_token(self):
        try:
            self.current = next(self.tokens)
        except:
            self.current = None

    def parse(self):
        if self.current == None:
            return None

        result = self.expr()

        if self.current != None:
            raise Exception("Invalid Token")

        return result

    def expr(self):
        result = self.term()

        while self.current != None and self.current.type in (Type.PLUS, Type.MINUS):
            if self.current.type == Type.PLUS:
                self.next_token()
                result = AddNode(result, self.term())
            if self.current.type == Type.MINUS:
                self.next_token()
                result = SubNode(result, self.term())

        return result

    def term(self):
        result = self.factor()

        while self.current != None and self.current.type in (Type.MULTIPLY, Type.DIVIDE):
            if self.current.type == Type.MULTIPLY:
                self.next_token()
                result = MulNode(result, self.factor())
            if self.current.type == Type.DIVIDE:
                self.next_token()
                result = DivNode(result, self.factor())

        return result

    def factor(self):
        token = self.current

        if token.type == Type.LPAREN:
            self.next_token()
            result = self.expr()

            if self.current.type != Type.RPAREN:
                raise Exception("RPAREN not found")

            self.next_token()
            return result

        elif token.type == Type.NUMBER:
            self.next_token()
            return NumberNode(token.value)

        elif token.type == Type.PLUS:
            self.next_token()
            return PlusNode(token.factor())

        elif token.type == Type.MINUS:
            self.next_token()
            return MinusNode(token.factor())

        raise Exception("Something went wrong while parsing")