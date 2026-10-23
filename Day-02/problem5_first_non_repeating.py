string='aabbcdd'
frequency={}
for char in string:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
for key,value in frequency.items():
    if value==1:
        print(f'first non-repeating character is {key}')
        break
else:
    print("No non-repeating character")