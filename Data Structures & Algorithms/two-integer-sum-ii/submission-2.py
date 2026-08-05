class Solution:

    # returns the index of the target or next one larger if not found
    def bin_search(self, nums, target):
            
        end = len(nums)-1
        start = 0
        if target > nums[end]:
            return end
        if len(nums) == 2:
            return end

        # bin search
        target_index = (start+end)//2
        while (nums[target_index] != target):


            if end-start < 3:
                while nums[end] <= target and end < len(nums)-1:
                    end+=1
                return end
            
            if nums[target_index] > target:
                start = target_index
                target_index = (start+end)//2

            if nums[target_index] < target:
                end = target_index
                target_index = (start+end)//2

        return target_index

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start = 0

        # iterate only that half : binary search
        # find the position where numbers[]  = target, 
        # end = self.bin_search(numbers, target)
        end = len(numbers) -1

        while start <= end:
            test = numbers[start] + numbers[end]

            print(f"testing: start: [{start}] {numbers[start]}, end: [{end}] {numbers[end]}")

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
