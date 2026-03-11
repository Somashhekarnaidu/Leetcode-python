class Solution(object):
    def reverse(self, x):
        rev = int(str(abs(x))[::-1])
        rev = rev if x >= 0 else -rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev