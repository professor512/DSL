def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

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

    sorted_percentages_selection = percentages.copy()
    selection_sort(sorted_percentages_selection)
    print("Sorted array using Selection Sort:")
    display_top_scores(sorted_percentages_selection, 5)

    sorted_percentages_bubble = percentages.copy()
    bubble_sort(sorted_percentages_bubble)
    print("\nSorted array using Bubble Sort:")
    display_top_scores(sorted_percentages_bubble, 5)

if __name__ == "__main__":
    main()
