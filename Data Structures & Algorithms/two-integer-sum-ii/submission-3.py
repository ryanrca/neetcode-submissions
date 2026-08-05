class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start = 0
        end = len(numbers) -1

        while start <= end:
            test = numbers[start] + numbers[end]

            if test == target:
                return [start+1, end+1]
    
            # if sum of two is > target: move end -1
            if test > target:
                end -= 1
    
            # if sum is < target: move start +1
            if test < target:
                start += 1

        # something went wrong:
        return [-1,-1]
