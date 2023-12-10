import math
with open("C:\\Users\\pri\\Desktop\\sample.txt") as aoc:
    directions, paths = aoc.read().split('\n\n')
    paths = {i.strip():v[2:-1].replace(' ','').split(',')
             for i,v in (line.split('=') for line in paths.splitlines())}
    starts = [i for i in paths if i.endswith('A')]

def steps(s):
    c = 0
    while s[-1] != 'Z':
        d = directions[c%len(directions)]
        s = paths[s][d =='R']
        c += 1
    return c

print('part1', steps('AAA'))
print('part2', math.lcm(*map(steps,starts)))
