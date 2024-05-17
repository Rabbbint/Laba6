class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def sort_list(self):
        if self.head is None or self.head.next is None:
            return

        # Разделение списка на две половины
        slow_ptr = self.head
        fast_ptr = self.head.next
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        mid_node = slow_ptr.next
        slow_ptr.next = None

        # Рекурсивная сортировка левой и правой половин
        left_half = LinkedList()
        left_half.head = self.head
        left_half.sort_list()

        right_half = LinkedList()
        right_half.head = mid_node
        right_half.sort_list()

        # Слияние отсортированных половин
        self.head = self.merge(left_half.head, right_half.head)

    def merge(self, left_head, right_head):
        if not left_head:
            return right_head
        if not right_head:
            return left_head

        if left_head.data <= right_head.data:
            left_head.next = self.merge(left_head.next, right_head)
            return left_head
        else:
            right_head.next = self.merge(left_head, right_head.next)
            return right_head

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
    llist.print_list()

if __name__ == "__main__":
    main()