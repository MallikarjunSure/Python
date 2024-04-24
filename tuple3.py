nagaraj=tuple([10,30,84,64])
yuvaraj=tuple([20,50,25,23])
chinnu=nagaraj+yuvaraj
print(chinnu)
print(type(nagaraj))
print(type(yuvaraj))
print(type(chinnu))
print(chinnu*2)
print(len(chinnu))
print(max(chinnu))
print(min(chinnu))
print(max(nagaraj))
print(min(nagaraj))
print(max(yuvaraj))
print(min(yuvaraj))



nagaraj=(10,25,37,40,57,65)
sum=0
for i in nagaraj:
    if i%10==7:
        print(i)
print()
        
nagaraj=tuple([10,20,30,40,50])
sum=0
for i in nagaraj:
    sum+=i
    print(sum)
print()
    
nagaraj=(10,20,30,40,50)
sum=0
for i in nagaraj:
    sum+=i
print(sum)
print()

#in tuple , append is not working like below, but it has different syntax 
'''nagaraj=tuple([10,20,30,40,50,30,50])
yuvaraj=()
for i in nagaraj:
    if i not in yuvaraj:
        yuvaraj.append(i)
print(yuvaraj)'''


yuvaraj=(10,20,30,40,50)
nagaraj=(60,70,80,90,100,20)
for i in yuvaraj:
    for j in nagaraj:
        if i==j:
            print(i)
            
            
apple=(10,20,30,40,50)
print(apple)
print(apple[1])
print(apple[-2])
#print(apple[4])
#print(apple[-4])
print("for iteration via access elements")
for i in apple:
    print(i)
print('after changed')
'''apple[1]=-99     #it is immuttable
print(apple)
apple[2]=(300,200)
print(apple)
print(apple[-1])
apple[3]=500,800,900
print(apple[3])
print(apple)
apple[1:4]=(564,789,123,456,999,111)
print(apple.index(456))
print(apple[5])'''




