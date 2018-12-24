class Point:
    def __init__(self,point):
        self.x = point[0]
        self.y = point[1]
    def __repr__(self):
        return "("+str(self.x)+", "+str(self.y)+")"
    def __str__(self):
        return "Point"+"("+str(self.x)+", "+str(self.y)+")"
    def area(self):
        area = 0
        for x in range(map_x0, map_x1 + 1, 1):
            for y in range(map_y0, map_y1 + 1, 1):
                #print(x,y)
                nearest = True
                hl = hlen((x,y), (self.x,self.y))
                for xy in points_list:
                    if hlen((x,y), (xy[0], xy[1])) <= hl and xy[0] != self.x and xy[1] != self.y:
                        nearest = False
                        break
                if nearest:
                    area += 1
                if nearest and ( x == map_x0 or x == map_x1 or y == map_y0 or y == map_y1):
                    return 0
        return area                
points_list = list()
def hlen(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
def isConfined(point):
    U = False
    L = False
    R = False
    B = False
    #confine = list()
    for othP in points_list:
        if othP[0] == point[0] and othP[1] == point[1]:
            continue
        else:
            if othP[1] <= point[1] and othP[0] >= point[0]:
                #print(othP, 'B')
                if B:
                    if hlen(point, othP) < hlen(point, BP):
                        BP = othP
                else:
                    BP = othP
                    B = True
                continue
            if othP[1] >= point[1] and othP[0] <= point[0]:
                #print(othP, 'U')
                if U:
                    if hlen(point, othP) < hlen(point, UP):
                        UP = othP
                else:
                    UP = othP
                    U = True
                continue
            if othP[0] <= point[0] and othP[1] <= point[1]:
                #print(othP, 'L')
                if L:
                    if hlen(point, othP) < hlen(point, LP):
                        LP = othP
                else:
                    LP = othP
                    L = True
                continue
            if othP[0] >= point[0] and othP[1] >= point[1]:
                #print(othP, 'R')
                if R:
                    if hlen(point, othP) < hlen(point, RP):
                        RP = othP
                else:
                    RP = othP
                    R = True
                continue
    if B and U and L and R:
        #print(confine)
        p = Point(point)
        return (True, p)
    return (False, None)
'''getting points to list'''
n = input().strip()
while n != 'end':
    n = tuple(map(int, n.split(', ')))
    points_list.append(n)
    n = input().strip()
    
map_x0 = min(points_list, key = lambda t : t[0])[0]
map_x1 = max(points_list, key = lambda t : t[0])[0]
map_y0 = min(points_list, key = lambda t : t[1])[1]
map_y1 = max(points_list, key = lambda t : t[1])[1]

'''analysis with my geniusness'''
confined_points = list()
for point in points_list:
    #print(point, "+++++++++")
    res = isConfined(point)
    if res[0]:
        confined_points.append((-res[1].area(), str(res[1])))

confined_points.sort()
print(confined_points[0])
