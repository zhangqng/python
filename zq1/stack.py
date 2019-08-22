class Stack1:
    def __init__(self):
        self.values = []
    def pop(self):
        if self.is_empty():
            raise Exception("stack is blank")
        return self.values.pop()
    def push(self, value):
        return self.values.append(value)
    def is_empty(self):
        return len(self.values) == 0
    def length(self):
        return len(self.values)
    def peak(self):
        if self.is_empty():
            raise Exception("stack is blank")
        print(self.values[self.length()-1])
        return self.values[self.length()-1]
    def now(self):
        print(self.values)
        return self.values


if __name__ == '__main__':
    s = Stack1()
    s.is_empty()
    s.push("a")
    s.peak()
    s.push("b")
    s.peak()
    s.push("c")
    s.length()
    s.is_empty()
    s.now()
    s.pop()
    s.now()
    s.length()
    s.pop()
    s.pop()
    s.is_empty()
    import time
    time.sleep(3)
    s.pop()
    s.peak()



