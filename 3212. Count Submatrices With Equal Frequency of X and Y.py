class Solution:
    def numberOfSubmatrices(self, grid):
        m = len(grid)
        n = len(grid[0])

        x_count = [[0]*n for _ in range(m)]
        y_count = [[0]*n for _ in range(m)]

        ans = 0

        for i in range(m):
            for j in range(n):
                x = 1 if grid[i][j] == 'X' else 0
                y = 1 if grid[i][j] == 'Y' else 0

                if i > 0:
                    x += x_count[i-1][j]
                    y += y_count[i-1][j]

                if j > 0:
                    x += x_count[i][j-1]
                    y += y_count[i][j-1]

                if i > 0 and j > 0:
                    x -= x_count[i-1][j-1]
                    y -= y_count[i-1][j-1]

                x_count[i][j] = x
                y_count[i][j] = y

                if x == y and x > 0:
                    ans += 1

        return ans