numbers=[0,1,0,3,12]
left=0
for right in range(len(numbers)):
    if numbers[right]!=0:
        numbers[left],numbers[right]=numbers[right],numbers[left]
        left+=1
print(numbers)

#or using extra list
numbers=[0,1,0,3,12]
result=[]
for num in numbers:
    if num!=0:
        result.append(num)
for num in numbers:
    if num==0:
        result.append(num)
print(result)

#0r- using list comprehension
numbers=[0,1,0,3,12]
non_zeros=[num for num in numbers if num!=0]
zeros=[num for num in numbers if num==0]
result=non_zeros+zeros
print(result)



