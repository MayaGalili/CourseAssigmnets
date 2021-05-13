# Feel free to change anything in this code, e.g.
# add or remove variables and functions. If you don't
# like it, you can delete it and start from scratch.

import sys

MAX_VAL = 50
MIN_VAL = 1

# n = int(sys.stdin.readline())
n = 3

assert n <= MAX_VAL
assert n >= MIN_VAL

res = ""
i = MIN_VAL
for i in range(MIN_VAL, n ** 2+1):
    res += str(i)
    if i % n == 0:
        res +='\n'
    else:
        res += ' '

print('*****************************************')
print(res)
