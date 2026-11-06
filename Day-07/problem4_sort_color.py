numbers=[2,0,2,1,1,0]
low=0
mid=0
high=len(numbers)-1
while mid<=high:
    if numbers[mid]==0:
        numbers[low],numbers[mid]=numbers[mid],numbers[low]
        low+=1
        mid+=1
    elif numbers[mid]==1:
        mid+=1
    else:
        numbers[mid],numbers[high]=numbers[high],numbers[mid]
        high-=1
print(numbers)
#Approch2
numbers=[2,0,2,1,1,0]
ones=numbers.count(1)
zeros=numbers.count(0)
twos=numbers.count(2)
numbers=[0]*zeros+[1]*ones+[2]*twos
print(numbers)
#Approch3
numbers=[2,0,2,1,1,0]
numbers.sort()
print(numbers)