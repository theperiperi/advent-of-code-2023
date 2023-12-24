#!/usr/bin/env python3

import pathlib
import sys

from collections import deque

sys.path.append(str(pathlib.Path(__file__).resolve().parents[3] / 'lib' / 'python'))


def walk_from(map: list[str], x: int, y: int, max_steps: int) -> int:
  visited = {}
  mx, my = len(map[0]), len(map)

  q: deque[tuple[int, int, int]] = deque([(x, y, 0)])
  while q:
    x, y, steps = q.popleft()
    steps += 1

    if steps > max_steps:
      continue

    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
      if (nx, ny) not in visited and map[ny % my][nx % mx] != "#":
        visited[nx, ny] = steps
        q.append((nx, ny, steps))

  return sum(1 for x in visited.values() if x % 2 == max_steps % 2)

def run() -> None:
  with open("C:\\Users\\pri\\Desktop\\sample.txt") as f:
    input = f.read()

  max_steps = 64
  inf_steps = 26501365

  map = input.strip().splitlines()

  x, y = next((x, y) for y, row in enumerate(map) for x, c in enumerate(row) if c == 'S')
  print(f"Total plots reached in {max_steps} steps: {walk_from(map, x, y, max_steps)}")

  size = len(map)
  iterations, extra = divmod(inf_steps, size)

  f0, f1, f2 = (walk_from(map, x, y, size * i + extra) for i in range(0, 3))

  a = (f0 - 2 * f1 + f2) // 2
  b = f1 - f0 - a
  c = f0

  steps = a * iterations * iterations + b * iterations + c
  print(f"Total plots reached in {inf_steps} steps: {steps}")

if __name__ == '__main__':
  run()
  sys.exit(0)
