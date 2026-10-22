numbers=[12,45,7,89,23]
frequency ={}
for num in numbers:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num]=1
for num,count in frequency.items():
    print(num,":",count)