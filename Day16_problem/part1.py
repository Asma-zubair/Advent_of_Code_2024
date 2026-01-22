
import heapq

def parse_input(file_name):
    with open(file_name, 'r') as f:
        maze = [line.strip() for line in f.readlines()]
    return maze

def find_positions(maze):
    start = end = None
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == 'S':
                start = (r, c)
            elif cell == 'E':
                end = (r, c)
    return start, end

def neighbors(position, direction, maze):
    r, c = position
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # East, South, West, North
    forward_r, forward_c = directions[direction]
    forward_pos = (r + forward_r, c + forward_c)

    neighbors = []

    # Forward move
    if 0 <= forward_pos[0] < len(maze) and 0 <= forward_pos[1] < len(maze[0]) and maze[forward_pos[0]][forward_pos[1]] != '#':
        neighbors.append((forward_pos, direction, 1))

    # Rotations
    neighbors.append(((r, c), (direction - 1) % 4, 1000))  # Counterclockwise rotation
    neighbors.append(((r, c), (direction + 1) % 4, 1000))  # Clockwise rotation

    return neighbors

def heuristic(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def a_star(maze, start, end):
    start_state = (start, 0)  # Position and direction (0: East)
    priority_queue = [(0, start_state)]  # (cost, (position, direction))
    visited = set()
    
    while priority_queue:
        cost, (position, direction) = heapq.heappop(priority_queue)
        
        if position == end:
            return cost

        if (position, direction) in visited:
            continue

        visited.add((position, direction))

        for next_position, next_direction, move_cost in neighbors(position, direction, maze):
            if (next_position, next_direction) not in visited:
                total_cost = cost + move_cost
                heapq.heappush(priority_queue, (total_cost, (next_position, next_direction)))

    return float('inf')  # If no path found

def main():
    maze = parse_input('input.txt')
    start, end = find_positions(maze)
    lowest_score = a_star(maze, start, end)
    print(f"The lowest score a Reindeer could possibly get: {lowest_score}")

if __name__ == "__main__":
    main()
