from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # intialize stack, result, potential water, wall_reduction
        stack = []
        result = 0
        potential_water = 0
        wall_reduction = 0
        # iterate through the height list
        for i in range(len(height)):
            # if the current height is 0 and empty stack
            if height[i] == 0 and not stack:
                continue
            # Now, the current height is 0 and stack is not empty
            # If the current height is greater than top of the stack
            if height[i] > stack[-1]:
                count_pop = 0
                # while the stack is not empty and the current height is greater than the top of the stack
                while stack and height[i] > stack[-1]:
                    # pop the top of the stack
                    top = stack.pop()
                    # if the stack is empty, break
                    if not stack:
                        break
                    wall_reduction = wall_reduction + top
                    count_pop += 1
                if stack:
                    # calculate the potential water
                    potential_water = min(height[i], stack[-1]) * count_pop - wall_reduction
                    if len(stack) ==  1:
                        result += potential_water
                        stack.pop()
                else:
                    potential_water = 0
                    wall_reduction = 0
            stack.append(height[i])
            
        # return the result
        return result
                    