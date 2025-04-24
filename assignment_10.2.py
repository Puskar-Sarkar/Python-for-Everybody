name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts=dict()
wds=list()
for line in handle:
    line=line.rstrip()
    if line.startswith('From '):
        y=line.split(':')
        z=y[0].split()
        x=z[5]         
        for m in x[0]:
            wds.append(x)

for w in wds:
    counts[w]=counts.get(w,0)+1
           
for k,v in sorted(counts.items()):
    print(k,v)
            
          
