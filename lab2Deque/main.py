from deque_and_node import Deque


if __name__ == '__main__':
    que = Deque()
    que.insert_left(1)

    que.insert_left(2)
    que.insert_left(3)
    que.insert_left(4)
    que.insert_right(-1)
    que.insert_right(-2)

    que.insert_right(-4)

    found_right = que.get_right()
    print("The last in the Que from right side -", found_right)
    found_left = que.get_left()
    print("The last in the Que from left side - ", found_left)

    que.show_deque()
    print(que.deque_into_list())
    que.check_if_present(2)
    que.check_if_present(5)
