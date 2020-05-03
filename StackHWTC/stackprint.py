# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
#stack.py

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def inOrder(self):
        temp_stack = Stack()
        after = self.items.pop()
        current = self.items.pop()
        temp_stack.push(after)
        temp_stack.push(current)
        while current < after and not(self.isEmpty()):
            current = after
            after = self.items.pop()
            temp_stack.push(after)
        if self.isEmpty():
            x = True
        else:
            x = False

        while not(temp_stack.isEmpty()):
            self.push(temp_stack.pop())

        return x

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        temp = Stack()
        stringy = ""
        while not self.isEmpty():
            a = self.pop()
            temp.push(a)
            stringy = str(a) + stringy
        while not temp.isEmpty():
            self.push(temp.pop())
        return "["+stringy+")\n"        
        
        '''
    def inOrder(self):
        order = 0
        for i in range(len(self.items)-1):
            if self.items[i] < self.items[i+1]:
                order += 1
        if order == len(self.items)-1:
            return True
        else:
            return False
'''
def main():
    a = "145"
    s = Stack()
    for b in a:
        s.push(b)
        print(s)
    print(s.inOrder())
main()
