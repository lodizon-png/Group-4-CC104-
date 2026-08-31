# List operations program
def create_list():
    nums = []
    n = int(input("How many integers do you want to enter? "))

    if n <= 0:
        print("Number of items must be greater than 0.")
        return nums

    print(f"Enter {n} integers:")
    for i in range(n):
        value = int(input(f"Value {i + 1}: "))
        nums.append(value)

    return nums


def display_list(nums):
    if not nums:
        print("The list is empty.")
        return

    print("List elements:")
    for i, value in enumerate(nums):
        print(f"[{i}] = {value}")


def find_largest(nums):
    if not nums:
        print("The list is empty.")
        return None

    largest = nums[0]
    for value in nums[1:]:
        if value > largest:
            largest = value
    return largest


def find_smallest(nums):
    if not nums:
        print("The list is empty.")
        return None

    smallest = nums[0]
    for value in nums[1:]:
        if value < smallest:
            smallest = value
    return smallest


def calculate_average(nums):
    if not nums:
        print("The list is empty.")
        return None

    total = sum(nums)
    avg = total / len(nums)
    return avg


def update_element(nums):
    if not nums:
        print("The list is empty.")
        return

    index = int(input(f"Enter the index to update (0 to {len(nums) - 1}): "))
    if index < 0 or index >= len(nums):
        print("Invalid index.")
        return

    new_value = int(input("Enter the new value: "))
    nums[index] = new_value
    print(f"Element at index {index} updated to {new_value}.")


def insert_element(nums):
    value = int(input("Enter the value to insert: "))
    position = int(input("Enter the position to insert at (0 to end): "))

    if position < 0 or position > len(nums):
        print("Invalid position.")
        return

    nums.insert(position, value)
    print(f"{value} inserted at index {position}.")


def delete_element(nums):
    if not nums:
        print("The list is empty.")
        return

    index = int(input(f"Enter the index to delete (0 to {len(nums) - 1}): "))
    if index < 0 or index >= len(nums):
        print("Invalid index.")
        return

    deleted = nums.pop(index)
    print(f"Deleted element {deleted} from index {index}.")


def linear_search(nums):
    if not nums:
        print("The list is empty.")
        return

    target = int(input("Enter the value to search: "))
    for i, value in enumerate(nums):
        if value == target:
            print(f"Found {target} at index {i}.")
            return

    print(f"{target} was not found in the list.")


def sort_list(nums):
    if not nums:
        print("The list is empty.")
        return

    nums.sort()
    print("List has been sorted in ascending order.")


def binary_search(nums):
    if not nums:
        print("The list is empty.")
        return

    target = int(input("Enter the value to search: "))
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            print(f"Found {target} at index {mid}.")
            return
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    print(f"{target} was not found in the list.")


def show_menu():
    print("\nLIST OPERATIONS MENU")
    print("1. Create a list")
    print("2. Display all elements")
    print("3. Find largest value")
    print("4. Find smallest value")
    print("5. Calculate average")
    print("6. Update an element")
    print("7. Insert a new element")
    print("8. Delete an element")
    print("9. Linear search")
    print("10. Sort the list")
    print("11. Binary search")
    print("12. Exit")


# Main program
nums = []

while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        nums = create_list()
    elif choice == 2:
        display_list(nums)
    elif choice == 3:
        largest = find_largest(nums)
        if largest is not None:
            print(f"Largest value: {largest}")
    elif choice == 4:
        smallest = find_smallest(nums)
        if smallest is not None:
            print(f"Smallest value: {smallest}")
    elif choice == 5:
        avg = calculate_average(nums)
        if avg is not None:
            print(f"Average value: {avg}")
    elif choice == 6:
        update_element(nums)
    elif choice == 7:
        insert_element(nums)
    elif choice == 8:
        delete_element(nums)
    elif choice == 9:
        linear_search(nums)
    elif choice == 10:
        sort_list(nums)
    elif choice == 11:
        binary_search(nums)
    elif choice == 12:
        print("Program ended. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")