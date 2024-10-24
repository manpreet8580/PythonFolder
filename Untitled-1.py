# def test_range(n):
#       if n in range(1,50):
#             print(" The number is present",str(n))
#       else:
#        print("The number is not present.")
# test_range(27)  



# def my_function(n):

#       if n<0:
#             print("Factorial does not exist for negative numbers.")
#       elif n==0:
#             print("The Factorial of O is 1.")
#       else:
#             for i in range(1,n+1):
#                   factorial = factorial*i  
#                   print("The factorial of",n,"is",factorial)    
# my_function(5)  

def factorial(n):
      if n == 0:
            return 1
      else:
            return n * factorial(n-1)     
print(factorial(6)) 
     

first=int(input("enter the first number:"))
operator = input("enter the operator(+,-,%,*,/):")
second=int(input("enter the second number:"))                
 
if operator =='+':
      print(first+second)
elif operator =='-':
      print(first-second)
elif operator =='%':
      print(first%second)
elif operator =='*':
      print(first*second)            
elif operator =='/':
      print(first/second)   
else:
     print("Invalid Operation") 