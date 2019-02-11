ids = []

for line in open('input.txt'):
    s = line.strip()
    ids.append(s)

for x in ids:
    for y in ids:
        diff = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                diff += 1
        if diff == 1:
            ans = []
            for i in range(len(x)):
                if x[i] == y[i]:
                    ans.append(x[i])
            print ''.join(ans)
