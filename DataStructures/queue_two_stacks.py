
class MyQueue(object):
    def __init__(self):
        self.mode = 'WRITE'
        self.lstack = []
        self.rstack = []

    def switch_mode(self, to_mode):
        if self.mode == to_mode:
            return

        if to_mode == 'WRITE':
            self.mode = 'WRITE'
            from_stack = self.lstack
            to_stack = self.rstack
        else:
            self.mode = 'READ'
            from_stack = self.rstack
            to_stack = self.lstack

        while True:
            try:
                to_stack.append(from_stack.pop())
            except IndexError:
                break

    def peek(self):
        self.switch_mode('READ')
        return self.lstack[-1]

    def pop(self):
        self.switch_mode('READ')
        return self.lstack.pop()

    def put(self, value):
        self.switch_mode('WRITE')
        self.rstack.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())


class MyQueue(object):
    # new_to_old => dequeue (get old from the back)
    # old_to_new => enqueue (add new to the back)
    def __init__(self):
        self.enqueue = []
        self.dequeue = []

    def peek(self):
        if not self.dequeue:
            while self.enqueue:
                self.dequeue.append(self.enqueue.pop())
        val = self.dequeue.pop()
        self.dequeue.append(val)
        return val

    def pop(self):
        if not self.dequeue:
            while self.enqueue:
                self.dequeue.append(self.enqueue.pop())
        return self.dequeue.pop()

    def put(self, value):
        self.enqueue.append(value)
