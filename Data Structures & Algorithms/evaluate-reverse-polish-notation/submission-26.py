class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens: 
            if token == '+':
                s1, s2 = stack.pop(), stack.pop() 
                result = int(s1) + int(s2) 
                stack.append(result)
            elif token == '*': 
                s1, s2 = stack.pop(), stack.pop() 
                result = int(s2) * int(s1) 
                stack.append(result)
            elif token == '/':
                s1, s2 = stack.pop(), stack.pop() 
                result = int(int(s2) / int(s1))
                stack.append(result)
            elif token == '-': 
                s1, s2 = stack.pop(), stack.pop() 
                result = int(s2) - int(s1) 
                stack.append(result)                
            else:
                stack.append(token)
        return int((stack[0]))
        