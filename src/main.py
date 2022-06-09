from interpreter import Interpreter
from parser import Parser
from tokenizer import Tokenizer

def main():
    while True:
        try:
            text = input('> ')
            if text == 'exit':
                exit(0)

            tokenizer = Tokenizer(text)
            tokens = tokenizer.generate_tokens()

            parser = Parser(tokens)
            ast = parser.parse()
            if not ast:
                continue

            interpreter = Interpreter()
            value = interpreter.visit(ast)
            print(value)
        except Exception as ex:
            print(ex)

if __name__ == '__main__':
    main()