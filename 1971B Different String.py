def solve(string):
    string = list(string)
    holder = string[0]
    for index in range(len(string)):
        print(index)
        if index == len(string)-1:
            string[index] = holder
        else:
            string[index] = string[index+1]
        print(string)
    print(''.join(string))

t = int(input())
for testcase in range(t):
    string = input()
    solve(string)