numbers = [10, 5, 20, 10, 5, 30, 8, 20, 5]

#function
def remove_duplicate(data_list):
    unique_set = set(data_list)
    unique_list = list(unique_set)
    return unique_list

#main program
uniuqe = remove_duplicate(numbers)

print("\n--- List Analysis ---")
print(f"List: {numbers}")
print(f"Unique List: {uniuqe}")
