def isReactable(polymer, i):
    return abs(ord(polymer[i]) - ord(polymer[i + 1])) == 32

def reacts(polymer, i):
    polymer = polymer[:i] + polymer[i + 2:]
    return polymer

def remove(polymer, a):
    out_polymer = ''
    for i in polymer:
        if i == a or i == a.upper():
            continue
        else:
            out_polymer += i
    return out_polymer

def fullyReacts(polymer):
    i = 0
    iteration = 0
    while i < len(polymer) - 1:
        if iteration % 1000 == 0:
            print(iteration)
        if isReactable(polymer, i):
            polymer = reacts(polymer, i)
            i -= 1
            if i < 0:
                i = 0
        else:
            i += 1
        iteration += 1
    return polymer

polymer = input().strip()

d = dict()

for a in 'abcdefghijklmnopqrstuvwxyz':
    p = remove(polymer, a)
    p = fullyReacts(p)
    d[a] = len(p)

''' Find the shortest unit'''
minlen = 50000
minkey = ''
for k in d:
    if d[k] < minlen:
        minlen = d[k]
        minkey = k

print("Remaining length of Polymer: ", minlen)
