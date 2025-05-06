def solve(x, y):
    array = []
    array.append(min(x,y))
    array.append(max(x,y))
    print(*array)

t = int(input())
for testcase in range(t):
    x, y = [int(x) for x in input().split()]
    solve(x, y)
