def binary_search_recursive(phonebook, name, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    if phonebook[mid][0] == name:
        return phonebook[mid]
    elif phonebook[mid][0] < name:
        return binary_search_recursive(phonebook, name, mid + 1, right)
    else:
        return binary_search_recursive(phonebook, name, left, mid - 1)


def binary_search_nonrecursive(phonebook, name):
    left, right = 0, len(phonebook) - 1
    while left <= right:
        mid = (left + right) // 2
        if phonebook[mid][0] == name:
            return phonebook[mid]
        elif phonebook[mid][0] < name:
            left = mid + 1
        else:
            right = mid - 1
    return None


def insert_friend(phonebook, name, number):
    for i, entry in enumerate(phonebook):
        if entry[0] == name:
            print(f"{name} is already in the phonebook.")
            return
        elif entry[0] > name:
            phonebook.insert(i, (name, number))
            print(f"{name} has been added to the phonebook.")
            return
    phonebook.append((name, number))
    print(f"{name} has been added to the phonebook.")


def main():
    phonebook = []
    while True:
        print("Made by Karan Salunkhe, 73, SE-A AI&DS")
        print("Phonebook Options:")
        print("1. Search for a friend (binary search - recursive)")
        print("2. Search for a friend (binary search - non-recursive)")
        print("3. Insert a friend")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter the name to search: ")
            result = binary_search_recursive(phonebook, name, 0, len(phonebook) - 1)
            if result:
                print(f"Name: {result[0]}, Number: {result[1]}")
            else:
                print(f"{name} not found in the phonebook.")

        elif choice == 2:
            name = input("Enter the name to search: ")
            result = binary_search_nonrecursive(phonebook, name)
            if result:
                print(f"Name: {result[0]}, Number: {result[1]}")
            else:
                print(f"{name} not found in the phonebook.")

        elif choice == 3:
            name = input("Enter the name to insert: ")
            number = input("Enter the number: ")
            insert_friend(phonebook, name, number)

        elif choice == 4:
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
