#Two strings are anagrams if they contain the same characters with the same 
#frequencies,even if the order differs
first="listen"
second="silent"
if sorted(first)==sorted(second):
    print('Anagrams')
else:
    print("Not Anagrams")