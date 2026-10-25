class MinStack:

    def __init__(self):
        self.myStack = []
        self.size = 0
        self.minStack = []

    def push(self, val: int) -> None:
        if self.size == 0:
            self.minStack.append(val) 
        self.myStack.append(val)
        self.size += 1 
        if self.minStack[-1] >= val: 
            self.minStack.append(val) 

    def pop(self) -> None:
        if self.size == 0: 
            print("Error")
        else: 
            popped_elem = self.myStack.pop(-1)
            self.size -= 1
            if popped_elem == self.minStack[-1]:
                self.minStack.pop(-1) 
            

    def top(self) -> int:
        if self.size == 0: 
            return -1
        else: 
            return self.myStack[-1]
    def getMin(self) -> int:
        return self.minStack[-1]
        
