#Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. Only compress the string if it saves space.
from collections import defaultdict
inp = 'AAABCCDDDD'
d = defaultdict(int)
for i in inp:
    d[i] += 1
# print(d)
op = ''
for k,v in d.items():
    if v != 1:
        op += k + '' + str(v)
    else:
        op += k
print(op)
