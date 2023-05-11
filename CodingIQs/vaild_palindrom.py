class Solution(object):
    def isPalindrome(self, s):
        # brute force
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if not self.alphaNum(s[l]):
                l += 1
            elif not self.alphaNum(s[r]):
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l, r = l + 1, r-1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(
            c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))
