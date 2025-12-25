class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        col_count = len(grid[0])
        
        for row in grid:
            heapq.heapify(row)

        ans = 0
        for _ in range(col_count):
            ans += max([heapq.heappop(h) for h in grid])
        return ans