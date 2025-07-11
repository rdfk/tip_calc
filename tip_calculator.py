import math  # Importing the math module so we can use math.ceil() to round the total up to the nearest dollar

# Prompt the user to enter the bill amount
bill_input = input("Enter Bill Amount: $")

# Check if the user didn't type anything
if bill_input == "":
    print("Please enter an amount")  # Friendly reminder if they left it blank
else:
    bill = float(bill_input)  # Convert the input string into a floating point number so we can do math

    # Display tip options
    print("\nHow much would you like to tip?")
    print("1. 5%", "2. for 10%", "3. for 15%")

    # Start an input validation loop for tip choice
    while True:
        try:
            # Ask the user to choose a tip percentage
            choice = int(input("Enter your choice (1-3): "))

            # If they chose a number not in the list, prompt again
            if choice not in [1, 2, 3]:
                print("Invalid input. Please enter choice (1-3)")

            else:
                # Calculate the tip based on their choice
                if choice == 1:
                    tip = bill * 0.05
                elif choice == 2:
                    tip = bill * 0.10
                elif choice == 3:
                    tip = bill * 0.15

                # Add the tip to the bill
                total = bill + tip

                # Round the total up to the nearest whole dollar
                rounded_total = math.ceil(total)

                # Print the final amount, formatted to two decimal places
                print(f"Total: ${rounded_total:.2f}")

                # Exit the loop now that we have valid input and results
                break

        # Catch anything that isn't a number (like "abc", etc.)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
