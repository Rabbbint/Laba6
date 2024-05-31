import unittest
from one import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_append(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        self.assertEqual(str(llist), "123")

    def test_sort_list(self):
        llist = LinkedList()
        llist.append(9)
        llist.append(1)
        llist.append(2)
        llist.sort_list()
        self.assertEqual(str(llist), "129")


if __name__ == '__main__':
    unittest.main()