def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def display_top_scores(arr, top_n):
    if top_n > len(arr):
        top_n = len(arr)
    print(f"Top {top_n} Scores:")
    for i in range(top_n):
        print(f"{i+1}. {arr[i]}%")

def main():
    n = int(input("Enter the number of students: "))
    percentages = []
    for i in range(n):
        percentage = float(input(f"Enter the percentage for student {i + 1}: "))
        percentages.append(percentage)

    sorted_percentages = quick_sort(percentages)
    print("Sorted array using Quick Sort:")
    display_top_scores(sorted_percentages, 5)

if __name__ == "__main__":
    main()
