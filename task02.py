import sys
import numpy as np

a, b = map(int, sys.stdin.readline().split())

assert 0 <= a <= 10000000
assert 0 <= b <= 10000000

ta = [int(sys.stdin.readline()) for _ in range(a)]
tb = [int(sys.stdin.readline()) for _ in range(b)]

pivot_num = 0


to_sort = np.unique(ta + tb)
sorted_lst = sorted(to_sort)

for nm in sorted_lst:
  print(nm)