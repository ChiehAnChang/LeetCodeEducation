from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize an empty stack to store the numbers
        stack = []
        
        # go through each token in the input list
        for token in tokens:
            if token not in "+-*/":
                
                stack.append(int(token))
                continue    
                
            top = stack.pop()  # pop the top element from the stack
            second_top = stack.pop()
                
            if token == "+":
                
                stack.append(second_top + top)
                
            elif token == "-":
                
                stack.append(second_top - top)
                
            elif token == "*":
                
                stack.append(second_top * top)
                
            else:
                
                # Perform integer division and truncate towards zero
                stack.append(int(second_top / top))

        return stack[0]  # The result will be the only element left in the stack
                