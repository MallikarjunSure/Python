# List is a muttable means value of index can be changed
apple=[10,20,30,40,50]
print(apple)
print(apple[1])
print(apple[-2])
#print(apple[4])
#print(apple[-4])
print("for iteration via access elements")
for i in apple:
    print(i)
print('after changed')
apple[1]=-99
print(apple)
apple[2]=(300,200)
print(apple)
print(apple[-1])
apple[3]=500,800,900
print(apple[3])
print(apple)
apple[1:4]=(564,789,123,456,999,111)  #list is not a fixed length it is a varing and here dynamically added extra index values and values are appended.
print(apple)
print(apple.index(456))
print(apple[5])
print()


college=list({10,20,30,40,50,60,70,80,90,100})
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
college[2]=200
print(college)




