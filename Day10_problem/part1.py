from collections import deque

def solve(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    def bfs(sr, sc):
        queue = deque([(sr, sc)])
        visited = set([(sr, sc)])
        reachable_nines = set()

        while queue:
            r, c = queue.popleft()
            if grid[r][c] == 9:
                reachable_nines.add((r, c))
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in visited and grid[nr][nc] == grid[r][c] + 1:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        return len(reachable_nines)

    total_score = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                total_score += bfs(r, c)

    return total_score


# Read input
grid = [list(map(int, line.strip())) for line in open("input.txt")]
print(solve(grid))
