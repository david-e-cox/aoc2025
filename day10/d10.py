#!/usr/bin/python3
import re
import itertools
import pulp as p

# Read input file
#f=open('example.txt');
f=open('input.txt');
lines = f.read().splitlines();
f.close()

def runLights(ls,buttonList):
    newLightState = [x for x in ls]
    for btn in buttonList:
        for press in btn:
            newLightState[press] = not newLightState[press]
    return newLightState

# Used only to check pulp's solution
def runJolts(A,buttonList):
    newJoltState = [0 for i in range(len(A[0]))]
    for i in range(0,len(A[0])):
        for j in range (0,len(A)):
            newJoltState[i] += A[j][i]*buttonList[j]
    return newJoltState


partA = 0
partB = 0

lights=[]
wires=[]
jolts=[]

# Parse input
for l in lines:
    regex = r"\[[.#]+\]"
    M = re.findall(regex,l)
    lights.append(M[0][1:-1])

    regex = r"\([0-9,0-9]+\)"
    M = re.findall(regex,l)
    w = ( [ wp.replace('(','').replace(')','').split(',') for wp in M])
    S=[]
    for strList in w:
        S.append([ int(strVal) for strVal in strList])
    wires.append(S)
    
    regex = r"\{[0-9,]+\}"
    M = re.findall(regex,l)
    j = [ jt.replace('{','').replace('}','').split(',') for jt in M]
    for strList in j:
        jolts.append([int(strVal) for strVal in strList])

targetState=[]
for mp in lights:
    targetState.append([True if c=='#' else False for c in mp])

# Solve part A, exhaustively searching all possible combinations until one is found
pressInfoA = []
for panel in range(0,len(wires)):
    done=False
    for cnt in range(1,len(wires[panel])+1):
        if done:
            break
        lightState=[False for i in range(len(targetState[panel]))]
        for cKeypress in itertools.combinations(wires[panel],cnt):
            newLightState = runLights(lightState, cKeypress)
            if newLightState==targetState[panel]:
                lightStr = ['#' if lv else '.' for lv in newLightState]
                pressInfoA.append([len(cKeypress), cKeypress])
                done=True
                break
partA = sum([pi[0] for pi in pressInfoA])


# Much harder, button action is not boolean but accumlates a result
# Looks like a linear programming problem, using Python's pulp library
for panel in range(0,len(wires)):
    nWires = len(wires[panel])
    nJolts = len(jolts[panel])
    A=[]
    # Build matrix form for button press operations on joltages
    # newJoltState = A' * buttonsPress
    for j in range(nWires):
        A.append ([ 1 if i in wires[panel][j] else 0 for i in range(len(jolts[panel]))])

    # Setup linear programming problem, minimization of objective over integer unknowns
    P = p.LpProblem("partB",p.LpMinimize)
    x = p.LpVariable.dicts("x_var", range(nWires), lowBound=0, cat=p.LpInteger)

    # Problem constraints are equality with desired joltage
    for i in range(0,nJolts):
        P +=  p.lpSum( [ A[j][i]*x[j] for j in range(nWires) ] ) == jolts[panel][i]
    # Problem objective function is to minimize number of button presses
    P +=  p.lpSum( [x[j] for j in range(nWires)] )

    # Solve (note: example has different solutions, but equavlent cost)
    P.solve(p.PULP_CBC_CMD(msg=0))

    # Extract solution, accumulate totals over all wires
    xOpt = [int(p.value(x[i])) for i in range(nWires)]
    partB += sum(xOpt)


print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


