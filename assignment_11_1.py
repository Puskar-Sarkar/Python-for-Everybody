import re
with open('regex_sum_2205812.txt','r') as file:
    text=file.read()
y=re.findall(r'[0-9]+',text)
total=sum(int(number) for number in y)
print(total)
