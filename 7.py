con = dict() #condition
n = input().strip()
while n != 'end':
    nlist = n.split()
    a1 = nlist[1]
    a2 = nlist[7]
    if a2 not in con:
        con[a2] = list()
    if a1 not in con:
        con[a1] = list()
    con[a2].append(a1)
    n = input().strip()

numSteps = len(con)
print(numSteps)
order = list()
while numSteps != 0:
    notPreceeded = list()

    for a2 in con:
        if len(con[a2]) == 0:
            notPreceeded.append(a2)

    notPreceeded.sort()
    e = notPreceeded[0]
    order.append(e)
    con.pop(e)
    for a2 in con:
        if e in con[a2]:
            con[a2].remove(e)
    numSteps -= 1

print(''.join(order))
