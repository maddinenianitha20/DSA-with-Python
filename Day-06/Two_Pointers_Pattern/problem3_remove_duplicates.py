numbers=[1,1,2,2,3,4,4,5]
i=0
for j in range(i+1,len(numbers)):
    if numbers[i]!=numbers[j]:
        i+=1
        numbers[i]=numbers[j]
print(numbers[:i+1])

#Approch2: Brute Force (Using a new list)
numbers=[1,1,2,2,3,4,4,5]
unique=[]
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)

#solution3 : using set
numbers=[1,2,1,2,2,3,4,4,5]
unique=list(set(numbers))
print(sorted(unique))
