numbers = [15, 8, 42, 4, 99, 16]

#function
def find_min_max(data_list):
    if not data_list:
        return "List is empty", "List is empty"

    current_min = data_list[0]
    current_max = data_list[0]

    for number in data_list:
        if number > current_max:
            current_max = number
        if number < current_min:
            current_min = number

    return current_min, current_max

#main program
minimum, maximum = find_min_max(numbers)

print("\n--- List Analysis ---")
print(f"List: {numbers}")
print(f"Minimum Value: {minimum}")
print(f"Maximum Value: {maximum}")