numbers=[-4,-1,0,3,10]
result=[0]*len(numbers)
left=0
right=len(numbers)-1
position=len(numbers)-1
while left<right:
    if abs(numbers[left])>abs(numbers[right]):
        result[position]=numbers[left]**2
        left+=1
    else:
     
        result[position]=numbers[right]**2
        right-=1
    position-=1
print(result)

#Approch2-BruteForce
numbers=[-4,-1,0,3,10]
result=[]
for num in numbers:
    result.append(num**2)
result.sort()
print(result)

