
from itertools import combinations
data = open("C:\\Users\\pri\\Desktop\\sample.txt").read().strip().splitlines()
w, h = len(data[0]), len(data)
map = [[c for c in row] for row in data]
galaxies = set((y, x) for y, l in enumerate(map) for x, c in enumerate(l) if c == "#")
expand_rows = [i for i in range(h) if set(map[i]) == {"."}]
expand_cols = [i for i in range(w) if set(map[r][i] for r in range(h)) == {"."}]

p1 = p2 = 0
p1_exp = 1
p2_exp = 1000000 - 1
for g1, g2 in combinations(galaxies, 2):
    y1, x1, y2, x2 = g1 + g2
    # get distance between galaxies
    p1 += abs(x1 - x2) + abs(y1 - y2)
    p2 += abs(x1 - x2) + abs(y1 - y2)
    # add extra (expanded) rows and cols
    p1 += sum([p1_exp for n in expand_rows if n in range(min(y1, y2), max(y1, y2))])
    p1 += sum([p1_exp for n in expand_cols if n in range(min(x1, x2), max(x1, x2))])
    p2 += sum([p2_exp for n in expand_rows if n in range(min(y1, y2), max(y1, y2))])
    p2 += sum([p2_exp for n in expand_cols if n in range(min(x1, x2), max(x1, x2))])
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")