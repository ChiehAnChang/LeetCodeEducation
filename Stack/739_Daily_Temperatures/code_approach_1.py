from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initiallize the stack and the result list
        stack = []
        result = [0] * len(temperatures)
        
        # iterate through the temperatures list
        for i, current_temp in enumerate(temperatures):
            
            # check if the current value have a greater value than the last value in the stack and the past
            
            while stack and current_temp > temperatures[stack[-1]]:
                
                # pop the last value
                last_index = stack.pop()
                
                # calculate the difference between the current index and the last index
                result[last_index] = i - last_index
            
            # append the current index to the stack
            stack.append(i)
        
        # loop through the stack and set the result to 0
        while stack:
            last_index = stack.pop()
            result[last_index] = 0
        return result
    
    
                    