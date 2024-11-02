def display_main_menu():
    print("“display_main_menu")

def get_user_input():
    user_input = input("Enter a sequence of numbers separated by commas (e.g., 5,67,32): ")
    string_list = user_input.split(",")
    float_list = [float(num) for num in string_list]  
    return float_list

def calc_average(temperatures):
    total = sum(temperatures)
    calc_average = total / len(temperatures)
    return calc_average

def find_min_max(temperatures):
    min_temp = min(temperatures)  # Find minimum temperature
    max_temp = max(temperatures)  # Find maximum temperature
    return [int(min_temp), int(max_temp)]  # Return as a list of integers

def sort_temperature(temperatures):
    print("sort_temperature")
    # This will return the sorted list of temperatures later
    return []

def calc_median_temperature(temperatures):
    print("calc_median_temperature")
    # This will return the median temperature later
    return 0.0

display_main_menu()
temperatures = get_user_input() #Get's the User Inputs
average = calc_average(temperatures)
print("The Average is "+ str(average))