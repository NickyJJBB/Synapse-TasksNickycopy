from itertools import combinations
lst=['0001','0011','0101','1011','1101','1111']#1,3,5,11,13,15
new_lst=[]
for i in lst:
    temp=int(i,2)
    new_lst.append(temp)

new_lst.sort()
a=[]
for r in range(1,len(new_lst)):
    for c in combinations(new_lst,r):
        a.append(c)
print(a)
diff=[]
for items in a:
    res=[i for i in new_lst if i not in items]
    c=abs(sum(res)-sum(items))
    diff.append(c)
    if c==0:
        break
print(diff)
print(f"Minimum difference: {sorted(diff)[0]}")
