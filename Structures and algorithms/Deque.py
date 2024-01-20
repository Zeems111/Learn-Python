class Deque:
    def __init__(self):
        self.queue = []
        self.reverse_queue = []

    def size(self):
        return len(self.queue) + len(self.reverse_queue)

    def clear(self):
        self.queue.clear()
        self.reverse_queue.clear()

    def push_back(self, item):
        self.queue.append(item)

    def push_front(self, item):
        self.reverse_queue.append(item)

    def pop_front(self):
        if self.size() == 0:
            return None
        tmp = None
        try:
            if not self.reverse_queue:
                for _ in range(len(self.queue)):
                    self.reverse_queue.append(self.queue.pop())
            tmp = self.reverse_queue.pop()
        except IndexError:
            pass
        return tmp

    def pop_back(self):
        if self.size() == 0:
            return None
        tmp = None
        try:
            if not self.queue:
                for _ in range(len(self.reverse_queue)):
                    self.queue.append(self.reverse_queue.pop())
            tmp = self.queue.pop()
        except IndexError:
            pass
        return tmp

    def back(self):
        if self.size() == 0:
            return None
        tmp = None
        try:
            if self.queue:
                tmp = self.queue[-1]
            else:
                tmp = self.reverse_queue[0]
        except IndexError:
            pass
        return tmp

    def front(self):
        if self.size() == 0:
            return None
        tmp = None
        try:
            if self.reverse_queue:
                tmp = self.reverse_queue[-1]
            else:
                tmp = self.queue[0]
        except IndexError:
            pass
        return tmp

    def __str__(self):
        deque = []
        deque.extend(list(reversed(self.reverse_queue)))
        deque.extend(self.queue)
        return " ".join(str(x) for x in deque)


if __name__ == '__main__':

    deq = Deque()
    while True:
        command = input().split()
        if command[0] == "exit":
            print("bye")
            break
        elif command[0] == "push_front":
            deq.push_front(command[1])
            print("ok")
        elif command[0] == "push_back":
            deq.push_back(command[1])
            print("ok")
        elif command[0] == "pop_front":
            t = deq.pop_front()
            if t is None:
                print("error")
            else:
                print(t)
        elif command[0] == "pop_back":
            t = deq.pop_back()
            if t is None:
                print("error")
            else:
                print(t)
        elif command[0] == "front":
            t = deq.front()
            if t is None:
                print("error")
            else:
                print(t)
        elif command[0] == "back":
            t = deq.back()
            if t is None:
                print("error")
            else:
                print(t)
        elif command[0] == "size":
            print(deq.size())
        elif command[0] == "clear":
            deq.clear()
            print("ok")

"""
examples of commands:
push_front 179
push_back 8343
front
back
size
pop_back
pop_front
push_back 342
clear
back
front
pop_back
pop_front
push_back 265
push_back 63456
size
pop_back
size
front
back
size
pop_front
size
back
front
size
pop_back
front
back
size
pop_front
back
front
size
exit
"""