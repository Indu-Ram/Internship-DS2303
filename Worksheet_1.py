#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q11.Write a python program to find the factorial of a number?


# In[ ]:


Ans)Factorial:Factorial of a number is denoted by n! is the product of all positive integers less than or equal to n:
n! = n*(n-1)*(n-2)*…..3*2*1


# In[3]:


import math


# In[8]:


print("Enter a Number: ", end="")
try:
    num = int(input())
    fact = 1
    for i in range(1, num+1):
        fact = fact*i
    print("\nFactorial of", num, "=", fact)
except ValueError:
    print("\nInvalid Input!")


# In[ ]:


#Q12.Write a python program to find whether a number is prime or composite.


# In[ ]:


Ans)Prime Number:Any natural number that is divisible by 1 and itself called Prime Number. 
Prime Number is not divisible by any other numbers by except one and itself.

Composite Number:Any positive integer that can be formed by multiplying two smaller 
positive integers is called composite number. In other word, composite number is a positive integer that has at least one
divisor other than 1 and itself.

    
    


# In[14]:


#Input a number and check if the number is prime or composite number
n= int(input("Enter any number:"))
if(n ==0 or n == 1):
    printf(n,"Number is neither prime nor composite")
elif n>1 :
    for i in range(2,n):
        if(n%i == 0):
            print(n,"is not prime but composite number")
            break
    else:
        print(n,"number is prime but not composite number")
else :
    print("Please enter positive number only ")


# In[ ]:


#13.	Write a python program to check whether a given string is palindrome or not.


# In[ ]:


Ans)A palindrome is a string that is the same read forward or backward.


# In[15]:


# function to check string is
# palindrome or not
def isPalindrome(str):
  
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
  
# main function
s = "malayalam"
ans = isPalindrome(s)
  
if (ans):
    print("Yes")
else:
    print("No")


# In[ ]:


#14.Write a Python program to get the third side of right-angled triangle from two given sides.


# In[ ]:


Ans)The Pythagorean theorem states that given a right triangle, the hypotenuse squared equals the sum of the sides squared.


# In[ ]:


import math
a = float(input("Give side a: "))
b = float(input("Give side b: "))
c = math.sqrt(a ** 2 + b ** 2)
print(f"The length of the hypotenuse c is {c}")


# In[ ]:


#15.	Write a python program to print the frequency of each of the characters present in a given string.


# In[ ]:


str1 = input ("String ")
d = dict()
for c in str1:
    if c in d:
        d[c] = d[c] + 1
    else:
        d[c] = 1
print(d)


# In[ ]:




