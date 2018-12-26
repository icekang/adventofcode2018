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

time = 0
order = list()
workers = [0 for i in range(5)]
workersA = ['' for i in range(5)]
while len(con) != 0 or sum(workers) != 0:
    for i in range(5):
        if workers[i] == time:
            order.append(workersA[i])
            for a in con:
                if workersA[i] in con[a]:
                    con[a].remove(workersA[i])
            workersA[i] = ''
            workers[i] = 0
    insertA = list()
    for a in con:
        if len(con[a]) == 0:
            for i in range(5):
                if workers[i] == 0:
                    workers[i] = time + ord(a) - ord('A') + 1 + 60
                    workersA[i] = a
                    insertA.append(a)
                    #print(i, a)
                    break
    for a in insertA:
        con.pop(a)
    #print(workersA)               
    time += 1
print(''.join(order))
print('Used: ', time - 1)
