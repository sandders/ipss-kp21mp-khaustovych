forvard_index = None
reversed_index = None

def build_indexes():
    raise NotImplementedError()

def search_using_indexes():
    raise NotImplementedError()

def get_indexes_structure():
    raise NotImplementedError()

def main_menue():
    while True:
        print('Select options:')
        print('1. Build indexes')
        print('2. Search using indexes')
        print('3. Get indexes structure')
        print('4. Exit\n')
        ans = input()
        match ans:
            case '1':
                build_indexes()
            case '2':
                search_using_indexes()
            case '3':
                pass
            case '4':
                break





if __name__ == '__main__':
    main_menue()
