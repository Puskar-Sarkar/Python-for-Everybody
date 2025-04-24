name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts=dict()
z=list()
for line in handle:
    if line.startswith('From '):
        line=line.rstrip()
        x=line.split()
        z.append(x[1])
                
for w in z:
    counts[w]=counts.get(w,0)+1
                
maxcount=None
maxname=None
for key,value in counts.items():
    if maxcount is None or value>maxcount:
        maxcount=value
        maxname=key
        
print(maxname,maxcount)
