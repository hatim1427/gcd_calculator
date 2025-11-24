
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
    
    
    
    
    

    


