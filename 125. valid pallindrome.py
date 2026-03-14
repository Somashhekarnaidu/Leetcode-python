class Solution(object):
    def isPalindrome(self, s):
        s= s.lower()
        cleaned= ""
        for ch in s.lower():
            if ch .isalnum():
                cleaned+= ch
        reverse=cleaned[::-1]
        return reverse== cleane