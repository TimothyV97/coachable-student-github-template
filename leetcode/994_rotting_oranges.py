'''
Understand the problem:
 
Keypoints:
  1. Every minute, any fresh orange connected adjacent to a rotten orange becomes rotten.
  2. Cells are connected - hint this is a graph problem.
  3. Return the number of minutes when no more fresh oranges remain; otherwise, return -1.
Solution: BFS on graph
  1. Count the number of fresh oranges.
  2. While counting, add the rotten oranges' positions to a queue (for BFS).
  3. Add a flag to the queue to indicate each minute (level in BFS).
  4. In BFS, pop a cell, check it, and rot the adjacent fresh oranges.
  
Runtime: O(m*n)
Space: O(m*n)
'''
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Determines the minimum time required for all fresh oranges to rot.
        
        Args:
            grid (List[List[int]]): A 2D grid where:
                - 0 represents an empty cell,
                - 1 represents a fresh orange,
                - 2 represents a rotten orange.
        
        Returns:
            int: The minimum number of minutes needed to rot all oranges, or -1 if impossible.
        """
        fresh_oranges = 0
        queue = deque()
        minutes = -1
        ROWS, COLS = len(grid), len(grid[0])
        # Count fresh oranges and enqueue all rotten oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        # Use (-1, -1) as a minute flag
        queue.append((-1, -1))
        # BFS to rot adjacent fresh oranges
        while queue:
            r, c = queue.popleft()
            if r == -1:  # Minute flag encountered
                minutes += 1
                if queue:
                    queue.append((-1, -1))
            else:
                # Explore the 4 possible directions
                for x, y in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    row, col = r + x, c + y
                    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                        # Rot the fresh orange
                        grid[row][col] = 2
                        fresh_oranges -= 1
                        queue.append((row, col))
        # If there are fresh oranges left, return -1; otherwise, return minutes
        return minutes if fresh_oranges == 0 else -1