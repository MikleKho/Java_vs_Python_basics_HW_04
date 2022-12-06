# Реализуйте очередь с помощью LinkedList со следующими методами:
# enqueue() - помещает элемент в конец очереди, 
# dequeue() - возвращает первый элемент из очереди и удаляет его, 
# first() - возвращает первый элемент из очереди, не удаляя.

from single_linked_list import *

def main():
    list = SingleLinkedList()
    for i in range(1, 11):
        list.enqueue(i) # ----> помещает элемент в конец очереди

    print("Исходная очередь --->")
    list.print_list()
    print("\n----->")

    element = list.dequeue()
    print(f"Удалили первый элемент ---> {element}") # ---> возвращает первый элемент из очереди и удаляет его
    print("----->")
 
    list.print_list()
    print("\n----->")

    element = list.first()
    print(f"Возвращаем первый элемент без удаления  ---> {element}") # ---> возвращает первый элемент из очереди, не удаляя.
    print("----->")

    list.print_list()
    print("\n----->")

    element = list.dequeue()
    print(f"Удалили первый элемент ---> {element}") # ---> возвращает первый элемент из очереди и удаляет его
    print("----->")

    list.print_list()
    print("\n----->")


if __name__ == '__main__':
    main()
