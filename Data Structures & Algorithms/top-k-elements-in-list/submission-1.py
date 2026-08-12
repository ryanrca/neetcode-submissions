import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        # first count instances in nums
        for i in nums:
            counts[i] = counts.get(i,0) + 1

        heap = []
        # heappushpop k items in count instance
        for num, count in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (count,num))
            else:
                heapq.heappushpop(heap, (count,num))

        ret = []
        for count,num in heap:
            ret.append(num)
        return ret