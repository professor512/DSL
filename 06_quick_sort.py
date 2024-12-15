# Write a Python program to store first year percentage of students in array. Write
# function forsorting array of floating point numbers in ascending order using quick
# sort and display top five scores.


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def print_top5(arr):
    arr.reverse()
    if len(arr) < 5:
        for i in range(0, len(arr)):
            print(arr[i])
    else:
        for i in range(0, 5):
            print(arr[i])


percentages = []
n = int(input("\nEnter Number of students in first year: "))
for i in range(n):
    percentage = float(input(f"\nEnter Percentage of student {i+1}: "))
    percentages.append(percentage)

print("\nPercentages in ascending order using Quick Sort: ")
sorted_percentages = quick_sort(percentages)
print(sorted_percentages)
print("\nTop 5 Scores are: ")
print_top5(sorted_percentages)
