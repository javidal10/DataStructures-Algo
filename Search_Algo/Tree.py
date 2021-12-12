import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def isValue(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.left:
                return self.left.isValue(data)
            else:
                return False
        else:
            if self.right:
                return self.right.isValue(data)
            else:
                return False

    def delete(self, data):
        if self.value == data:
            if self.left is None and self.right is None:
                return None
