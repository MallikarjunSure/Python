if(5>10):
    print("yes")
else:
    print("no")
age1=int(input('Enter the age1='))
age2=int(input('Enter age2='))
if(age1>age2):
    age3=age1+age2
    print('My age is added=',age3)
else:
    age3=age1-age2
    print('My age is substracted=',age3)
    

emailid="suremallikarjun2@gmail.com"
password=12456789
#otp=24
email_id=str(input('Enter the emailid='))
pass_word=int(input('Enter the password='))
#ot_p=int(input('enter the otp='))

#if(email_id is not email_id and pass_word is not password):
if(email_id==emailid):
    if(pass_word==password):
        print('login successful')
                            #if(ot_p==otp):
                               #''' print('otp is correct')
                            #else:
                                #print('Incorrect otp')
    else:
        print('login faild becz password is wrong')
else:
    print('login faild becz emailid is wrong')
#else:
 #    print('login faild becz emailid and passwoeerd are wrong')
    
    
