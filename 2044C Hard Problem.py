def solve(m, a, b, c):
    seated = 0
    total = 2 * m

    seated += min(a, m)
    seated += min(b, m)
    seated += min(c, total-seated)

    print(seated)

t = int(input())
for testcase in range(t):
    m, a, b, c = [int(x) for x in input().split()]
    solve(m, a, b, c)