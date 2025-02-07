#TestCases only
if __name__ == '__main__':
    n = int(input().strip())
    x = 0
    for _ in range(n):
        command = str(input().strip())
        if "++" in command:
            x += 1
        else:
            x -= 1
    print(x)