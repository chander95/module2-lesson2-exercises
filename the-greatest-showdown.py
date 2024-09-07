#Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.

magic_number1 = input("Please enter first number: ")
magic_number2 = input("Please enter second number: ")
magic_number3 = input("Please enter third number: ")

if int(magic_number1) > int(magic_number2) and int(magic_number1) > int(magic_number3):
    print("The largest number is " + str(magic_number1) + "!")
elif int(magic_number2) > int(magic_number1) and int(magic_number2) > int(magic_number3):
    print("The largest number is " + str(magic_number2) + "!")
else:
    print("The largest number is " + str(magic_number3) + "!")



#Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.
#Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. The largest number is 4. "
