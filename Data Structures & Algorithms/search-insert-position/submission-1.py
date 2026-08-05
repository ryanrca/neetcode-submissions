class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        low = 0
        high = len(nums)-1

        # find number
        while low <= high:
            mid = (low+high)//2

            # return if found
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                high = mid-1
            if target > nums[mid]:
                low = mid+1
        
        # not found
        # check edge cases:
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)

        return low
