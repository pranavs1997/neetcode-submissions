class Solution:
    def isPalindrome(self, s: str) -> bool:
        # result = ''.join(c for c in s if c.isalnum())
        # if result.lower() == result[::-1].lower():
        #     return True
        # else:
        #     return False
        result = ''.join(c for c in s if c.isalnum())
        result = result.lower()
        l, r = 0, len(result)-1
        while l < r:
            if result[l] != result[r]:
                return False
            l, r = l + 1, r - 1
        return True