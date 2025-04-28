import re
fhand=open('regex_sum_2205812.txt','r')
line=fhand.read()
y=re.findall('[0-9]+',line)
total=sum(int(number) for number in y)
print(total)
