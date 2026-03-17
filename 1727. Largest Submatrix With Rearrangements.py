class Solution(object):
    def largestSubmatrix(self, matrix):
        if not matrix:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        height = [0] * cols
        max_area = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    height[c] += 1
                else:
                    height[c] = 0
            
            sorted_heights = sorted(height, reverse=True)
            
            for i in range(cols):
                area = sorted_heights[i] * (i + 1)
                if area > max_area:
                    max_area = area
        
        return max_area