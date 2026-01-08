#!/usr/bin/python3
from collections import defaultdict

# Read input file
#f=open('example.txt');
#f=open('exampleb.txt');
f=open('input.txt');
lines = f.read().splitlines();
f.close()
partA = 0
partB = 0
nodeParent = defaultdict(list)


# Chat-GPT wrote most of this
# It tried, very patiently, to explain it to me
# I kind-of got it, but not well enought to add comments
def compute_reachability(graph):
    reach = {}

    for start in graph:
        stack = [start]
        visited = set()

        while stack:
            n = stack.pop()
            if n in visited:
                continue
            visited.add(n)
            for nxt in graph.get(n, []):
                stack.append(nxt)

        reach[start] = visited

    return reach


def dfs_iterate(G,v,target):
    S        = [(v, [v])]
    reach = compute_reachability(G)
    reach['out']=set()
    
    pathCnt=0
    while S:
        v,path    = S.pop()
        neighbors = T.get(v,[])

        if v == target:
            pathCnt+=1

        if not target in (reach[v]):
            continue

        for nxt in reversed(neighbors):
            if nxt in path:
                continue
            
            S.append( (nxt, path+[nxt]) )

    return pathCnt


T=dict()
for l in lines:
    kvp = l.split(':')
    T[kvp[0]]= kvp[1].strip().split(' ')

    
partA = dfs_iterate(T,'you','out')

# Compute sub-sections, total from product of paths
# The svr->dac and dac->fft paths were empty
pcPartB_3 = dfs_iterate(T,'dac','out')
pcPartB_2 = dfs_iterate(T,'fft','dac')
pcPartB_1 = dfs_iterate(T,'svr','fft')
partB = pcPartB_1*pcPartB_2*pcPartB_3

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


