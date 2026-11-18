class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot_queue = deque()
        fresh_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    rot_queue.append((i, j))
        if fresh_count == 0:
            return 0

        time = 0
        while rot_queue:
            self.spread = False
            for _ in range(len(rot_queue)):
                i, j = rot_queue.popleft()
                if grid[i][j] == 0:
                    continue
                self.spread = True
                grid[i][j] = 0
                if time > 0:
                    fresh_count -= 1
                for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                    if 0 <= i+dx < len(grid) and 0 <= j+dy < len(grid[0])\
                    and grid[i+dx][j+dy] == 1:
                        rot_queue.append((i+dx, j+dy))

            if not self.spread:
                time -= 1
            if rot_queue:
                time += 1
        
        return time if fresh_count == 0 else -1

