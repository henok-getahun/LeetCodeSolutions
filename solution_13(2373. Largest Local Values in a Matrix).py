class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        new_matrix = [[0]*(n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                max_value = grid[i][j]
                for k in range(i,i+3):
                    for r in range(j,j+3):
                        if max_value < grid[k][r]:
                            max_value = grid[k][r]
                new_matrix[i][j] = max_value

        return new_matrix
