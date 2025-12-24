#!/usr/bin/python3


# Read input file
#f=open('example.txt'); stopAt=9
f=open('input.txt'); stopAt=999
lines = f.read().splitlines()
f.close()

# function to calculate linear distance (squared), 3D
def dist3sq(a,b):
    D=0
    for i in range(3):
        D+= (a[i]-b[i]) * (a[i]-b[i])
    return(D)

# Create list of junction box coordinatesa
xyzJ = []
for l in lines:
    xyzJ.append([ int(p) for p in l.split(',')])

# Create list with distance between all boxes and coordinates, sorted by distance
distInfo = [];
for i in range(len(xyzJ)):
    for j in range(i+1,len(xyzJ)):
        distInfo.append((dist3sq(xyzJ[i],xyzJ[j]),xyzJ[i],xyzJ[j]))
distInfo.sort()

circuits = []
#Step through connections, starting with nearest boxes
for i in range(len(distInfo)):
    a=distInfo[i][1]
    b=distInfo[i][2]
    afound=-1
    bfound=-1
    # Determine if current junction box is already in a circuit
    for j in range(0,len(circuits)):
        if a in circuits[j]:
            afound=j
        if b in circuits[j]:
            bfound=j

    # Several possibilities:
    # Both ends found, but different circuits -> connect and merge circuits
    if afound>=0 and bfound>=0 and afound!=bfound:
        circuits[afound] += [p for p in circuits[bfound]]
        circuits.pop(bfound)
    # One end found, append the other to existing circuit
    elif afound>=0 and bfound==-1:
        circuits[afound].append(b)
    # Other end found, connect first        
    elif bfound>=0 and afound==-1:
        circuits[bfound].append(a)
    # Neither end in existing circuits, start new circuit
    elif afound==-1 and bfound==-1:
        circuits.append([a,b])
    # Note: both ends already in same circuit => no-operation, not included in if/else
    
    # Termination criteria, part A
    if i==stopAt:
        lenVec = [len(c) for c in circuits];
        lenVec.sort(reverse=True)
        partA = 1
        for i in range(min(3,len(lenVec))):
            partA *= lenVec[i]

    # Termination criteria, partB (one circuit that contains all junction boxes)
    if len(circuits)==1 and len(circuits[0])==len(xyzJ):
        partB = a[0]*b[0]
        break
        
print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


