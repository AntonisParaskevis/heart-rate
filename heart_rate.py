while True:
    # Prompt the user to enter a person's age
    age = input("Enter a person's age\n")
    
    # Check whether the user's input is valid (in this case, a positive integer). If the user has entered a letter, a punctation mark, a symbol, a non-integer number, zero, or a negative number, prompt the user to enter a valid input
    if not age.isdigit() or int(age) <= 0:
        print("Invalid entry, please enter an integer greater than zero.")
        continue
    else:
        # Convert the user's input to an integer, as the input itself is a string by default
        age = int(age)
        break

# Same for the resting heart rate
while True:
    heart_rate = input("Enter the resting heart rate\n")
    
    if not heart_rate.isdigit() or int(heart_rate) <= 0:
        print("Invalid entry, please enter an integer greater than zero.")
        continue
    else:
        heart_rate = int(heart_rate)
        break

# Calculate and display the exercise heart rate
print("Exercise heart rate: " + str(0.7 * (220-age) + 0.3 * heart_rate) + " bpm.")

# In the end, prompt the user to press Enter, in order to exit the program
input("Press Enter to exit the program")