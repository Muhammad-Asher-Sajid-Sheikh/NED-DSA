# LAB SESSION 01 - Array Implementation and Traversal in Python
# (Without using built-in functions like sum, max, min)

# 1. Input values from the user instead of hardcoded values
def input_array(size):
    arr = []
    print(f"Enter {size} numbers:")
    for i in range(size):
        num = int(input(f"Element {i}: "))
        arr.append(num)
    return arr

# 2. Function to calculate sum and average (without sum())
def sum_and_average(arr):
    total = 0
    count = 0
    for num in arr:
        total += num
        count += 1
    avg = total / count if count != 0 else 0
    return total, avg

# 3. Find maximum and minimum value (without max() and min())
def find_max_min(arr):
    maximum = arr[0]
    minimum = arr[0]
    for num in arr[1:]:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum, minimum

# 4. Display array in reverse order (without reverse slicing)
def reverse_array(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# 5. Find the second largest element (manual logic)
def second_largest(arr):
    # First find largest
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num

    # Now find second largest
    second = None
    for num in arr:
        if num != largest:
            if second is None or num > second:
                second = num
    return second

# 6. Frequency of each unique element (manual dictionary counting is allowed)
def frequency_count(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    size = 5
    arr = input_array(size)  # user inputs values
    
    print("\nArray elements with index:")
    for i in range(len(arr)):
        print(f"Element at index {i} = {arr[i]}")

    # Sum and Average
    total, avg = sum_and_average(arr)
    print(f"\nSum = {total}, Average = {avg}")

    # Maximum and Minimum
    mx, mn = find_max_min(arr)
    print(f"Maximum = {mx}, Minimum = {mn}")

    # Reverse Order
    print("Array in reverse order:", reverse_array(arr))

    # Second Largest
    second = second_largest(arr)
    if second:
        print("Second largest element =", second)
    else:
        print("No second largest element (all values same)")

    # Frequency of elements
    print("Frequency of elements:")
    freq = frequency_count(arr)
    for key, val in freq.items():
        print(f"{key} -> {val} times")
