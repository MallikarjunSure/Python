#inside curlly bracesses u used any one comma that  considerd as set.

states={"goa","MP","UP","karnataka"}
print(states)
print(type(states))
print("looping through the set elements...")
for i in states:
    print(i)
    
    
set2={12}#if curlly bracesses has any value than it is set.
print(type(set2))

#set is a immuttable, unordered, duplicate removable.
set4={10,20,30,40,50,60,70,80,90}
print(set4)
    
set3={}    #if curlly braces is empty it is printed as 'dict'(dictionary)
print(type(set3))


teams=set(["mi","csk","rr"])
print("\nPrinting as it is....")
print(teams)
print("\n Adding other teams...")
teams.add("RCB")    #u can be able insert single element.
print(teams)
for i in teams:
    print(i)
teams.remove("csk")   #it removes or discard or delete  csk
print(teams)
teams.discard("rr")  #it discard or remove or delete rr
print(teams)
#teams.remove("aa")   #shows error becz there is no element like aa.
teams.discard("aa")  #doesnt show error and execute program doent terminate prgm.
teams.update("kkr","lsg")    #u can be able insert multiple element.
print(teams)
teams.pop()  #in displayed output last element is popout
print(teams)
teams.clear()  #deleting the entire elements in the set.
print(teams)


days1={"monday","tuseday","wednesday"}
days2={"thursday","friday"}
print(days1|days2)   #printing the union of the sets

days1={"monday","tuseday","wednesday"}
days2={"thursday","friday"}
print(days1.union(days2)) #printing the union of the sets.


days1={"monday","tuseday","wednesday"}
days2={"thursday","friday","monday"}  #if any one element is common it will print only one time.
print(days1.union(days2))   #printing the union of the sets.'''


set1={1,2,3}
set2={2,4,5}
set3={2,4,5}
#removes the duplicates elements
common_elements=set1.union(set2,set3)
#printing the common values
set1={1,2,3,5,6,8}
set2={2,4,5,7,5,2}
set3=set1.intersection(set2)
print(set3)

set1={1,2,3}
set2={2,4,5}
set3={2,4,5}
#removes the duplicates elements
common_elements=set1.intersection(set2,set3)
print(common_elements)



days1={"monday","tuseday","wednesday"}
days2={"thursday","friday","monday","wednseday"}
print(days1-days2)  #comparing ele of days1 and days2 and removing common elemnts from days1.

days1={"monday","tuseday","wednesday"}
days2={"thursday","friday","monday","wednesday"}
print(days2-days1)  #comparing ele of days1 and days2 and removing common elemnts from days2.



days1={"monday","tuseday","wednesday"}
days2={"thursday","friday","monday","wednesday"}
print(days1.difference(days2))   #prints the differnce of the two sets days1 and days2 and printing the days1 differnece elements.


days1={"monday","tuseday","wednesday"}
days2={"thursday","friday","monday","wednesday"}
print(days2.difference(days1))   #prints the differnce of the two sets days1 and days2 and printing the days2 differnece element



days1={"monday","thursday","wednesday","friday"}
days2={"thursday","monday","wednesday"}
days3={"sunday","malli","harish"}
#days1 is the supperset of days2 hence it will print true
print(days1>days2)
#prints false since days1 is not the subset of days2
print(days1<days2)
#prints false days2 and days3 are not equivalent
print(days2==days3)
