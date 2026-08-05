class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start <= end:
            while not s[start].isalnum() and start < len(s) -1:
                start+=1
            while not s[end].isalnum() and end >= 0:
                end-=1
            if s[start].upper() != s[end].upper():
                if start < len(s) -1 and end >= 0:
                    return False
                else:
                    break
            start+=1
            end-=1
        return True