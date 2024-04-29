stack = []
def push (value):
    stack.append(value)

def pop ():
    stack.pop()

def noel ():
    print(len(stack))

def top():
    top = len(stack)-1
    if top < 0:
        print("tidak terdefinisi")
    else:
        print(stack[top])

def isempty():
    if len(stack) == 0:
        print("TRUE")
    else:
        print("FALSE")

def tampilkan(stack):
    print("stack")    

def peek(self):
    return self.items[len(self.items)-1]

def size(self):
    return len (self.items)

#Contoh penggunaan stack
stack=stack()
stack.push('a')
stack.push('b')
stack.push('c')
print(stack.pop())#c
print(stack.peek())#b
stack.push('d')
print(stack.size())#3
print(stack.is_empety())#False                       

while True:
    value = input("--> ")