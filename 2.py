n = ''
two = 0
three = 0

while n != 'end':
    n = input().strip()
    l = sorted(n)
    ss = ''.join(l) #string of sorted letters
    ls = set(l) #distinct letter of letters
    
    #FIND TWO AND THREE
    countedTwo = False
    countedThree = False
    for letter in ls:
        i = j = ss.find(letter)
        count = 0
        while j < len(ss) and ss[i] == ss[j]:
            count += 1
            j += 1
        if count == 2 and not countedTwo:
            #print(n, "TWO")
            countedTwo = True
            two += 1
        elif count == 3 and not countedThree:
            countedThree = True
            #print(n, "THREE")
            three += 1
print("The answer is ", two * three)
