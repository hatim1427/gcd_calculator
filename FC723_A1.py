
#this class purpose is to find the greatest common diviser of 2 intigers 
#using the Euclidean Algorith
class GCD:
#initialising the function and calling it find GCD
    
   def find_GCD (self ,a, b):
       #storing the value to variables 
        self.a = a
        self.b = b
        #start looping until b becomes 0
        #when b becomes 0 a have the GCD
        while b != 0:
           # caucilate the remainder wich is a divided by b
            rem = a % b
           #switch the value of a to b (the swaping part)
            a = b
           #replaceing b with the remainder
            b = rem
        #at this part a has the GCD 
        return a
    
#take input from the user for the first number
num1 = input('Enter you first number')
#take input from the user for the second
num2 = input('Enter your second number')
#checking if both inputs are digits 
if num1.isdigit() and num2.isdigit():
    #conversting strings into integers
    num1 = int(num1)
    num2 = int(num2)
    #check if both numbers are positive
    if num1 > 0 and num2 > 0:
        #create an object of the GCD 
        x = GCD()
        #call the function to find the GCD for the tow numbers
        result = x.find_GCD(num1 , num2)
        print(result)
    else:
        #print an error if any number is zero or negitive
        print('the number must be positive')
else:
    #print an error message if the input has non digital characters
    print('the number is invalid')
    
    
    

    


