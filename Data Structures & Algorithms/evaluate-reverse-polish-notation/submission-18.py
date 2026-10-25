class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        while len(tokens) != 1: 
            if tokens[i] == '+': 
                print(tokens)
                result = int(tokens[i-2]) + int(tokens[i-1])
                tokens[i-2:i+1] = [str(result)] 
                i = 0
                print(tokens)
            elif tokens[i] == '-': 
                result = int(tokens[i-2]) - int(tokens[i-1])
                tokens[i-2:i+1] = [str(result)] 
                i = 0
                print(tokens)
            elif tokens[i] == '*': 
                result = int(tokens[i-1]) * int(tokens[i-2])
                tokens[i-2:i+1] = [str(result)] 
                i = 0
                print(tokens)
            elif tokens[i] == '/':
                result = int(int(tokens[i-2]) / int(tokens[i-1]))
                tokens[i-2:i+1] = [str(result)] 
                i = 0
                print(tokens)
            else:
                i+= 1 
        count = 0 
        for i in range(len(tokens)): 
            count += int(tokens[i])
        return count 
        