from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # in-place sorting to avoid extra space usage
        nums.sort()
        
        longest_streak = 0
        current_streak = 1
        
        curret_index = 0
        while curret_index < len(nums) - 1:
            if nums[curret_index] == nums[curret_index + 1]:
                curret_index += 1
                continue
            
            if nums[curret_index] + 1 == nums[curret_index + 1]:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
            
            curret_index += 1
        longest_streak = max(longest_streak, current_streak)
        return longest_streak
                
                
        
        
sorted_nums = [9,1,4,7,3,-1,0,5,8,-1,6]
sorted_nums.sort()
print(sorted_nums)