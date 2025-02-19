
def float_input(prompt):
# Function that will prompt user to input an integer value for the function after it, func_select. Also contains correction method for undesirable non-integer input.
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Please enter a valid integer.")

func_select = int(input("Enter an integer value from 1 - 5 to select the function to be used by the solver: "))
# Function that, based on integer input value, will select from externally defined functions 1, 2, 3, 4, or 5 to be used by the solver.
try:
    if func_select == 1:
        main_function = newton_function_1
        prime_function = newton_function_1_prime
        
    elif func_select == 2:
        main_function = newton_function_2
        prime_function = newton_function_2_prime
            
    elif func_select == 3:
        main_function = newton_function_3
        prime_function = newton_function_3_prime
            
    elif func_select == 4:
        main_function = newton_function_4
        prime_function = newton_function_4_prime
            
    elif func_select == 5:
        main_function = newton_function_5
        prime_function = newton_function_5_prime
        
    else:
        print("Please input a number from 1 to 5.")
            
except ValueError:
    print("Please select a number from 1 to 4.")
    
iter_number = int(input("Enter the number of iterations you would like the solver to undergo: "))
    
x_input = float_input("Enter an intial integer value for x_0: ")


final_result = newton_method(x_input, iter_number)
print(f"Final x_n after {iter_number} iterations is: {final_result}")

