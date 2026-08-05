class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return -1

        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low+high)//2

            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                high = mid-1
            if target > nums[mid]:
                low = mid+1
        return -1 