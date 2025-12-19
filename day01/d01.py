#!/usr/bin/python3
        
# Read input file
#f=open('example.txt');
f=open('input.txt');
lines = f.read().splitlines();
f.close()
partA = 0
partB = 0

# ---------- Part A
dial = 50
for l in lines:
    direc = l[0];
    dist  = int(l[1:])
    if (direc=='L'):
      dial -= dist
    elif (direc =='R'):
      dial += dist
    dial = dial%100
    if (dial==0):
      partA +=1

# ---------- Part B
dial = 50
for l in lines:      
    direc = l[0];
    dist  = int(l[1:])
    if (direc=='L'):
        q,r = divmod(dist,100);
        if (r>=dial and dial!=0):
            q+=1
        partB += q;
        dial -= dist
        dial = dial%100
    else:
        q,r = divmod(dist,100);
        if (r>=(100-dial)):
            q+=1
        partB += q;
        dial += dist
        dial = dial%100
               
print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


