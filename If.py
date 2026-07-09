#age = 31

#if age > 18:
#    print("You are an adult.")
#elif age == 18:
#    print("You are exactly 18 years old.")  
#else:
#    print("You are a minor.")


#name = input("Enter your name: ")
##name_len = len(name)

#if name_len < 3:
#    print("Name must be at least 3 characters long.")
#elif name_len > 50:
#    print("Name can be a maximum of 50 characters long.")
#else:
#    print("Name looks good!")



# Weight = int(input("Enter your weight "))
# calculate_weight = input("(L)bs or (K)g: ")

# if calculate_weight.upper() == "L":
#     converted_weight = Weight * 0.45
#     print(f"You are {converted_weight} kg.")
# elif calculate_weight.upper() == "K":
#     converted_weight = Weight / 0.45
#     print(f"You are {converted_weight} pounds.")
# else:
#     print("Invalid input. Please enter 'L' for pounds or 'K' for kilograms.")

# #####ODD or EVEN #####
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("The number is even.")
# else:
    # print("The number is odd.")


# ###POSITIVE, NEGATIVE or ZERO
# number  =int(input("Enter a number: "))
# if number > 0:
#     print("Number is positive")
# elif number < 0:
#     print ("Number is Negative")    
# else :
#     print ("Number is Zero")

#####GRade Calculator###

# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print('Grade A')
# elif marks >= 80:
#     print('Grade B')
# elif marks >= 70:
#     print('Grade C')
# else:
#     print('Grade D')


# ###Largest of 3 Numbers###
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# c = int(input("Enter 3rd number: "))
# if a >=b and b>=c:
#     print(f"{a} is the largest number.")
# elif b >= a and b >= c:
#     print(f"{b} is the largest number.")
# else:
#     print(f"{c} is the largest number.")

# ####Simple Calculator####
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number:"))
# operator = input(" Enter a operation: +, -, *, /, //, %: ")
# if operator == "+":
#     print (f" addition: {num1 + num2}")
# elif operator == "-":
#     print (f" subtraction: {num1 - num2}")
# elif operator == "*":
#     print (f" multiplication: {num1 * num2}")
# elif operator == "/":
#     print (f" division: {num1 / num2}")
# elif operator == "//":
#     print (f" floor division: {num1 // num2}")
# elif operator == "%":
#     print (f" modulus: {num1 % num2}")
# else:   
#     print("Invalid operator. Please enter a valid operator (+, -, *, /, //, %).")   


# ####temperature Checker####
# temperature = int(input("Enter the temperature in Celsius: "))
# if temperature > 30:
#     print("It's Hot!")
# elif temperature >=15 and temperature <=30:
#     print("It's Warm.")
# elif temperature < 15:
#     print("It's Cold.")
# else:
#     print("Invalid temperature input.")

####Number Divisibility Checker####
# number = int(input("Enter a number: "))
# if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
# elif number % 5 == 0:
#     print("Buzz")
# elif number % 3 == 0:
#     print("Fizz")
# else:
#     print("Not divisible by 3 or 5")

#####VOTE ELIGIBILITY CHECKER#####
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote yet.")


###Weekday Checker###
# number = int(input("Enter a number (1-7): "))
# if number ==1:
#     print("Monday")
# elif number ==2:
#     print("Tuesday")
# elif number ==3:
#     print("Wednesday")  
# elif number ==4:
#     print("Thursday")  
# elif number ==5:
#     print("Friday")
# elif number ==6:
#     print("Saturday")  
# elif number ==7:
#     print("Sunday")
# else:
#     print("Invalid input")



###Marks to grade###
# marks = int(input("Enter your marks (0-100): "))
# if marks >= 90 and marks <= 100:
#     print("Excellent")
# elif marks >= 75 and marks < 90:
#     print("Very Good")
# elif marks >= 50 and marks < 75:
#     print("Good")
# elif marks >= 35 and marks < 50:
#     print("Pass")
# elif marks < 35:
#     print("Fail")
# else:
#     print("Invalid input")



####LEAP YEAR CHECKER####   
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 !=0 or year % 400 ==0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")