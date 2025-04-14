class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        nums.sort()
        
        # result array
        res = []
        # for loop through the array
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else: 
                
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    # calculate the sum of the three numbers
                    total = nums[i] + nums[left] + nums[right]
                    # if the sum is 0, add it to the result array
                    if total == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # skip duplicates for left pointer
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        # skip duplicates for right pointer
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < 0:
                        left += 1
                    else:
                        right -= 1
        return res