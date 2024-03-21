class Stack:
    def __init__(self):
        self.st = []

    def isEmpty(self):
        if len(self.st) == 0:
            return True
        else:
            return False

    def push(self, el):
        self.st.append(el)

    def pop(self):
        result = self.st.pop()
        return result

    def peec(self):
        result = self.st[-1]
        return result

    def size(self):
        result = len(self.st)
        return result