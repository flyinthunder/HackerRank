def watermelon(n):
    return n%2 == 0


if __name__ == '__main__':
    n = int(input())
    out = watermelon(n)
    if n == 2:
        print("NO")
    elif out:
        print("YES")
    else:
        print("NO")