#find the character that occurs most frequently in a string.
text="success"
frequency={}
for char in text:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
most_frequent = max(frequency,key=frequency.get)
print("Most frequent character:",most_frequent)
print("Frequency",frequency[most_frequent])