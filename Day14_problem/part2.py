from typing import List, Tuple, Set

def parse_input(filename: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Parse input file to extract robot positions and velocities.

    Args:
        filename (str): Path to input file

    Returns:
        List of tuples, each containing (position, velocity)
    """
    robots = []
    with open(filename, 'r') as f:
        for line in f:
            pos_str, vel_str = line.strip().split(' ')
            px, py = map(int, pos_str[2:].split(','))
            vx, vy = map(int, vel_str[2:].split(','))
            robots.append(((px, py), (vx, vy)))
    return robots

def simulate_positions(
    robots: List[Tuple[Tuple[int, int], Tuple[int, int]]],
    time: int,
    width: int,
    height: int
) -> Set[Tuple[int, int]]:
    """
    Simulate robot positions after the given time.

    Args:
        robots (List): List of robot (position, velocity) tuples
        time (int): Seconds to simulate
        width (int): Space width
        height (int): Space height

    Returns:
        Set of robot positions at the given time
    """
    positions = set()
    for (px, py), (vx, vy) in robots:
        final_x = (px + vx * time) % width
        final_y = (py + vy * time) % height
        positions.add((final_x, final_y))
    return positions

def is_christmas_tree(positions: Set[Tuple[int, int]]) -> bool:
    """
    Check if the robot positions form a Christmas tree pattern.

    Args:
        positions (Set): Set of robot positions

    Returns:
        Boolean indicating if a Christmas tree pattern is found
    """
    # Define the Christmas tree pattern as relative positions
    tree_pattern = [
        (0, 2), (1, 1), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 2),
        (4, 1), (4, 2), (4, 3)
    ]

    for x, y in positions:
        if all((x + dx, y + dy) in positions for dx, dy in tree_pattern):
            return True
    return False

def find_christmas_tree_time(filename: str, max_time: int = 10000, width: int = 101, height: int = 103) -> int:
    """
    Find the earliest time when robots form a Christmas tree pattern.

    Args:
        filename (str): Input file path
        max_time (int): Maximum time to search
        width (int): Space width
        height (int): Space height

    Returns:
        Time when Christmas tree pattern is found, or -1 if not found
    """
    robots = parse_input(filename)
    for time in range(max_time):
        positions = simulate_positions(robots, time, width, height)
        if is_christmas_tree(positions):
            return time
    return -1

# Solve problem
result = find_christmas_tree_time('input.txt')
print(f"Seconds until Christmas Tree Pattern: {result}")