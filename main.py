username=""
password=""
number=""
timer = [1,2,3,4,5,6,7,8,9]
def signIn():
    username= input("Enter your username : ")
    password=input("Enter your password: ")
    for x in timer:
        while x <6:
            x= x+1
            print("Authorizing... ",+ x)
    
    print("Your phone number is required for  more auth.")
    number= input("Enter your phone number: ")
    print("Done. ")
    
    print(f"Username: {username}, Password :{password}")

signIn()
    
def deleteAccount ():
    action = "Delete"
    print(action)
    
deleteAccount()
deleteAccount()
deleteAccount()