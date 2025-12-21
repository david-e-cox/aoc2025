#!/usr/bin/python3

# Read input file
#f=open('example.txt')

f=open('input.txt')
lines = f.read().splitlines()
f.close()

partA = 0
partB = 0

# --------- Part A ---------
# Extract list of operators
nVals = len(lines)-1
oper = lines[nVals].split()

# Extract values into array
vals=[]
for i in range(nVals):
    vec=[int(v) for v in lines[i].split()];
    vals.append(vec)

# Apply desired operation
for i in range(len(oper)):
    if oper[i]=="+":
        total=0
        for j in range(nVals):
            total += vals[j][i]
    else:
        total=1;
        for j in range(nVals):
            total *= vals[j][i]
# Sum for total
    partA += total



    
# --------- Part B ---------

# Create input data as 2-d array of characters
dataStr=[]
colVal =[[]];
for i in range(len(lines)-1):
    dataStr.append([c for c in lines[i]])

# Convert columns to numbers, skipping to new entry on a full column of spaces
for i in range(len(dataStr[0])):
    colStr = ""
    for j in range(len(dataStr)):
        colStr += dataStr[j][i]
    if all([c==" " for c in colStr]):
        colVal.append([])
    else:
        colVal[-1].append(int(colStr))

# Apply desired operation to column-numbers
for i in range(len(colVal)):
    if oper[i]=="+":
        total=0
        for v in colVal[i]:
            total += v
    else:
        total=1;
        for v in colVal[i]:
            total *= v
# Sum for solution                       
    partB += total

    
print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


