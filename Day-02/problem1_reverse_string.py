text='python'
characters=list(text)
# print(characters)

left=0
right=len(characters)-1

# print(l[left])
# print(l[right])

while left<right:
    characters[left],characters[right]=characters[right],characters[left]
    left+=1
    right-=1

res="".join(characters)

print("reversed string is :",res)