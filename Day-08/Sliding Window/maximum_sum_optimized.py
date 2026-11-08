numbers=[2,1,5,1,3,2]
k=3
current_sum=sum(numbers[:k])
max_sum=current_sum
for i in range(k,len(numbers)):
    current_sum=current_sum+numbers[i]-numbers[i-k]
    if current_sum>max_sum:
        max_sum=current_sum
print(max_sum)

