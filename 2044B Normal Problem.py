def solve(string):
    string = list(string)
    string = string[::-1]

    for index in range(len(string)):
        if string[index] == 'p':
            string[index] = 'q'
        elif string[index] == 'q':
            string[index] = 'p'
        else:
            pass
    
    answer = ''
    for character in string:
        answer += character
    
    print(answer)

t = int(input())
for testcase in range(t):
    string = input()
    solve(string)