from indexes import ForwardIndex, InvertedIndex
from pprint import pprint

FORWARD_INDEX = None
INVERTED_INDEX = None

def set_directory():
    global FORWARD_INDEX, INVERTED_INDEX
    ans = input('Enter derectory path where text files will be indexed \
or skip to use default one "sem_9_lab_1/files" :')
    FORWARD_INDEX = ForwardIndex(ans) if ans else ForwardIndex()
    INVERTED_INDEX = InvertedIndex(ans) if ans else InvertedIndex()

def build_indexes():
    if FORWARD_INDEX and INVERTED_INDEX:
        FORWARD_INDEX.build_index()
        INVERTED_INDEX.build_index()
        print('\nIndexes built successfuly\n')
    else:
        print('\nIndex dirrectory not set\n')


def search_using_indexes():
    if FORWARD_INDEX and INVERTED_INDEX:
        ans = input('Enter searcj word: ')
        pprint(f'Forward index search result: {FORWARD_INDEX.search(ans)}')
        pprint(f'Inverted index search result: {INVERTED_INDEX.search(ans)}')
    else:
        print('\nIndex dirrectory not set\n')

def get_indexes_structure():
    if FORWARD_INDEX and INVERTED_INDEX:
        print('Forward index :')
        pprint(FORWARD_INDEX.index)
        pprint('\nInverted index :')
        print(INVERTED_INDEX.index)
    else:
        print('\nIndex dirrectory not set\n')

def main_menue():
    while True:
        print('\nSelect options:')
        print('1. Set dirrectory')
        print('2. Build indexes')
        print('3. Search using indexes')
        print('4. Get indexes structure')
        print('5. Exit\n')
        ans = input()
        match ans:
            case '1':
                set_directory()
            case '2':
                build_indexes()
            case '3':
                search_using_indexes()
            case '4':
                get_indexes_structure()
            case '5':
                break


if __name__ == '__main__':
    main_menue()
