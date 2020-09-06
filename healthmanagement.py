def date():
    import time
    second=time.time()
    local_time = time.ctime(second)
    return(local_time)	

def management():
    while(1):
        c=int(input("enter 1 for ram 2 for ratan 3 roy enter 4 for exit\n"))
        if(c==1):
            f=open("record1.txt",'r+')
            b=int(input("if you want to do exercise press 1 \n if want to enter your diet details press 2 \n if you want to get the details of past actions print 3\n"))
            if(b==1):
                exercise=input("enter the exercise\n")
                d=date()
                f.write(exercise+" at "+d+"\n")
            if(b==2):
                food=input("enter the food\n")
                d=date()
                f.write(food+" at "+d+"\n")
            f.close()
            if(b==3):
                f=open("record1.txt",'r')
                content=f.read()
                print(content)
    
        if(c==2):
            f=open("record2.txt",'a')
            b=int(input("if you want to do exercise press 1 \n if want to enter your diet details press 2 \n if you want to get the details of past actions print 3\n"))
            if(b==1):
                exercise=input("enter the exercise\n")
                d=date()
                f.write(exercise+" at "+d+"\n")
            if(b==2):
                food=input("enter the food\n")
                d=date()
                f.write(food+" at "+d+"\n")
            f.close()
            if(b==3):
                f=open("record2.txt",'r')
                content=f.read()
                print(content)
        if(c==3):
            f=open("record3.txt",'a')
            b=int(input("if you want to do exercise press 1 \n if want to enter your diet details press 2 \n if you want to get the details of past actions print 3\n"))
            if(b==1):
                exercise=input("enter the exercise\n")
                d=date()
                f.write(exercise+" at "+d+"\n")
            if(b==2):
                food=input("enter the food\n")
                d=date()
                f.write(food+" at "+d+"\n")
            f.close()
            if(b==3):
                f=open("record3.txt",'r')
                content=f.read()
                print(content)

        if(c==4):
            break
  
        
        

management()