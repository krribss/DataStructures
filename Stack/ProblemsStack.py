from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

    def reverse_string(self,val):
        text=""
        for chr in val:
            self.push(chr)
        while(not self.is_empty()):
            text+=self.pop()
        return text

    def paranthesis_check(self,val):
        for chr in val:
            if (chr in ['[','{','(']):
                self.push(chr)
            elif(self.is_empty() and chr in [']','}',')']):
                return False
            elif((not self.is_empty()) and chr == ']' and self.peek()=='['):
                self.pop()
            elif((not self.is_empty()) and chr == '}' and self.peek()=='{'):
                self.pop()
            elif((not self.is_empty()) and chr == ')' and self.peek()=='('):
                self.pop()
            else:
                pass

        if (self.is_empty()):
            return True
        else:
            return False

stack=Stack()
#print(stack.reverse_string("We will conquere COVID-19"))
print(stack.paranthesis_check("({a+b})"))
print(stack.paranthesis_check("))((a+b}{"))
print(stack.paranthesis_check("((a+b))"))
print(stack.paranthesis_check("))"))
print(stack.paranthesis_check("[a+b]*(x+2y)*{gg+kk}"))
