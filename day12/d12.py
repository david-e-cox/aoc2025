#!/usr/bin/python3
import parse as P
import numpy as np

# Read input file
#f=open('example.txt');
f=open('input.txt');
lines = f.read().splitlines();
f.close()
package = []
pkgSet  = []
area    = []
for l in lines:
    #print("_____ {}".format(l))
    if len(l)==0:
        pkgSet.append(np.array(package))
        package=[]
    elif l[-1]==":":
        ndx=int(l.split(':')[0])
    elif "x" in l:
        R = P.parse("{}x{}: {}",l)
        area.append( [ (int(R[0]),int(R[1])), [int(n) for n in R[2].split()] ] )
    else:
        package.append([1 if c=='#' else 0 for c in l])
        
def verifyInput(pkgSet,area):
    for pNdx in range(len(pkgSet)):
        print("Package No: {}".format(pNdx))
        for l in pkgSet[pNdx]:
            print("   {}".format(l))

    #for av in area:
    #   print("Dimensions {},  Packages {}".format(av[0],av[1]))

def unique_rotations(shape):
    rots = []
    for k in range(4):
        r = np.rot90(shape, k)
        if not any(np.array_equal(r, x) for x in rots):
            rots.append(r)
    r = np.flipud(shape)
    if not any(np.array_equal(r, x) for x in rots):
        rots.append(r)    

    r = np.fliplr(shape)
    if not any(np.array_equal(r, x) for x in rots):
        rots.append(r)
        
    return rots

partA = 0
partB = 0

verifyInput(pkgSet,area)

rots = unique_rotations(pkgSet[0])
print(rots)

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


