# This class finds the Greatest Common Divisor (GCD) of two integers
# using the Euclidean Algorithm.
class GCD:

    # Find the GCD of two numbers.
    def find_gcd(self, a, b):

        # Continue until b becomes 0.
        # When b becomes 0, a contains the GCD.
        while b != 0:

            # Calculate the remainder when a is divided by b.
            remainder = a % b

            # Replace a with b.
            a = b

            # Replace b with the remainder.
            b = remainder

        # Return the GCD.
        return a


# Take input from the user for the first number.
num1 = input("Enter your first number: ")

# Take input from the user for the second number.
num2 = input("Enter your second number: ")

# Check if both inputs contain only digits.
if num1.isdigit() and num2.isdigit():

    # Convert the input strings into integers.
    num1 = int(num1)
    num2 = int(num2)

    # Check if both numbers are positive.
    if num1 > 0 and num2 > 0:

        # Create an object of the GCD class.
        gcd_calculator = GCD()

        # Find the GCD of the two numbers.
        result = gcd_calculator.find_gcd(num1, num2)

        # Display the result.
        print("The GCD is:", result)

    else:

        # Display an error if either number is zero or negative.
        print("The numbers must be positive.")

else:

    # Display an error if the input contains non-numeric characters.
    print("Invalid input. Please enter positive integers.")
    
    

    


