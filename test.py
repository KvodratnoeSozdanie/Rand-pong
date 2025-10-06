a = [["" for _ in range(111)] for _ in range(111)]
b = "ТЫПИДОР"
c = 0
for i in range(111):
    for j in range(111):
        a[i][j] = b[c]
        c += 1
        if c == 7:
            c = 0
[print(*i) for i in a]