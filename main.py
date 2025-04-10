import os
import re

# 1. Write full name to a text file
full_name = "John Michael Doe"
with open("fullname.txt", "w") as file:
    file.write(full_name)

# 2. Read and extract first, middle, last names
with open("fullname.txt", "r") as file:
    name_parts = file.read().strip().split()
    first, middle, last = name_parts[0], name_parts[1], name_parts[2]
    print("First Name:", first)
    print("Middle Name:", middle)
    print("Last Name:", last)

# 3. Print the local file path using os
file_path = os.path.abspath("fullname.txt")
print("Local File Path:", file_path)

# 4. Extract baby names from baby2008.html using regex
with open("C:baby2008.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Regex pattern for male and female names in table rows
pattern = re.compile(r"<tr align=\"right\"><td>\d+</td><td>(\w+)</td><td>(\w+)</td>", re.IGNORECASE)
names = pattern.findall(html_content)

# Flatten and merge male and female names
baby_names = sorted(set([name for pair in names for name in pair]))

# 5. Sort the names using custom sort (Bubble Sort for simplicity)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted_names = bubble_sort(baby_names.copy())
print("First 10 Sorted Baby Names:", sorted_names[:10])

# 6. Binary Search Implementation
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example search
target_name = "Emily"
position = binary_search(sorted_names, target_name)
if position != -1:
    print(f"{target_name} found at index {position}.")
else:
    print(f"{target_name} not found.")
