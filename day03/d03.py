#!/usr/bin/python3
        
# Read input file
#f=open('example.txt')
f=open('input.txt')
line = f.read().splitlines()
f.close()

partA = 0
partB = 0

# --------------- Part A -----------------------
for l in line:
    maxV=-1;
    for i in range(0,len(l)):
        # move on if 10's digit is not above max
        if (int(l[i])*10 < maxV):
            continue
        for j in range(i+1,len(l)):
            V = int(l[i]+l[j])
            if V>maxV:
                maxV = V
    partA += maxV


# --------------- Part B -----------------------
for l in line:
    # Create copy of line to start with
    lStr=l

    # Iterate until it's down to 12 digits
    while(len(lStr)>12):
        # Remove one digit, retain largest value
        maxV = -1
        for i in range(0,len(lStr)):
            V = int(lStr[0:i]+lStr[i+1:])
            if V > maxV:
                maxV = V;
        # Reassign lStr to maxV
        lStr=str(maxV)
    # lStr is down to 12 digits, add to sum
    partB += int(lStr)


print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


