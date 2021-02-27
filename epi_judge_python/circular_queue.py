from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:

    def getNext(self, cur):
        return 0 if cur == self.capacity - 1 else cur + 1

    def getPrevious(self, cur):
        return self.capacity - 1 if cur == 0 else cur - 1

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.start = 0
        self.end = 0

    def enqueue(self, x: int) -> None:
        # TODO - you fill in here.
        return

    def dequeue(self) -> int:
        # TODO - you fill in here.
        return 0

    def size(self) -> int:
        # TODO - you fill in here.
        return 0


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
