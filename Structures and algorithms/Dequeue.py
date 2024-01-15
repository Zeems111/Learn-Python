class Dequeue:
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
        print("ok")
    def pop_back(self):
        try:
            top = self.queue.pop()
        except Exception:
            print("error")
        return top

    def front(self):
        return self.queue[0] if self.queue else self.reverse_queue[-1]

    def back(self):
        return self.queue[-1] if self.queue else self.reverse_queue[0]