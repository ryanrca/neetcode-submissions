class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 3:
            if (nums[0] + nums[1] + nums[2]) == 0:
                return [[nums[0], nums[1], nums[2]]]
            else:
                return []

        ret = []
        nums.sort()
        i = 0

        while i < len(nums)-2 and nums[i] < 1:  # We can break once all numbers are positive - we will never get 0!
            left  = i + 1
            right = len(nums)-1
            while left < right:
                ans = nums[i] + nums[left] + nums[right]
                if ans == 0:

                    ret.append([nums[i], nums[left], nums[right]])
                    # move left up until nums[left] is a new number
                    cur_l = nums[left] 
                    left+=1
                    while nums[left] == cur_l and left < right:
                        left+=1
                    # move right down until nums[right] is a new number
                    cur_r = nums[right]
                    right-=1
                    while nums[right] == cur_r and right > left:
                        right-=1

                if ans < 0:
                    left+=1

                if ans > 0:
                    right-=1

            # increment i until nums[i] is new:
            cur_i = nums[i]
            i+=1
            while i < (len(nums)-2) and nums[i] == cur_i:
                i+=1

        return ret

                

        