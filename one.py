class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def sort_list(self):
        if not self.head or not self.head.next:
            return

        new_head = None
        current = self.head
        while current:
            next_node = current.next
            if not new_head or current.data <= new_head.data:
                current.next = new_head
                new_head = current
            else:
                search = new_head
                while search.next and search.next.data < current.data:
                    search = search.next
                current.next = search.next
                search.next = current
            current = next_node

        self.head = new_head

    def __str__(self):
        if not self.head:
            return ""

        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next

        return "".join(result)

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

def get_user_input():
    llist = LinkedList()
    while True:
        user_input = input("Введите число или 'stop' для завершения ввода: ")
        if user_input.lower() == "stop":
            break
        try:
            llist.append(int(user_input))
        except ValueError:
            print("Некорный ввод. Попробуйте ещё раз.")
    return llist

def main():
    llist = get_user_input()
    print("Изначальная последовательность чисел:")
    print(llist)

    llist.sort_list()
    print("Отсортированная последовательность чисел:")
    print(llist)

if __name__ == "__main__":
    main()
