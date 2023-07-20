import sys


def split(s):
    splits = [0]
    for i in range(len(s)):
        if s[i].isupper():
            splits.append(i)
    splits.append(-1)
    new_string = []
    for i in range(len(splits) - 1):
        new_string.append(s[splits[i]:splits[i + 1]])
    new_string[-1] += s[-1]
    return " ".join(new_string).lower().strip()


def merge(s):
    new_string = ""
    s = s.split(" ")
    new_string += s[0]
    for i in range(1, len(s)):
        new_string += s[i].capitalize()
    return new_string.strip()


lines = sys.stdin.readlines()

for s in lines:
    s = s.split(";")

    if s[0] == "S":
        if s[1] == "M":
            s[2] = s[2][:-2]
            print(split(s[2]).strip())

        elif s[1] == "V":
            print(split(s[2]).strip())
        elif s[1] == "C":
            print(split(s[2]).strip())
        else:
            pass

    elif s[0] == "C":
        if s[1] == "M":
            s[2] = merge(s[2])
            s[2] = s[2].strip()
            s[2] += "()"
            print(s[2].strip())
        elif s[1] == "V":
            s[2] = merge(s[2])
            print(s[2].strip())
        elif s[1] == "C":
            s[2] = merge(s[2])
            print((s[2][0].upper() + s[2][1:]).strip())
        else:
            pass
