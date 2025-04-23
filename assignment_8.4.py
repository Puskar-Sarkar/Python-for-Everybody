fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    x=line.split()
    for item in x:
        if item not in lst:
            lst.append(item)

lst.sort()
print(lst)
