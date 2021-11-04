import unittest
from deque_and_node import Deque


class TestTheDeque(unittest.TestCase):
    def test_insert_left(self):
        test_que = Deque()
        test_que.insert_left(8)
        test_que.insert_left(12)
        test_que.insert_left(15)
        list_que = test_que.deque_into_list()
        self.assertEqual(list_que, [15, 12, 8])

    def test_insert_right(self):
        test_que = Deque()
        test_que.insert_right(3)
        test_que.insert_right(4)
        test_que.insert_right(11)
        list_que = test_que.deque_into_list()
        self.assertEqual(list_que, [3, 4, 11])
    # get values of last elements from deque

    def test_get_left(self):
        self.test_que = Deque()
        self.test_que.insert_left(8)
        self.test_que.insert_left(12)
        self.test_que.insert_left(15)
        self.test_que.insert_right(3)
        self.test_que.insert_right(4)
        self.test_que.insert_right(11)
        found_value = self.test_que.get_left()
        self.assertEqual(found_value, 15)

    def test_get_right(self):
        self.test_que = Deque()
        self.test_que.insert_left(8)
        self.test_que.insert_left(12)
        self.test_que.insert_left(15)
        self.test_que.insert_right(3)
        self.test_que.insert_right(4)
        self.test_que.insert_right(11)
        found_value = self.test_que.get_right()
        self.assertEqual(found_value, 11)

    # deletion from both sides
    def test_delete_left(self):
        self.test_que = Deque()
        self.test_que.insert_left(8)
        self.test_que.insert_left(12)
        self.test_que.insert_left(15)
        self.test_que.insert_right(3)
        self.test_que.insert_right(4)
        self.test_que.insert_right(11)
        self.test_que.delete_last_left()
        list_que = self.test_que.deque_into_list()
        self.assertEqual(list_que, [12, 8, 3, 4, 11])

    def test_delete_right(self):
        self.test_que = Deque()
        self.test_que.insert_left(8)
        self.test_que.insert_left(12)
        self.test_que.insert_left(15)
        self.test_que.insert_right(3)
        self.test_que.insert_right(4)
        self.test_que.insert_right(11)
        self.test_que.delete_last_right()
        list_que = self.test_que.deque_into_list()
        self.assertEqual(list_que, [15, 12, 8, 3, 4])
