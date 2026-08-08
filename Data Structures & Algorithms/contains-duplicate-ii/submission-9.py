class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if k == 0:
            return False

        wset = set()
        L = 0
        R = 0
        wset.add(nums[R])

        for i in range(R+1, len(nums)):
            if nums[i] in wset:
                return True
            wset.add(nums[i])
            if len(wset) > k:
                wset.remove(nums[i-k])
        return False

