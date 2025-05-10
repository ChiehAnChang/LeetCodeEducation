from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # There is at least one element and if the len is 1, return 0 if the element is equal to target
        if nums[0] == target:
            return 0
        
        
        left, right = 0, len(nums) - 1
        
        
        while left <= right:
            
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1