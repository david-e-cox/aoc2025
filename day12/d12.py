#!/usr/bin/python3
import parse as P
import numpy as np

# Read input file
#f=open('example.txt');
f=open('input.txt');
lines = f.read().splitlines();
f.close()
        
def verifyInput(pkgSet,area):
    for pNdx in range(len(pkgSet)):
        print("Package No: {}".format(pNdx))
        for l in pkgSet[pNdx]:
            print("   {}".format(l))
    for av in area:
       print("Dimensions {},  Packages {}".format(av[0],av[1]))

def parseInput(lines):
    package = []
    pkgSet  = []
    pkgSiz  = []
    area    = []
    for l in lines:
        #print("_____ {}".format(l))
        if len(l)==0:
            pkgSet.append(np.array(package))
            pkgSiz.append( (np.prod(pkgSet[-1].shape), np.sum(pkgSet[-1]) ) )
            package=[]
        elif l[-1]==":":
            ndx=int(l.split(':')[0])
        elif "x" in l:
            R = P.parse("{}x{}: {}",l)
            area.append( [ (int(R[0]),int(R[1])), [int(n) for n in R[2].split()] ] )
        else:
            package.append([1 if c=='#' else 0 for c in l])
    return pkgSet,pkgSiz,area

def unique_rotations(shape):
    # Include original shape
    rots = [shape]
    # Create shapes with package flipped about the vertical and horizontal
    shapeUD = np.flipud(shape)
    shapeLR = np.fliplr(shape)

    # Add in flipped shapes, unless symmetry makes them redundant
    if not any(np.array_equal(shapeUD, x) for x in rots):
        rots.append(shapeUD)    

    if not any(np.array_equal(shapeLR, x) for x in rots):
        rots.append(shapeLR)    

    # Add in rotations of shape (90,180,270) degs
    for k in range(1,4):
        r = np.rot90(shape, k)
        if not any(np.array_equal(r, x) for x in rots):
            rots.append(r)

    # Add in rotations of flipped shape (90,180,270) degs
    for k in range(1,4):
        r = np.rot90(shapeUD, k)
        if not any(np.array_equal(r, x) for x in rots):
            rots.append(r)

    # Add in rotations of flipped shape (90,180,270) degs
    for k in range(1,4):
        r = np.rot90(shapeLR, k)
        if not any(np.array_equal(r, x) for x in rots):
            rots.append(r)
    return rots

def verifyRotations(pkgSet):
    for pkg in pkgSet:
        rots = unique_rotations(pkg)
    print("Length of unique rotations: {}".format(len(rots)))
    for shape in rots:
        print()
        for l in shape:
            print(" {}".format(l))

            
partA = 0
partB = 0

pkgSet,pkgSiz,area = parseInput(lines)
#verifyInput(pkgSet,area)
#verifyRotations(pkgSet)

partA=0        
optSum=0
    
for a in area:
    room = a[0][0]*a[0][1]
    req=0
    opt=0

    for i in range(len(a[1])):
        opt += a[1][i] * pkgSiz[i][0]
        req += a[1][i] * pkgSiz[i][1]
  #  print("{}: {} {}/{}".format(a,room,req,opt))
    if req<=room:
        partA+=1

    if opt<=room:
        optSum+=1

print("Well Damn.... {}=={}".format(partA,optSum))

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


