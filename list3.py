nagaraj=[10,25,37,40,57,65]
sum=0
for i in nagaraj:
    if i%10==7:
        print(i)
print()
        
nagaraj=[10,20,30,40,50]
sum=0
for i in nagaraj:
    sum+=i
    print(sum)
print()
    
nagaraj=[10,20,30,40,50]
sum=0
for i in nagaraj:
    sum+=i
print(sum)
print()


nagaraj=[10,20,30,40,50,30,50]
yuvaraj=[]
for i in nagaraj:
    if i not in yuvaraj:
        yuvaraj.append(i)
print(yuvaraj)


yuvaraj=[10,20,30,40,50]
nagaraj=[60,70,80,90,100,20]
for i in yuvaraj:
    for j in nagaraj:
        if i==j:
            print(i)



