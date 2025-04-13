from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Intialize the left and right pointers
        left = 0
        right = len(numbers) - 1
        # while-loop to find the two numbers
        while numbers[left] + numbers[right] != target:
            # check if the sum is less than the target
            if numbers[left] + numbers[right] < target:
                left += 1
            # check if the sum is greater than the target
            else:
                right -= 1
        return [left + 1, right + 1]