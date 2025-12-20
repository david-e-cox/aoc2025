#!/usr/bin/python3
        
# Read input file
#f=open('example.txt')
f=open('input.txt')
lines = f.read().splitlines()
f.close()


def removeRolls(map):
    # Adjacent positions
    adj = [ (-1,-1), (-1,0), (-1,1),  (0,-1), (0,1),  (1,-1), (1,0), (1,1) ]

    nRows = len(map)
    nCols = len(map[0])
    newMap = [ [map[j][i] for i in range(nCols)] for j in range(nRows)]
    movable=0

    for row in range(0,nRows):
        for col in range(0,nCols):
            # Only process spaces with paper roll
            if map[row][col]!="@":
                continue

            cnt=0
            # Check all adjacent spaces
            for delta in adj:
                ndx1 = row+delta[0]
                ndx2 = col+delta[1]
                # Check boundaries
                if ndx1<0 or ndx1>=nRows or  ndx2<0 or ndx2>=nCols:
                    continue
                # Count up adjacent paper rolls
                if map[ndx1][ndx2] == "@":
                    cnt +=1
                # If less the four, mark for early removal
            if cnt<4:
                movable +=1
                newMap[row][col] = "."  # Mark roll as removed in newMap
    return movable,newMap




partA = 0
partB = 0

# Form input map as 2-D array will be updated in removeRolls
map = [ [lines[c][r] for r in range(0,len(lines[0]))] for c in range(0,len(lines))]
partA, newMap = removeRolls(map)

# Continue removing rolls while possible
partB    = partA
newCount = partA
while(newCount>0):
    newCount, newMap = removeRolls(newMap)
    partB += newCount

# Dispay map
#for i in range(len(newMap)):
#    print("".join(newMap[i]))

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


