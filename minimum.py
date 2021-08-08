a=[180,8,12,32,46,89,9,18,100]
min=a[0]
i=0
while i<len(a):
    if a[i]<min:
        min=a[i]
    i=i+1
print(min)
