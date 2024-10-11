'''
Question - Brightness Begins - https://codeforces.com/problemset/problem/2020/B
Concept - Only the blubs with number that is a perfect square will be off. All other blubs will be on.
Standard Puzzle of Doors
'''

import math
import sys
from heapq import *
 
input = lambda: sys.stdin.readline().rstrip('\r\n')
sint = lambda: int(input())
mint = lambda: map(int, input().split())
aint = lambda: list(map(int, input().split()))
 
def solve():
    n = sint()
    y = [[] for _ in range(n+1)]
    for _ in range(n):
        xi, yi = mint()
        y[xi].append(yi)
    
    res = sum(1 for ys in y if len(ys) > 1) * (n-2)
    
    for i in range(n-1):
        if y[i] and y[i+1] and y[i+2]:
            if 1 in y[i] and 0 in y[i+1] and 1 in y[i+2]:
                res += 1
            if 0 in y[i] and 1 in y[i+1] and 0 in y[i+2]:
                res += 1
 
    print(res)
 
for _ in range(sint()):
    solve()
