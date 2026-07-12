#i = 5
#while i > 0:
#    print('*' * i)
#    i -= 1
#print("Happy New Year!")


# ###Number guessing game
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")
#         break
# else:
#     print("Sorry, you failed!")


# i=0

# while i <=5:
#     print(i * '*')
#     i += 1


#####sum of natural numbers###

# num = int(input("Enter a number: "))
# i =1    
# total = 0
# while i <= num:
#     total += i
#     i += 1
# print (f"The sum of natural numbers up to {num} is: {total}")

# ####print 1-10 numbers###
# i = 1
# while i <=10:
#     print(i)
#     i += 1


####sum of natural numbers####
# num = int(input("Enter a number:  "))
# i = 1
# total = 0
# while i <=num:
#     total += i
#     i = i + 1
# print(total)

# ###multiplication table####
# table = int(input("Enter a number: "))
# i=1
# while i <=10:
#     print(table,  'x', i, '=', table * i)
#     i +=1


###reverse countdown####
# n = int(input("Enter a number: "))
# while n > 0:
#     print(n)
#     n -= 1


###Guess the number#####
# secret = 6
# guess = int(input("Guess the number (1-10): "))
# while guess != secret:
#     print("Wrong! Try again.")
#     guess = int(input("Guess the number (1-10): "))

# print("Correct! You guessed it.")

# num = int(input("Enter a numer: "))
# i=1
# sum=0
# while i <= num:
#     sum += i
#     i +=1
# print(f"total = {sum}")


# guess = 7
# num = int(input("Enter a number: "))
# count = 0
# while num != guess:
#     print("Wrong Guess, Try Again")
#     count = count + 1
#     if count < 3:
#         num = int(input("Enter a number: "))
#     else:
#         break  
# else:
#     print("You guessed it right")
    
num = int(input("Enter a number: "))
i = 1
factorial = 1

while i <= num:
    factorial *= i
    i += 1

print("Factorial =", factorial)
