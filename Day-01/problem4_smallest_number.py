numbers=eval(input("Enter the list : "))
smallest=numbers[0]
for num in numbers:
    if num<smallest:
        smallest=num
print(f'the maximu number is {smallest}')