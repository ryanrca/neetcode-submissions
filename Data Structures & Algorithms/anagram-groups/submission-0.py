class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_cache = {}   # key = sorted string, val = array of strings
        res = []

        for word in strs:
            sortstr = "".join(i for i in sorted(word))
            if sortstr in sorted_cache:
                sorted_cache[sortstr].append(word)
            else:
                sorted_cache[sortstr] = [word]

        for key,val in sorted_cache.items():
            res.append(val)
        return res


