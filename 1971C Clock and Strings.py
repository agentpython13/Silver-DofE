def solve(a, b, c, d):
    array = [int(x) for x in range(min(a,b)+1, max(a,b))]
    if (c in array and d in array) or (c not in array and d not in array):
        print('NO')
    else:
        print('YES')

t = int(input())
for testcase in range(t):
    a, b, c, d = [int(x) for x in input().split()]
    solve(a, b, c, d)
