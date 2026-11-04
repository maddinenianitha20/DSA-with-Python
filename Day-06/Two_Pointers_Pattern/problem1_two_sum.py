numbers=[1,2,4,6,8,9]
target=11
left=0
right=len(numbers)-1
while left<right:
    total=numbers[left]+numbers[right]

    if total==target:
        print("Pair found",numbers[left],numbers[right])
        break
    elif total<target:
        left+=1
    else:
        right-=1
#approch-2 : Brute-Force Approch
numbers=[1,2,4,6,8,9]
target=11
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]+numbers[j]==target:
            print(numbers[i],numbers[j])
            break

#approch-3 : Hashing(using set)
numbers=[1,2,4,6,8,9]
target=11
seen=set()
for num in numbers:
    remaining=target-num
    if remaining in seen:
        print(remaining,num)
        break
    seen.add(num) 



