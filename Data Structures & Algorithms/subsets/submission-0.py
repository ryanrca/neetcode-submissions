class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = []
        current_subset = []

        def backtrace(ans, current, index):
            
            ans.append(current.copy())
            
            for i in range(index, len(nums)):
                if nums[i] not in current:
                    current.append(nums[i])
                    backtrace(ans, current, i)
                    current.pop()
            return

        backtrace(subsets, current_subset, 0)

        return subsets