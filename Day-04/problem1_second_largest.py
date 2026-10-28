numbers=[10,5,20,8,15]
largest=float('-inf')
second_largest=float('-inf')

for num in numbers:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num != largest:
        second_largest=num
if second_largest==float('-inf'):
    print('Second largest distinct numbers does not exist')
else:
    print("Second largest",second_largest)