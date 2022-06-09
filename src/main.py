def main():
    while True:
        try:
            text = input('> ')
            if text == 'exit':
                exit(0)
                
        except Exception as ex:
            print(ex)

if __name__ == '__main__':
    main()