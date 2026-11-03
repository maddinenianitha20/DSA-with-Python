l=[12,45,67,34,23]
largest=float('-inf')
second_largest=float('-inf')
for num in l:
    if num>largest:
        largest=num
        second_largest=largest
    elif num>second_largest and num!=largest:
        second_largest=num
largest_sum=largest+second_largest
print("Largest sum:",largest_sum)