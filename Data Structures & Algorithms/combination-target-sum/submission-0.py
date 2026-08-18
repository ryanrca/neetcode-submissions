class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        current = []

        def backtrace(answers, cur, index):

            if index > len(nums):
                return
            if sum(cur) == target:
                answers.append(cur.copy())
                return
            if sum(cur) > target:
                return

            for i in range(index, len(nums)):
                cur.append(nums[i])
                backtrace(answers, cur, i)
                cur.pop()

        backtrace(ret, current, 0)
        return ret
        