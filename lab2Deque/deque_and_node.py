class Node:
    def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None


class Deque:
    def __init__(self):
        self.current = None

    def insert_left(self, value):
        new_obj = Node(value)
        if self.current is None:
            self.current = new_obj
        else:
            new_obj.right = self.current
            self.current.left = new_obj
            self.current = new_obj

    def insert_right(self, value):
        new_obj = Node(value)
        checker = self.current
        if self.current is None:
            self.current = new_obj
        else:
            while checker.right is not None :
                checker = checker.right

            new_obj.left = checker
            checker.right = new_obj

    def get_right(self):
        checker = self.current
        if checker.left is None:
            while checker.right is not None:
                checker = checker.right
            return checker.value

    def get_left(self):
        return self.current.value

    def delete_last_left(self):
        self.current = self.current.right

    def delete_last_right(self):
        checker = self.current
        if checker.left is None:
            while checker.right is not None:
                checker = checker.right
            checker.left.right = None

    def show_deque(self):
        checker = self.current
        while checker.right is not None:
            print(checker.value)
            checker = checker.right
        print(checker.value)

    def deque_into_list(self):
        list_res = list()
        checker = self.current
        while checker.right is not None:
            list_res.append(checker.value)
            checker = checker.right
        list_res.append(checker.value)
        return list_res

    def check_if_present(self, searched_value):
        checker = self.current
        while checker is not None:
            if checker.value == searched_value:
                print("The deque has this value: ", searched_value)
                return
            checker = checker.right
        print("Value %d is not found" % searched_value)
