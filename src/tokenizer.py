from token import Token, Type

class Tokenizer:
    def __init__(self, text) -> None:
        self.text = iter(text)
        self.next_char()

    def next_char(self):
        try:
            self.current = next(self.text)
        except:
            self.current = None

    def generate_tokens(self):
        while self.current != None:
            if self.current_char in ' \n\t':
                self.advance()
            elif self.current_char == '.' or self.current_char in '0123456789':
                yield self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(Type.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(Type.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(Type.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(Type.DIVIDE)
            elif self.current_char == '(':
                self.advance()
                yield Token(Type.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(Type.RPAREN)
            else:
                raise Exception(f"Illegal character '{self.current_char}'")

    def generate_number(self):
        decimal_point_count = 0
        number_str = self.current_char
        self.advance()

        while self.current_char != None and (self.current_char == '.' or self.current_char in '0123456789'):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.current_char
            self.advance()

        if number_str.startswith('.'):
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str += '0'

        return Token(Type.NUMBER, float(number_str))
