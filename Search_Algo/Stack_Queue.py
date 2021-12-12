import unittest


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def front(self):
        return self.items[- 1]

    def back(self):
        return self.items[0]

    def size(self):
        return len(self.items)
# Unit Test


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

    def test_pop(self):
        self.stack.pop()
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 0)

    def test_size(self):
        self.assertEqual(self.stack.size(), 3)
        self.stack.push(4)
        self.assertEqual(self.stack.size(), 4)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 3)

    def test_peek(self):
        self.assertEqual(self.stack.peek(), 3)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), None)

    def test_stack(self):
        stack = Stack()
        self.assertEqual(stack.isEmpty(), True)
        stack.push(4)
        stack.push('dog')
        self.assertEqual(stack.peek(), 'dog')
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.isEmpty(), False)
        self.assertEqual(stack.pop(), 'dog')
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.isEmpty(), True)


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue('perro')
        self.queue.enqueue('gato')

    def testPop(self):
        self.assertEqual(self.queue.dequeue(), 'perro')
        self.assertEqual(self.queue.size(), 1)
        self.assertEqual(self.queue.dequeue(), 'gato')
        self.assertEqual(self.queue.size(), 0)
        self.assertEqual(self.queue.dequeue(), None)


# run the test
if __name__ == '__main__':
    unittest.main()
