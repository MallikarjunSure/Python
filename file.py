#fileptr=open("malli.txt","r")

#fileptr=open("mango.txt","x")
fileptr1=open("mango.txt","a")
#content=fileptr.read(15)
fileptr1.write("mango city")
print(fileptr1)

if fileptr1:
    print("file is oppened successfully")
    

fileptr1.close()
    


    