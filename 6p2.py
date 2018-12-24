points_list = list()
def hlen(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

n = input().strip()
while n != 'end':
    n = tuple(map(int, n.split(', ')))
    points_list.append(n)
    n = input().strip()
    
map_x0 = min(points_list, key = lambda t : t[0])[0]
map_x1 = max(points_list, key = lambda t : t[0])[0]
map_y0 = min(points_list, key = lambda t : t[1])[1]
map_y1 = max(points_list, key = lambda t : t[1])[1]

count = 0
iteration = 0
print((map_x1 + 1  - map_x0) * (map_y1 + 1 - map_y0))
for x in range(map_x0, map_x1 + 1, 1):
    for y in range(map_y0, map_y1 + 1, 1):
        xy = (x,y)
        iteration += 1
        #if iteration % 1000 == 0:
            #print(iteration)
        hlenTotal = 0
        for point in points_list:
            hlenTotal += hlen(point, xy)
            
        if hlenTotal < 10000:
            count += 1

print("Arean within 10000: ", count)
