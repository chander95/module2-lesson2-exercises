#Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))
num3 = int(input("Please enter a final number: "))

def largest_number():
    if num1 >= num2 and num1 >= num3:
        print("The largest number is " + str(num1))
    elif num2 >= num1 and num2 >= num3:
        print("The largest number is " + str(num2))
    elif num3 >= num1 and num3 >= num2:
        print("The largest number is " + str(num3))
        

largest_number()



#Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.
#Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. The largest number is 4. "

def smallest_number():
    if num1 <= num2 and num1 <= num3:
        print("The smallest number is " + str(num1))
    elif num2 <= num1 and num2 <= num3:
        print("The smallest number is " + str(num2))
    elif num3 <= num1 and num3 <= num2:
        print("The smallest number is " + str(num3))


smallest_number()