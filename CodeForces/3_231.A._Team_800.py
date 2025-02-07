#TestCases only
if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    problems = 0
    for _ in range(n):
        if sum(list(map(int, str(input().strip()).split(" ")))) >= 2:
            problems += 1
    print(problems)
