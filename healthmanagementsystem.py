#health management system
def logdata():
    reg=input("Are you already registered? y for Yes and n for No : ")
    name=input("Please Enter your first name : ")
    
    if reg=='n':
        with open(name.strip()+'-ex.txt','w') as f:
            pass
        with open(name.strip()+'-diet.txt','w') as f:
            pass
        
    work=int(input('Enter 1 for diet and 2 for exercise : '))
    
    filename=f"{name}{'-ex.txt' if work==2 else '-diet.txt'}"
    with open(filename,'a') as f:
        f.write(gettime()+' '+input()+'\n')
    print("data added successfully")
def retrievedata():
    name=input("Please Enter your first name : ")
    work=int(input('Enter 1 for diet and 2 for exercise : '))
    filename=f"{name}{'-ex.txt' if work==2 else '-diet.txt'}"
    with open(filename,'r') as f:
        print(f.read())
    print("data successfully printed")
def gettime():
    import datetime
    return str(datetime.datetime.now())

n=int(input("Enter 1 to log data and 2 to retrieve : "))
if n==1:
    logdata()
elif n==2:
    retrievedata()
else:
    print('invalid input')
   
    
