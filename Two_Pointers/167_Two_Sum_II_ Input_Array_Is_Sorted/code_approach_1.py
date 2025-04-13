from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initial hash_map
        prev_map = {}
        # Initialize the final result list
        # for-loop the numbers
        for i in range(len(numbers)):
            # check if the number is in the hash_map
            if numbers[i] in prev_map:
                return [prev_map[numbers[i]] + 1, i + 1]
            # add the number to the hash_map
            prev_map[target - numbers[i]] = i
        
        
        
        