f = 0
n = input()
l = [0]
ll = []
found = False
while(n != 'a'):
    ll.append(int(n))
    f += int(n)
    n = input()
    if(f not in l):
        l.append(f)
    else:
        res = f
        found = True
        break
if (not found):
    print("WTF")
    while(not found):
        for i in ll:
            f += i
            if(f not in l):
                l.append(f)
            else:
                res = f
                found = True
                break
print('The ans is', res)


    
