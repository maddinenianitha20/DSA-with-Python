string="banana"
frequency={}
for char in string:
    if char!=" ":
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
print(frequency)
for key,value in frequency.items():
    print(key ,":",value)