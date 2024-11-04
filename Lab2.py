def display_main_menu():
    print("display_main_menu")

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
    sorted_temps = sorted(temperatures)
    return sorted_temps

def calc_median_temperature(temperatures):
    sorted_temps = sorted(temperatures)  # Sort the temperatures
    n = len(sorted_temps)  # Find the number of elements
    # Calculate the median
    if n % 2 == 1:  # Odd number of elements
        median = sorted_temps[n // 2]
    else:  # Even number of elements
        median = (sorted_temps[n // 2 - 1] + sorted_temps[n // 2]) / 2
    return median

def main():
    display_main_menu()
    temperatures = get_user_input()  # Get user input as a list of floats
    average = calc_average(temperatures)
    print("The Average is " + str(average))
    min_max = find_min_max(temperatures)
    print("The minimum temperature is " + str(min_max[0]) + " and the maximum temperature is " + str(min_max[1]))
    sorted_temps = sort_temperature(temperatures)
    print("The sorted temperatures are:", sorted_temps)
    median = calc_median_temperature(temperatures)
    print("The median temperature is " + str(median))
    
if __name__ == "__main__":
 main()