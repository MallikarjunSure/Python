for i in range(-10,10,2):
    print(i,end=' ')
    print(i+1,end=' ')
print()


college=(10,20,30,40,50,60,70,80,90,100)
print(college[1])
print(college[-1])
print(college[1:3])
print(college[1:7])
print(college[5])
print(college[:])
print(college[-4:-1])
print(college[3:-1])
print(college[:-1])
print(college[:0])
print(college[0:])
print(college[0:4:2])
print(college[0:4:3])
print(college[0:20:3])
'''college[2]=200'''  #this is immuttable becz we r using tuple
print(college)
print(college[2])
print()

banana=(10,'malli',2545.78,'z')
print(banana)
print(banana[1])
print()

for i in banana:
    print(i,end="-")
print()
    
pineapple=tuple([10,'malli',25451.78,'z'])
print(pineapple)
print(pineapple==banana)
print()


#in tuple , append is not working like below, but it has different syntax 
'''shetty=()
n=int(input('Enetr the list size='))
for i in range(0,n):
    ele=int(input('Enter the elements'))
    shetty.append(ele)  #it shows error
print(shetty)'''
