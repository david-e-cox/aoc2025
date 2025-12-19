#!/usr/bin/python3
        
# Read input file
#f=open('example.txt')
f=open('input.txt')
line = f.read()
f.close()
partA = 0
partB = 0

sku = line.split(',')
for entry in sku:
    str1,str2 = entry.split('-')
    low  = int(str1)
    high = int(str2)
    for v in range(low,high+1):
        vstr = str(v)
        l = len(vstr)

        # if sku is even, split in half check for repeat
        if l%2==0:
             if (vstr[0:int(l/2)] == vstr[int(l/2):]):
                 partA += v

        # check every possible pattern length (up to mid-length)
        for patLength in range(1,int(l/2)+1):
            inval=True
            # check initial pattern against all others in sku
            for startNdx in range(patLength, l-patLength+1, patLength):
                # just skip out if pattern length is not an integer multiple of sku length
                if l%patLength !=0:
                    inval=False
                    break
                # check initial pattern agains others, if any mismatch throw flag, skip out
                if (vstr[0:patLength] != vstr[startNdx:startNdx+patLength]):
                    inval=False
                    break
            # if invalid, increment total advance to next sku
            if ( inval ):
                partB += v
                break

                
print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


