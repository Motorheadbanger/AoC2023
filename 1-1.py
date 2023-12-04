shrimp = """"""


def solve():
    result = 0
    lines = shrimp.split("\n")

    for line in lines:
        first = search(line)
        last = search(line[::-1])
        result += int(first + last)

    print(result)


def search(line):
    lst = list(line)
    for char in lst:
        if "0" <= char <= "9":
            return char


solve()
