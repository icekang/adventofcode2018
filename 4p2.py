class Guard:
    def __init__(self, n): #['[1518-11-02', '00:40]', 'falls', 'asleep']
        self.day = n[0][1:]
        self.time = n[1][:-1]
        self.id = int(n[3][1:])
        self.table = ['.' for i in range(60)]
    def __str__(self):
        return self.table
    def __repr__(self):
        return "#"+str(self.id)
    def fall(self, n):
        for i in range(int(n[1][:-1][3:]), 60, 1):
            self.table[i] = '#'
    def awake(self, time):
        for i in range(int(n[1][:-1][3:]), 60, 1):
            self.table[i] = '.'
    def timeFall(self):
        time = 0
        mFall = [0 for i in range(60)]
        minu = 0
        for i in self.table:
            if i == '#':
                time += 1
                mFall[minu] += 1
            minu += 1
        return time, mFall

l = list()
n = input().strip().split()
while n[0] != 'end':
    l.append(n)
    n = input().strip().split()

l.sort()

print("Start")
g = dict()
gnum = 0
for n in l:
    if n[2] == 'Guard':
        gnum = int(n[3][1:])
        if gnum not in g:
            g[gnum] = [Guard(n)]
        else:
            g[gnum].append(Guard(n))
            
    elif n[2] == 'falls':
        g[gnum][len(g[gnum]) - 1].fall(n)
    elif n[2] == 'wakes':
        g[gnum][len(g[gnum]) - 1].awake(n)

ll = list()
for gid in  g:
    l = list()
    for i in g[gid]:
        l.append(i.timeFall()[1])
    ll.append((l,gid))

    ll_res = list()
for l in ll:
    l_res = [0 for k in range(60)]
    for i in range(len(l[0])):
        for j in range(60):
            l_res[j] += l[0][i][j]
    ll_res.append((l_res,l[1]))
    
lm = list()
for l_res in ll_res:
    m = -1
    mindex = -1
    for i in range(len(l_res[0])):
        if l_res[0][i] > m:
            mindex = i
            m = l_res[0][i]
    lm.append((-m, mindex, l_res[1]))

lm.sort()
mindex = lm[0][1]
res_guard_id = lm[0][2]


print("ID of the guard you chose multiplied by the minute you chose: ", res_guard_id, " x ", mindex)
print(res_guard_id * mindex)
