class Solution:
    def maxArea(self, height: List[int]) -> int:
        # intialize the left and right pointers
        left = 0
        right = len(height) - 1
        # intialize the max area to 0
        max_area = 0
        # while the left pointer is less than the right pointer
        while left < right:
            # calculate the current area
            # update the max area if the current area is greater than the max area
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            # move the pointer with the smaller height towards the other pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area