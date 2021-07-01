

n=int(input("Enter the number : "))
r = n
for i in range(1, (n+1)):
    c=n+1 
    r=r+1
    for j in range(r): 
         if(c==(i+j+1)):
             #print("Inside if ",i,j,c)
             print("*",end='')
             c=c+2
         else:
             print(" ",end='')
             #print("Outside if ",i,j,c)
    print() 


r=2*n
c=n+1+2
c1=c
for i in range((n+1), (2*n)):
    r=r-1
    c2=c1
    for j in range(r): 
        if(c2==(i+j+1)):
            #print("* Inside if ",i,j,c2)
            print("*",end='') 
            c2=c2+2
        else:
            print(" ",end='')
            #print("Outside if ",i,j,c2)
    
    c1=c1+2
                                      
    print()
