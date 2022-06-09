from tokenizer import Tokenizer

def main():
    while True:
        try:
            text = input('> ')
            if text == 'exit':
                exit(0)

            tokenizer = Tokenizer(text)
            tokens = tokenizer.generate_tokens()

        except Exception as ex:
            print(ex)

if __name__ == '__main__':
    main()