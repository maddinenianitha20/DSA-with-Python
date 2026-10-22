numbers=[10,10,20,30,30,67,67,89]
seen=set()
duplicates=set()
for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print(sorted(duplicates))

# or
l=[10,34,56,56,7,8,8,9,9,10]
frequency={}
d=[]
for i in l:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)
for i in frequency:
    if frequency[i]>1:
        d.append(i)
print(d)


