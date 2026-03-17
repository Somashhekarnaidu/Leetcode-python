class Solution(object):
    def isPowerOfTwo(self, n):
        if n<= 0:
            return False
        for i in range( 0, 31):
            if 2**i == n:
                return True
        return False

        