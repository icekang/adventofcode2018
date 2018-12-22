import numpy as np

#fabric = np.ndarray((1100,1100))
fabric = np.zeros((2010,2010), dtype = int)

count = 0
n = input().strip().split()
while n[0] != 'end':
    j,i = map(int, n[2][:len(n[2]) - 1].split(','))
    x,y = map(int, n[3].split('x'))
    for m in range(x):
        for n in range(y):
            fabric[i+n][j+m] += 1
            if fabric[i+n][j+m] == 2:
                count += 1
    n = input().strip().split()
print("Overlap area: ", count, "sq.in")
