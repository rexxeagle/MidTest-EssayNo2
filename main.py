'''
Name  : Rendy Elang Lesmana
NIM   : 20230040044
Class : TI23I

Essay Number 2 of Mid Exam of Basic Programming Subject
Calculator Program
'''
print("====Welcome to Calculator Program====")
print("=========Programmed by Rendy=========")
def menu():
    print()
    print("Menu :")
    print("1. Calculate Current Age")
    print("2. Calculate the Remaining Installment Years")
    print("3. Calculate BMI body Weight")
    print("4. Exit")
    print()
    choice = int(input("Choose a menu : "))
    print()
    if choice == 1:
        print("You chosed Calculate Current Age menu")
        user_birth_year = int(input("Enter your birth year : "))
        user_current_year = int(input("Enter the current year : "))
        result = calculate_current_age(user_birth_year, user_current_year)
        print(f"Your current age is {result} years old")
        is_repeat_program()
    elif choice == 2:
        print("You chosed Calculate the Remaining Installment Years menu")
        input_total_installment_years = int(input("Enter the total installment years : "))
        input_installment_years_paid = int(input("Enter the installment years paid : "))
        result = calculate_remaining_installment_years(input_total_installment_years, input_installment_years_paid)
        if input_installment_years_paid > input_total_installment_years:
            print(f"Your installment years has overpaid with remaining {result} years")
        else:
            print(f"The remaining installment years are {result} years")
        is_repeat_program()
    elif choice == 3:
        print("You chosed Calculate BMI body Weight menu")
        user_weight = float(input("Enter your weight (kg) : "))
        user_height_cm = float(input("Enter your height (cm) : "))
        result = round(calculate_bmi(user_weight, user_height_cm), 1)
        print(f"Your BMI is {result}")
        is_repeat_program()
    elif choice == 4:
        print("Thank you for using this program")
        exit()
    else:
        print("Invalid input, please type the correct number!")
        is_repeat_program()

# Function for is_repeat_program
def is_repeat_program():
    print()
    decision = input("Do you want to repeat the program? (yes/no) : ")
    if decision == "yes":
        menu()
    else:
        print("Thank you for using this program")
        exit()

# Function for Calculate Current Age
def calculate_current_age(birth_year, current_year):
    result = current_year - birth_year
    return result

# Function for Calculate the Remaining Installment Years
def calculate_remaining_installment_years(total_installment_years, installment_years_paid):
    result = total_installment_years - installment_years_paid
    return result

# Function for Calculate BMI
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    result = weight / (height_m ** 2)
    return result

menu()