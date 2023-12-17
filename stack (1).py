class Stack:
    def __init__(self):
        self.list = []
    def push(self, item):
        self.list.insert(0,item)
    def peek(self):
        return self.list[0]
    def pop(self):
        if len(self.list) != 0:
            return self.list.pop(0)
    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False
    def __str__(self):
        s1 = ""
        for i in range(len(self.list)):
            s1 += str(self.list[i]) + " " 
        return s1
    def __len__(self):
        return len(self.list)
obj = Stack()
obj.push(2)
obj.pop()
obj.pop()
print(obj.__str__())


		