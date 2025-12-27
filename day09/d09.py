#!/usr/bin/python3
from shapely.geometry import Polygon

# Read input file
#f=open('example.txt');
f=open('input.txt');
lines = f.read().splitlines()
f.close()

def areaIn(a,b):
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)


# Winding Algorithm for point in polygon
# This works, but doesn't solve the challenge problem
# Python's shapely library is well suited, used it instead
#def pointInPoly(Vertex,pt,failOnBoundary):
#    wn = 0
#    for i in range(len(Vertex)):
#        j = (i+1)%len(Vertex)
#        A = Vertex[i]; B = Vertex[j]  # poly edge from A->B
#        # Is point left of active polygon edge
#        isLeftCondition = ( (B[0]-A[0])*(pt[1]-A[1]) - (pt[0]-A[0])*(B[1]-A[1]) )
#        if isLeftCondition==0:
#            if pt[0]<=max([A[0],B[0]]) and pt[0]>=min([A[0],B[0]]) and pt[1]<=max([A[1],B[1]]) and pt[1]>=min([A[1],B[1]]):
#                if failOnBoundary:
#                    return False
#                else:
#                    return True
#
#        if A[1] <= pt[1]:
#           if (B[1] > pt[1]) and isLeftCondition > 0:
#               wn += 1
#        else:
#           if (B[1] <= pt[1]) and isLeftCondition < 0:
#               wn -= 1
#
#    if wn != 0:
#        return True
#    else:
#        return False
#

partA = 0
partB = 0

Vxy=[]
for i in range(len(lines)):
    Vxy.append([ int(c) for c in lines[i].split(',')])

# For every possible combination of corners
cPairs=[];
for i in range(len(Vxy)):    
    for j in range(i+1,len(Vxy)):
        # List of tuples, all corner pairs
        cPairs.append([ (Vxy[i][0],Vxy[i][1]) , (Vxy[j][0],Vxy[j][1]) ])

areaInfo_PartA = [];   # Contains area and pair of corners
for cp in cPairs:
    areaInfo_PartA.append( [areaIn(cp[0],cp[1]), cp] )

areaInfo_PartA.sort(reverse=True)   # Sort by area
partA = areaInfo_PartA[0][0]


areaInfo_PartB = []
cnt=0
P = Polygon( Vxy + [Vxy[0]] )
for cp in cPairs:
    cnt+=1
    # For every corner pair, interate on rectangle points
    # Skip if a rectangle vertex is not inside the polygon
    xRange = [cp[0][0], cp[1][0]]; xRange.sort()
    yRange = [cp[0][1], cp[1][1]]; yRange.sort()

    corners = [[xRange[0],yRange[0]],
               [xRange[1],yRange[0]],
               [xRange[1],yRange[1]],
               [xRange[0],yRange[1]]]
    R = Polygon(corners + [corners[0]])

    if (P.contains(R)):
        areaInfo_PartB.append([areaIn(cp[0],cp[1]),cp])

    if cnt%5000==0:
        print("Finished {}/{}, found {} rects".format(cnt,len(cPairs),len(areaInfo_PartB)))

areaInfo_PartB.sort(reverse=True)
partB = areaInfo_PartB[0][0]

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))

            

