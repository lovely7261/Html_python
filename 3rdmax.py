numbers=[8,6,3,1,4,7,9]
s=numbers[1]
i=0
new=[]
while i<len(numbers):
    m=numbers[i]
    if m>s:
        s=m
        new.append(s)
    i=i+1
numbers.remove(s)
k=0
j=numbers[1]
while k<len(numbers):
    a=numbers[k]
    if a>j:
        j=a
        new.append(i)
    k=k+1
for i in new:
    print(i)