l=[23,34,45,45,56,78,34,23,45]
seen=[]
for i in l:
    if i not in seen:
        seen.append(i)
    else:
        print("first repeating character is:",i)
        break


