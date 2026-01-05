
from collections import Counter

with open('input.txt') as fin:
    initial_stones = [int(x) for x in fin.read().split()]

def simulate_blinks(stones_list, blinks):
    stones = Counter(stones_list)
    
    for _ in range(blinks):
        new_stones = Counter()

        for num, count in stones.items():
            if num == 0:
                new_stones[1] += count

            elif len(str(num)) % 2 == 0:
                s = str(num)
                mid = len(s) // 2
                left = s[:mid].lstrip('0') or '0'
                right = s[mid:].lstrip('0') or '0'
                new_stones[int(left)] += count
                new_stones[int(right)] += count

            else:
                new_num = num * 2024
                new_stones[new_num] += count

        stones = new_stones

    total_stones = sum(stones.values())
    return total_stones

result = simulate_blinks(initial_stones, 25)

print(result)
