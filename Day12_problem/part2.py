ORTHOGONAL_DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get(lines, pos, default):
    x, y = pos
    if 0 <= x < len(lines) and 0 <= y < len(lines[0]):
        return lines[x][y]
    return default

def calculate_total_area_and_perimeter(input_file):
    with open(input_file, 'r') as f:
        lines = [list(line.strip()) for line in f.readlines()]

    total = 0
    visited = set()

    for i, row in enumerate(lines):
        for j, c in enumerate(row):
            if (i, j) in visited:
                continue

            visited_perimeter = set()
            stack = [(i, j)]
            area = 0
            perimeter = 0

            while stack:
                x, y = stack.pop()
                if (x, y) in visited:
                    continue

                for d in ORTHOGONAL_DIRS:
                    if get(lines, (x + d[0], y + d[1]), None) == c:
                        stack.append((x + d[0], y + d[1]))
                    else:
                        if ((x, y), (x + d[0], y + d[1])) in visited_perimeter:
                            continue

                        perimeter += 1
                        visited_perimeter.add(((x, y), (x + d[0], y + d[1])))

                        d1 = (-d[1], d[0])
                        d2 = (d[1], -d[0])

                        curr = (x, y)
                        while True:
                            curr = (curr[0] + d1[0], curr[1] + d1[1])
                            if get(lines, curr, None) == c and get(lines, (curr[0] + d[0], curr[1] + d[1]), None) != c:
                                visited_perimeter.add((curr, (curr[0] + d[0], curr[1] + d[1])))
                            else:
                                break

                        curr = (x, y)
                        while True:
                            curr = (curr[0] + d2[0], curr[1] + d2[1])
                            if get(lines, curr, None) == c and get(lines, (curr[0] + d[0], curr[1] + d[1]), None) != c:
                                visited_perimeter.add((curr, (curr[0] + d[0], curr[1] + d[1])))
                            else:
                                break

                area += 1
                visited.add((x, y))

            total += area * perimeter

    return total

input_file = 'input.txt'
total = calculate_total_area_and_perimeter(input_file)
print(total)