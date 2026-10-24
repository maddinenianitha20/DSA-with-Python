#Find the unique characters that appear in both strings
first="hello"
second="world"
common=[]
for char in first:
    if char in second and char not in common:
        common.append(char)
print("Common Characters:",common)