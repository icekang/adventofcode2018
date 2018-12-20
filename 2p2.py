n = input().strip()
list_n = []
found = False
while n != 'end':
    list_n.append(n)
    n = input().strip()
    
for box_id in list_n:
    for other_box_id in list_n:
        count = 0
        i = 0
        if box_id == other_box_id:
            continue
        else:
            while i < len(box_id):
                if box_id[i] != other_box_id[i]:
                    count += 1
                    saved_i = i
                if count > 1:
                    break
                i += 1
            if count == 1:
                found = True
                print("The ans is: ", box_id[:saved_i] + box_id[saved_i + 1:])
                break
    if found:
        break
