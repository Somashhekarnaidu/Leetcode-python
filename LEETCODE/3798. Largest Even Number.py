class Solution:
    def largestEven(self, s: str) -> str:
        # Given an arbitrary digit string, we may delete characters but must
        # retain order. The largest even integer we can obtain is the longest
        # prefix ending in an even digit (0,2,4,6,8). Removing trailing odd
        # digits makes the number smaller, so we simply truncate at the last
        # even digit if one exists.
        #
        # Example:
        #   "2314523" -> last even is the 2 before the final 3 -> "231452"
        #   "1111"    -> no even digit -> ""

        # scan from right for an even digit
        for i in range(len(s) - 1, -1, -1):
            if s[i] in "02468":
                return s[: i + 1]
        return ""