def fibonacci_search(phonebook, name):
    j = 0
    k = 1
    l = j + k
    while l < len(phonebook):
        j = k
        k = l
        l = j + k

    offset = -1

    while l > 1:
        i = min(offset + j, len(phonebook) - 1)

        if phonebook[i][0] < name:
            l, k, j = k, j, k - j
            offset = i
        elif phonebook[i][0] > name:
            l, k, j = j, k - j, j - k
        else:
            return phonebook[i]

    if (k and offset + 1 < len(phonebook) and phonebook[offset + 1][0] == name):
        return phonebook[offset + 1]

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
        print("1. Search for a friend (Fibonacci search)")
        print("2. Insert a friend")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter the name to search: ")
            result = fibonacci_search(phonebook, name)
            if result:
                print(f"Name: {result[0]}, Number: {result[1]}")
            else:
                print(f"{name} not found in the phonebook.")

        elif choice == 2:
            name = input("Enter the name to insert: ")
            number = input("Enter the number: ")
            insert_friend(phonebook, name, number)

        elif choice == 3:
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
