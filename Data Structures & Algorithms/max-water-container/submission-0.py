class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        if len(heights) == 0:
            return 0

        # n^2 solution:
        '''
        for left in range(len(heights)):
            for right in range(left, len(heights)):
                area = (right-left) * min(heights[left], heights[right])

                max_area = max(max_area, area)
        '''

        # n solution:
        left = 0
        right = len(heights) - 1
        while left < right:
            area = (right-left) * min(heights[left], heights[right])
            max_area = max(max_area, area)
            if heights[left] <= heights[right]:
                left+=1
            else:
                right-=1

        return max_area
        