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



Weight = int(input("Enter your weight "))
calculate_weight = input("(L)bs or (K)g: ")

if calculate_weight.upper() == "L":
    converted_weight = Weight * 0.45
    print(f"You are {converted_weight} kg.")
elif calculate_weight.upper() == "K":
    converted_weight = Weight / 0.45
    print(f"You are {converted_weight} pounds.")
else:
    print("Invalid input. Please enter 'L' for pounds or 'K' for kilograms.")
