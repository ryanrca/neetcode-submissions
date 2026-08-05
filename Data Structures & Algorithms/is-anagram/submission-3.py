class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        comp = {}
        for i in s:
            if i in comp:
                comp[i] += 1
            else:
                comp[i] = 1
        for i in t:
            if i in comp:
                comp[i] -= 1
            else:
                comp[i] = 1

        print(comp)
        
        for key,val in comp.items():
            if val != 0:
                return False
        return True
        
        