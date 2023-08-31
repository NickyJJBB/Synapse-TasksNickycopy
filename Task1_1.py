jumbled_superheroes=['DocTor_StrAnGe','sPIDerman','Moon_knIGHt','capTAin_AmerICa','huLK']
decoded_names=[]
indices=[]

for index,name in enumerate(jumbled_superheroes):
    indices.append(index)
    t=name.lower()
    decoded_names.append(t.replace("_"," "))

get_name_length=lambda n:len(n)
name_lengths=list(map(get_name_length, decoded_names))

def func1(x):
    return name_lengths[x]

indices.sort(key=func1)

def myfunc(n):
    return len(n)

decoded_names.sort(key=myfunc)
j=1
print("Phase 5 kickoff list :")
for i in decoded_names:
    print(f"{j}.",i.title())
    j+=1
