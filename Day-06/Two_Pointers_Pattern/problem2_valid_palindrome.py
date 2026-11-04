word='madam'
left=0
right=len(word)-1
while left<right:
    if word[left]!=word[right]:
        print("Not Palindrome")
        break
    left+=1
    right-=1
else:
    print("palindrome")

#Approch-2
word="teacher"
reversed_word=word[::-1]
if word == reversed_word:
    print("palindrome")
else:
    print("Not palindrome")
#Approch-3 using python Built-in Funtion
word='madam'
if word ==''.join(reversed(word)):
    print("palindrome")
else:
    print("Not palindrome")
