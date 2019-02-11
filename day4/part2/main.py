import re

claims = []

for line in open('input.txt'):
    s = line.strip()
    m = re.match(r'#\d+ @ (\d+),(\d+): (\d+)x(\d+)', s)
    left = int(m.group(1))
    top = int(m.group(2))
    wide = int(m.group(3))
    tall = int(m.group(4))

    claim = []

    for i in range(wide):
        top = int(m.group(2))
        for i in range(tall):
            claim.append("%sx%s" % (left, top))
            top += 1
        left += 1
    claims.append(claim)

clashed_claims = []

jrange = len(claims)

for i in range(len(claims)):
    jrange -= 1
    clash_count = 0
    # print(claims[i])

    for j in range(jrange):
        clash = set(claims[i]) & set(claims[i + j + 1])
        if len(clash) > 0:
            clashed_claims.append(i)
            clashed_claims.append(i + j + 1)

for i in range(len(claims)):
    if i not in clashed_claims:
        print(i + 1)

