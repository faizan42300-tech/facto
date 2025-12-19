def fact(n):                                                #3  -flow of data-
   if (n==1 or n==0):                                       #4          #6
    return 1                                                #4 if true  #6
   return n*fact(n-1)                                       #5         #7     so on.....
n=int(input("enter a number:"))                             #1         
print(f"The factorial of {n} is:{fact(n)}")                 #2    
