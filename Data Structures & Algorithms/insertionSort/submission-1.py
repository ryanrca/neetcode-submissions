# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def p(self, a: List[List[Pair]]):
        for l in a:
            print(f"{l.key}: {l.value}")
        
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:


        ret = []
        if len(pairs) == 0:
            return ret

        ret.append(pairs[:])
        for cur in range(1,len(pairs)):
            for j in range(cur, 0, -1):
                if pairs[j-1].key > pairs[j].key:
                    pairs[j-1], pairs[j] = pairs[j], pairs[j-1]
                else:
                    break
            # self.p(pairs)
            ret.append(pairs[:])

        return ret
