class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test_lib = {}
        for i in nums:
            if i in test_lib:
                test_lib[i] += 1
            else:
                test_lib[i] = 1
            if test_lib[i] > 1:
                return True
        return False
        