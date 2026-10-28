numbers=[1,2,3,5]
n=len(numbers)+1
expected_sum = n*(n+1)//2
actual_sum=sum(numbers)
missing_number =expected_sum-actual_sum
print("missing number is",missing_number)

#or -using set
numbers=[1,2,3,5]
n=len(numbers)+1
numbers_set=set(numbers)
# print(numbers_set)
for i in range(1,n+1):
    if i not in numbers_set:
        print("Missing number",i)
        break

#or - using a loop
numbers=[1,2,3,5]
n=len(numbers)+1

expected_sum=0
for i in range(1,n+1):
    expected_sum+=i
actual_sum=0
for num in numbers:
    actual_sum+=num
missing_number =expected_sum-actual_sum
print("missing number is",missing_number)

