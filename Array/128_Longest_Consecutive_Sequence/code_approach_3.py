from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # turn the nums into the set
        nums_set = set(nums)
        
        longest_streak = 0
        
        # for-loop the nums
        for num in nums_set:
            # check if the num is the start of a sequence
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1
                
                # while-loop to find the longest streak
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
            
            if longest_streak > len(nums_set) // 2:
                break
        
        return longest_streak
                
