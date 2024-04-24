names="malli sure"
vowels="aeiou"
print(names)
print(names[:])
print(names[2:])
print(names[-1:])
print(names[-5:-1])
print(names[::-1])    #reverse printing
result=[char for char in names if char in vowels ]
print(result)
sep='-'.join(names[::2])
print(sep)
for i in range(0,len(names)):
    if(i%3==0  and i!=0):
        print(i,end=' ')
r=[char for char in names if char in names[1:10:2]]
for i in r:
    print(i,end='-')
    

