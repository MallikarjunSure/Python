banana=[10,'malli',2545.78,'z']
print(banana)
print(banana[1])

for i in banana:
    print(i)
print()
    
pineapple=[10,'malli',25451.78,'z']
print(pineapple)
print(pineapple==banana)
print()

shetty=[]
n=int(input('Enetr the list size='))
for i in range(0,n):
    ele=int(input('Enter the elements:'))
    shetty.append(ele)
print(shetty)
print()

nagaraj=[10,30,84,64]
yuvaraj=[20,50,25,23]
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