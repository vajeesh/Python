from interface import Interface          # import Interface class from interface module

class Main:                      # Main class is created

    def __init__(self):
        pass

    def main(self):              # Method created to reun the menu from interface module
        Interface.menu()

if __name__ == '__main__':
    Main().main()

