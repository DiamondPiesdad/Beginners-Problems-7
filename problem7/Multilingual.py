numberofpeople=int(input("how many people"))
s=set()
l=[]
li=[]
for people in range(numberofpeople):
    numberoflanguage=int(input("how many language can he speak"))
    for language in range(numberoflanguage):
        languageinput=input("what language can he speak")
        s.add(languageinput)
        l.append(languageinput)
for lan in s:
    n=0
    for la in l:
        if la==lan:
            n+=1
    if n==numberofpeople:
        li.append(lan)
print("Number of languages everyone speaks:",len(li))
print("Spoken language(s) everyone speaks:",', '.join(li))
print("Total languages spoken in the group: ",len(s))
print("Languages spoken:",', '.join(s))