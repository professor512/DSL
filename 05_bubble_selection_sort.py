# Write a Python program to store first year percentage of students in array. Write 
# function forsorting array of floating point numbers in ascending order using
# a) Selection Sort
# b) Bubble sort and display top five scores.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i;
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                arr[j], arr[min_index] = arr[min_index], arr[j]
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def top_5_score(percentages):
    top5 = bubble_sort(percentages)
    top5.reverse()
    if len(percentages) < 5:
        for i in range(0,len(percentages)):
            print(top5[i])
    else:
        for i in range(0,5):
            print(top5[i])
    
    
percentages = []
n = int(input("\nEnter number of students in first year: "))
for i in range(n):
    percentage = float(input(f"Enter percentage of student no {i+1}: "))
    percentages.append(percentage)
    
    
while True:
    print("\nSelect an Option")
    print("\n1 - Selection sort")
    print("\n2 - Bubble sort")
    print("\n3 - Display top 5 score")
    print("\n4 - EXIT")
    choice = int(input("\nEnter your choice: "))
    
    if choice == 1:
        selection_sorted = selection_sort(percentages)
        print("\n\nSorted list using Selection sort: ", selection_sorted)
      
    elif choice == 2:
        bubble_sorted = bubble_sort(percentages)
        print("\n\nSorted list using Bubble sort:", bubble_sorted)
        
    elif choice == 3:
        top_5_score(percentages)
    
    elif choice == 4:
        break
    
    else:
        print("\nInvalid Choice")
    
