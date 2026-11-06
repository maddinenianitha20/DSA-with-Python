numbers=[-1,0,1,2,-1,-4]
numbers.sort()
result=[]
for i in range(len(numbers)-2):
    if i>0 and numbers[i]==numbers[i-1]:
        continue
    left=i+1
    right=len(numbers)-1
    while left<right:
        total=numbers[i]+numbers[left]+numbers[right]
        if total<0:
            left+=1
        elif total>0:
            right-=1
        else:
            result.append([numbers[i],numbers[left],numbers[right]])
            left+=1
            right-=1
            while left<right and numbers[left]==numbers[left-1]:
                left+=1
            while left<right and numbers[right]==numbers[right+1]:
                right-=1
print(result)
