#!/usr/bin/python3

# Read input file
#f=open('example.txt')

f=open('input.txt')
lines = f.read().splitlines()
f.close()

partA = 0
partB = 0
foodId  = [];
rawLow  = [];
rawHigh = []

def  addNewRange(rawLow,rawHigh):
    # Add new low/high pair, checking for overlap with
    # existing low/high ranges

    # Initial Range
    comboLow  = [rawLow[0] ]
    comboHigh = [rawHigh[0]]

    # Check for overlap, if so update low/high endpoints
    for i in range(1,len(rawLow)):
        overlap=False
        for j  in range(0, len(comboLow)):
            low  = rawLow[i];
            high = rawHigh[i]
            # intersections and overlay
            if low <= comboLow[j]  and high >= comboLow[j]:
                comboLow[j] = low  # Push down bottom end
                overlap=True
            if high >= comboHigh[j] and low <= comboHigh[j]:
                comboHigh[j] = high
                overlap=True
            if low >= comboLow[j] and high <= comboHigh[j]:
                overlap=True

        # If there is no overlap, append as new range
        if (not overlap):
            comboLow.append(low)
            comboHigh.append(high)
        
    return comboLow,comboHigh




# Parse input
cnt=0
while (len(lines[cnt])>0):
    tmp=lines[cnt].split('-')
    rawLow.append(int(tmp[0]))
    rawHigh.append(int(tmp[1]))
    cnt=cnt+1

for i in range(cnt+1,len(lines)):
    foodId.append(int(lines[i]))

# Create low/high list
N=len(rawLow)
comboLow,comboHigh = addNewRange(rawLow,rawHigh)
Nred = len(comboLow)
    
# As range extension for overlap may have created new overlaps
# reprocess list until the number of entries stabilizes
cnt=0
while (Nred<N):
    N = len(comboLow)
    comboLow,comboHigh = addNewRange(comboLow,comboHigh)
    Nred = len(comboLow)

#  Check id in range, partA
for id in foodId:
    for i in range(0,len(comboLow)):
        if id>=comboLow[i] and id<=comboHigh[i]:
            partA +=1;

# Compute number of fresh IDs, partB
for i in range(0,len(comboLow)):
    partB += comboHigh[i]-comboLow[i]+1

      
print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


