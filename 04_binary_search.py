# a) Write a Python program to store names and mobile numbers of your 
# friends in sorted order on names. Search your friend from list using binary search 
# (recursive and non- recursive). Insert friend if not present in phonebook

def binary_search_recursive(phonebook, name, left, right):
    if left > right:
        return None
    mid = (left + right) // 2 
    if phonebook[mid][0] == name:
        return phonebook[mid]
    elif phonebook[mid][0] < name:
        return binary_search_recursive(phonebook, name, mid+1, right)
    else:
        return binary_search_recursive(phonebook, name, left, mid-1)



def binary_search_nonrecursive(phonebook, name, left, right):
    while left <= right:
        mid = (left+right) // 2
        if phonebook[mid][0] == name:
            return phonebook[mid];
        elif phonebook[mid][0] < name:
            left = mid+1
        else:
            right = mid-1


def insert_friend(phonebook, name, number):
    for i, entry in enumerate(phonebook):
        if entry[0] == name:
            print(f"{name} is already in the phonebook.")
            return
        if entry[0] > name:
            phonebook.insert(i, (name, number))
            break
    else:
        phonebook.append((name, number))
    print(f"{name} has been added to the phonebook.")
    

phonebook =[]

while True:
    print("\nSelect an Option: ")
    print("\n1 - Insert a friend")
    print("\n2 - Binary Search Recursive")
    print("\n3 - Binary Search non-recursive")
    print("\n4 - Exit\n\n")
    
    choice = int(input(" Enter your choice: "))
    
    if choice == 1:
        name = input("Enter the name to insert: ")
        number = input("Enter the number: ")
        insert_friend(phonebook, name, number)
        
    elif choice == 2:
        name = input("Enter Name to search: ")
        result = binary_search_recursive(phonebook, name, 0, len(phonebook)-1)
        
        if result:
            print(f"\nName: {result[0]}\nNumber: {result[1]}")
        else:
            print("\nElement not found")
            
    elif choice == 3:
        name = input("\nEnter Name to search")
        result = binary_search_nonrecursive(phonebook, name, 0, len(phonebook)-1)
        
        if result:
            print(f"\nName: {result[0]}\nNumber: {result[1]}")
        else:
            print("\nElement not found")
        
    elif choice == 4:
        break
        
