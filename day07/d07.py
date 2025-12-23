#!/usr/bin/python3

# Read input file
#f=open('example.txt')
f=open('input.txt')
lines = f.read().splitlines()
f.close()

beamMap=[]
for l in lines:
    beamMap.append([c for c in l])
    
partA = 0
partB = 0

def showBeam(beamMap):
    for r in beamMap:
        print("".join(r))

def flowBeam(beamMap):
    splitCnt=0;
    rowNdx = 0
    startNdx = beamMap[0].index('S')
    beamMap[1][startNdx]='|'
    rowNdx+=1
    while (rowNdx<len(beamMap)-1):
        beamCols = [i for i,c in enumerate(beamMap[rowNdx]) if c=='|']
        for bc in beamCols:
            if beamMap[rowNdx+1][bc]=='.':
                beamMap[rowNdx+1][bc]='|'
            elif beamMap[rowNdx+1][bc]=='^':
                beamMap[rowNdx+1][bc-1]='|'
                beamMap[rowNdx+1][bc+1]='|'
                splitCnt+=1
        rowNdx +=1
    return splitCnt
            
                
def countTimelines(beamMap):
    # Initialize.  One beam at S in row zero
    timelineCnt = [ 0 for i in range(len(beamMap[0]))]
    timelineCnt[beamMap[0].index('S')] = 1

    # Check every row, apply splitters and pass-through beams
    for rowNdx in range(1,len(beamMap),1):
        # Find index of splitters
        splitters = [i for i,c in enumerate(beamMap[rowNdx]) if c=='^']
        # find all locations with beams
        fromNdx = [ i for i in range(len(timelineCnt)) if timelineCnt[i] != 0]
        # from every existing beam, create new beams around spliters when hit
        for locFr in fromNdx:
            for s in splitters:
                if locFr==s:  #hit splitter, two new beams, existing beam propagation stops
                    timelineCnt[locFr-1] += timelineCnt[locFr]
                    timelineCnt[locFr+1] += timelineCnt[locFr]
                    timelineCnt[locFr]    = 0

        #print("Iteration {:02d}/{}  beams = {}  count = {}".format(rowNdx,len(beamMap),timelineCnt,sum(timelineCnt)))

    # At last ruw the sum of beam counts from each column is the number of timelines
    return(sum(timelineCnt))
    
partA = flowBeam(beamMap)
partB = countTimelines(beamMap)

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


