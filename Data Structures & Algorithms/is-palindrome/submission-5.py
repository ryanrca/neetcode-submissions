class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_p = 0
        right_p = len(s)-1

        s = s.lower()

        while left_p < right_p:

            while (not s[left_p].isalnum()) and left_p < len(s)-1:
                left_p += 1

            while (not s[right_p].isalnum()) and right_p > 0:
                right_p -= 1

            if right_p < 0:
                break

            if left_p >= right_p:
                break

            if s[left_p] != s[right_p]:
                return False

            left_p += 1
            right_p -= 1

        return True
