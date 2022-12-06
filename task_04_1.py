# Пусть дан LinkedList с несколькими элементами. Реализуйте метод, который вернет “перевернутый” список.

from single_linked_list import *

def main():
    list = SingleLinkedList()
    for i in range(1, 11):
        list.insert_at_end(i)
    list.insert_at_start(0)

    list.print_list()
    print("\n----->")

    list.reverse_list()

    list.print_list()
    print("\n<-----")

if __name__ == '__main__':
    main()