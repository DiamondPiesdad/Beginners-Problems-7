l=[1,3,8,35,4,2,3]
s=set()
for x in l:
    if x in s:
        print("Yes")
    else :
        s.add(x)
        print("No")