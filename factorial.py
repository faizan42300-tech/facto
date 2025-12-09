def fact(n):                                                #flow of data
   if (n==1 or n==0):                                       #3          #5
    return 1                                                #3 if true  #5
   return n*fact(n-1)  #factorial formula = n*fact(n-1)     #4          #6     so on.....
n=int(input("enter a number:"))                             #1          
print(f"The factorial of {n} is:{fact(n)}")                 #2    