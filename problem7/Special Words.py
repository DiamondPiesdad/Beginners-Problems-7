sentence="the quick brown fox jumps over the lazy dog"
words=sentence.split()
s=set()
for y in words:
    s.add(y)
print(len(s))
n=int(0)
for x in sentence:
    if x=="a":
        n+=1
print(n)