def solve(a,b):
    arr = []
    for i in range(len(b)):
        arr.append(a.count(b[i]))
    return arr
