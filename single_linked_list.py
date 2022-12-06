class Node:
    def __init__(self, value=None):
        self.data_value = value
        self.next_value = None

class SingleLinkedList:
    def __init__(self):
        self.head_link = None

    def insert_at_start(self, value):
        new_node = Node(value)
        new_node.next_value = self.head_link
        self.head_link = new_node

    def enqueue(self, value): # enqueue() - помещает элемент в конец очереди,
        new_node = Node(value)
        new_node.next_value = self.head_link
        self.head_link = new_node

    def dequeue(self): # возвращает первый элемент из очереди и удаляет его
        if self.head_link is None:
            return
        previous = None
        now = self.head_link
        result = self.head_link.data_value
        while now.next_value:
            previous = now
            now = now.next_value
        result = now.data_value
        previous.next_value = None
        return result
        
    def first(self): # возвращает первый элемент из очереди
        if self.head_link is None:
            return
        now = self.head_link
        result = self.head_link.data_value
        while now.next_value:
            now = now.next_value
        result = now.data_value
        return result

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head_link is None:
            self.head_link = new_node
            return
        last = self.head_link
        while last.next_value:
            last = last.next_value
        last.next_value = new_node

    def print_list(self):
        value = self.head_link
        while value is not None:
            print(value.data_value, end="  ")
            value = value.next_value

    def reverse_list(self):
        if not self.head_link:
            return self.head_link
        temp_prev = None
        temp_current = self.head_link
        while temp_current:
            temp_next = temp_current.next_value
            temp_current.next_value = temp_prev
            temp_prev = temp_current
            temp_current = temp_next
        self.head_link = temp_prev

    def del_last(self):
        temp = self.head_link.next_value
        self.head_link = temp