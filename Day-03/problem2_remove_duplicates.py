# remove duplicate characters while preserving the original order
text="Programming"
result=""
for char in text:
    if char not in result:
        result+=char
print(f'After removing duplicates in text : {result}')