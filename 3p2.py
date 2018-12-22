import numpy as np

#fabric = np.ndarray((10,10), dtype = "|S256")
fabric = [['' for i in range(2000)] for i in range(2000)]
#fabric = np.chararray((10,10), buffer = '')
pure = list()
impure = list()
n = input().strip().split()
while n[0] != 'end':
    eyedee = int(n[0][1:])
    if eyedee % 100 == 0: print("ID: ", eyedee)
    j,i = map(int, n[2][:len(n[2]) - 1].split(','))
    x,y = map(int, n[3].split('x'))
    for m in range(x):
        for n in range(y):
            if fabric[i+n][j+m] == '':
                fabric[i+n][j+m] = str(eyedee)
                if eyedee not in pure and eyedee not in impure:
                    pure.append(eyedee)
            else:
                impure.append(eyedee)
                if fabric[i+n][j+m] != 'X':
                    if int(fabric[i+n][j+m]) in pure:
                        pure.pop(pure.index(int(fabric[i+n][j+m])))
                    impure.append(int(fabric[i+n][j+m]))
                if eyedee in pure:
                    pure.pop(pure.index(eyedee))
                fabric[i+n][j+m] = 'X'
    n = input().strip().split()
print("None overlap id: ", pure)
