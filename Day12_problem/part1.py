def total_fence_price(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        stack = [(r, c)]
        plant = grid[r][c]
        area = 0
        perimeter = 0

        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue

            visited.add((x, y))
            area += 1

            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                    perimeter += 1
                elif grid[nx][ny] != plant:
                    perimeter += 1
                elif (nx, ny) not in visited:
                    stack.append((nx, ny))

        return area, perimeter

    total = 0
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                area, per = dfs(i, j)
                total += area * per

    return total


# 📥 Read input from file
with open("input.txt", "r") as f:
    grid = [line.strip() for line in f if line.strip()]

# 🧮 Compute answer
print(total_fence_price(grid))
