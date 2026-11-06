def two_sortedlists(lst1,lst2):
    i=0
    j=0
    result=[]
    while i<len(lst1) and j<len(lst2):
        if lst1[i]<lst2[j]:
            value=lst1[i]
            i+=1
        elif lst1[i]>lst2[j]:
            value=lst2[j]
            j+=1
        else:
            value=lst1[i]
            i+=1
            j-=1
        #Avoid Duplicates
        if not result or result[-1]!=value:
            result.append(value)
    while i<len(lst1):
        if result[-1]!=lst1[i]:
            result.append(lst1[i])
        i+=1
    while j<len(lst2):
        if result[-1]!=lst2[j]:
            result.append(lst2[j])
        j+=1
    return result
lst1=[1,2,3,4,4]
lst2=[4,5,5,6,7,7]
print(two_sortedlists(lst1,lst2))


            