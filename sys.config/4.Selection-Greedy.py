# --------------------------------------------------------------------
# Problem Statement:
# Implement Greedy Search Algorithm for Selection Sort (Ascending and Descending)
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# Greedy Algorithm: Selection Sort using Greedy Strategy (Ascending Order)
# Greedy Choice: Always pick the minimum element from the unsorted part
# --------------------------------------------------------------------




# Greedy Algorithm: Selection Sort using Greedy Strategy (Ascending Order)

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == "__main__":
    arr = list(map(int, input("Enter elements for Ascending Order sort (space-separated): ").split()))
    print("\nOriginal Array:")
    print(arr)
    sorted_arr = selection_sort(arr.copy())
    print("\nSorted Array (Using Greedy Selection Sort - Ascending Order):")
    print(sorted_arr)





# --------------------------------------------------------------------
# Greedy Algorithm: Selection Sort using Greedy Strategy (Descending Order)

def selection_sort_desc(arr):
    n = len(arr)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr


if __name__ == "__main__":
    arr = list(map(int, input("\nEnter elements for Descending Order sort (space-separated): ").split()))
    print("\nOriginal Array:")
    print(arr)
    sorted_arr = selection_sort_desc(arr.copy())
    print("\nSorted Array (Using Greedy Selection Sort - Descending Order):")
    print(sorted_arr)









# ------------------------------Explainataion------------------------------




def selection_sort(arr):
    """
    Function to perform selection sort in ascending order.
    It follows the Greedy Strategy by selecting the smallest element
    from the unsorted part and placing it at the correct position.
    """
    n = len(arr)  # Step 1: Get total number of elements in the array

    # Step 2: Traverse the array from the first to second last element
    for i in range(n - 1):
        min_index = i  # Step 3: Assume current index i holds the minimum value

        # Step 4: Find the index of the actual minimum element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # If a smaller element is found
                min_index = j  # Update min_index to the new minimum

        # Step 5: Swap the smallest element found with the element at index i
        # This is the greedy step: placing the best choice (minimum) at the right position
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    # Step 6: Return the sorted array
    return arr


# --------------------------------------------------------------------
# Main Function for Ascending Order Sort
# --------------------------------------------------------------------
if __name__ == "__main__":
    # Step A: Take input from the user
    # Input format: space-separated integers (e.g., 10 5 2 8)
    arr = list(map(int, input("Enter elements for Ascending Order sort (space-separated): ").split()))

    # Step B: Display the original array
    print("\nOriginal Array:")
    print(arr)

    # Step C: Sort the array using selection sort (ascending)
    sorted_arr = selection_sort(arr.copy())  # Using .copy() to preserve the original input

    # Step D: Display the sorted array
    print("\nSorted Array (Using Greedy Selection Sort - Ascending Order):")
    print(sorted_arr)


# --------------------------------------------------------------------
# Greedy Algorithm: Selection Sort using Greedy Strategy (Descending Order)
# Greedy Choice: Always pick the maximum element from the unsorted part
# --------------------------------------------------------------------

def selection_sort_desc(arr):
    """
    Function to perform selection sort in descending order.
    It follows the Greedy Strategy by selecting the largest element
    from the unsorted part and placing it at the correct position.
    """
    n = len(arr)  # Step 1: Get total number of elements in the array

    # Step 2: Traverse the array from the first to second last element
    for i in range(n - 1):
        max_index = i  # Step 3: Assume current index i holds the maximum value

        # Step 4: Find the index of the actual maximum element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:  # If a larger element is found
                max_index = j  # Update max_index to the new maximum

        # Step 5: Swap the largest element found with the element at index i
        # This is the greedy step: placing the best choice (maximum) at the right position
        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]

    # Step 6: Return the sorted array
    return arr


# --------------------------------------------------------------------
# Main Function for Descending Order Sort
# --------------------------------------------------------------------
if __name__ == "__main__":
    # Step A: Take input from the user
    # Input format: space-separated integers (e.g., 10 5 2 8)
    arr = list(map(int, input("\nEnter elements for Descending Order sort (space-separated): ").split()))

    # Step B: Display the original array
    print("\nOriginal Array:")
    print(arr)

    # Step C: Sort the array using selection sort (descending)
    sorted_arr = selection_sort_desc(arr.copy())  # Using .copy() to preserve the original input

    # Step D: Display the sorted array
    print("\nSorted Array (Using Greedy Selection Sort - Descending Order):")
    print(sorted_arr)







# Theory:

"""

💡 Greedy Algorithm

🔢 Selection Sort

📈 Time and Space Complexity

♻️ In-place and Stability Concepts

👨‍🏫 How Greedy Strategy Applies to Selection Sort

🧪 Real-world Analogy

📘 THEORY: Selection Sort using Greedy Algorithm
1. ✅ Greedy Algorithm: Concept
A Greedy Algorithm is a method of solving problems by making the locally optimal choice at each step, with the hope that this leads to a globally optimal solution.

🔑 Characteristics:
Makes immediate best (greedy) decisions.

Does not reconsider previous choices.

Works best for problems where a local optimum leads to a global optimum.

2. 🔢 Selection Sort: Concept
Selection Sort is a simple sorting algorithm that divides the input list into two parts:

The sublist of items already sorted

The remaining sublist of items yet to be sorted

The algorithm repeatedly selects the smallest (or largest) element from the unsorted part and places it at the beginning of the unsorted part—this is where the greedy approach is applied.

3. 🧠 How Greedy Algorithm Is Applied in Selection Sort
In each iteration:

Greedy Choice: Pick the smallest (or largest) element in the unsorted portion

Place it in its final position (sorted portion)

This decision is local and immediate, without backtracking

This satisfies the principle of a greedy algorithm.

4. ⏱️ Time Complexity of Selection Sort
Case	Comparisons	Swaps	Time Complexity
Best Case	n(n-1)/2 comparisons	O(n) swaps	O(n²)
Worst Case	n(n-1)/2 comparisons	O(n) swaps	O(n²)
Average	n(n-1)/2 comparisons	O(n) swaps	O(n²)

The number of comparisons does not change based on input order.

So, time complexity is always O(n²).

5. 📦 Space Complexity
O(1) — constant space

It uses only a few extra variables (like min_index, i, j)

So, it is an in-place sorting algorithm

6. 🔁 In-Place vs Stable Algorithm
🧩 In-Place:
Selection sort does not use extra memory — it modifies the array directly.

⚖️ Stable:
Selection sort is NOT stable.

Equal elements may be swapped and lose their original order.

Example:

text
Copy
Edit
Input: [4a, 4b, 3]
Output: [3, 4b, 4a]  ← not stable
7. ⬆️⬇️ Ascending vs Descending Order
Ascending: Greedily pick the minimum element and place it at the front.

Descending: Greedily pick the maximum element and place it at the front.

8. 🌍 Real-life Analogy
Imagine you're selecting the shortest person from a group and asking them to stand first in line.

Then pick the next shortest from the remaining.

You continue doing this until everyone is arranged by height.
This is how selection sort (greedy) works.

🧾 Summary
Concept	Summary
Greedy Algorithm	Makes the best local choice at each step without looking back
Selection Sort	Repeatedly selects smallest/largest and moves it to sorted part
Time Complexity	O(n²) for all cases
Space Complexity	O(1), in-place sorting
Stability	Not stable — may change relative order of equal elements
Ascending Sort	Selects minimum from unsorted
Descending Sort	Selects maximum from unsorted
Greedy Strategy Usage	Greedy choice = picking best candidate (min/max) in each iteration



1. 🔢 Selection Sort
Working Principle:
Selection Sort is a comparison-based sorting algorithm that works by selecting the smallest (or largest) element from the unsorted part of the array and swapping it with the first unsorted element.

Steps:
Traverse the array and find the smallest element.

Swap it with the first unsorted element.

Repeat this process for the remaining unsorted part of the array.

Time Complexity:
Best, Worst, and Average Case: O(n²)

Space Complexity:
O(1) — It is an in-place sorting algorithm.

Advantages:
Simple and easy to understand.

In-place sorting — uses constant space.

Performs well on small arrays.

Disadvantages:
Inefficient for large datasets with O(n²) time complexity.

Not stable — equal elements may not retain their original order.

Performs unnecessary swaps even when the array is already sorted.

Best Use Cases:
Small-sized arrays where the simplicity of implementation matters more than efficiency.

When memory usage is critical (since it uses constant space).

2. 🔄 Bubble Sort
Working Principle:
Bubble Sort works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order. The process is repeated until the list is sorted.

Steps:
Compare each pair of adjacent elements.

Swap them if they are in the wrong order.

After each pass, the largest (or smallest) element "bubbles" to its correct position.

Repeat until the list is sorted.

Time Complexity:
Best Case: O(n) (when the array is already sorted)

Worst and Average Case: O(n²)

Space Complexity:
O(1) — It is an in-place sorting algorithm.

Advantages:
Simple to understand and implement.

Stable — preserves the order of equal elements.

Works well when the input array is already nearly sorted.

Disadvantages:
Inefficient for large datasets (O(n²) in the worst case).

A lot of unnecessary comparisons, even when the array is sorted.

Best Use Cases:
For small arrays or arrays that are already nearly sorted.

Educational purposes for learning basic sorting concepts.

3. 🔀 Insertion Sort
Working Principle:
Insertion Sort builds the sorted portion of the array one element at a time by inserting each new element into its correct position within the sorted part.

Steps:
Start from the second element and compare it with the elements before it.

Shift the elements larger than the current element to the right.

Insert the current element in its correct position.

Time Complexity:
Best Case: O(n) (when the array is already sorted)

Worst and Average Case: O(n²)

Space Complexity:
O(1) — It is an in-place sorting algorithm.

Advantages:
Adaptive — works faster when the array is already partially sorted.

Stable — maintains the relative order of equal elements.

Simple to implement.

Disadvantages:
Inefficient for large arrays with time complexity O(n²).

May require a lot of shifting of elements in the worst case.

Best Use Cases:
For nearly sorted or small arrays.

When you need an adaptive sort that works well for arrays with small inversions.

4. 🔽 Merge Sort
Working Principle:
Merge Sort is a divide-and-conquer algorithm that splits the array into halves, sorts each half recursively, and then merges them back together.

Steps:
Divide the array into two halves.

Recursively sort each half.

Merge the two sorted halves to produce the final sorted array.

Time Complexity:
Best, Worst, and Average Case: O(n log n)

Space Complexity:
O(n) — It is not in-place and requires additional space for merging.

Advantages:
Efficient for large datasets due to O(n log n) time complexity.

Stable — preserves the relative order of equal elements.

Handles large arrays better than quadratic algorithms like Selection or Bubble Sort.

Disadvantages:
Not in-place — requires extra space proportional to the size of the array.

Slower than Quick Sort in practice due to higher constant factors.

Best Use Cases:
For large datasets where the efficiency of O(n log n) matters.

When stability is required.

5. 🚀 Quick Sort
Working Principle:
Quick Sort is a divide-and-conquer algorithm that picks a pivot element, partitions the array around the pivot, and recursively sorts the sub-arrays.

Steps:
Pick a pivot element from the array.

Partition the array into two sub-arrays: one with elements smaller than the pivot and the other with elements greater than the pivot.

Recursively sort the two sub-arrays.

Time Complexity:
Best and Average Case: O(n log n)

Worst Case: O(n²) (occurs when the pivot is poorly chosen)

Space Complexity:
O(log n) — in-place sorting with space required for the recursion stack.

Advantages:
Efficient on average with O(n log n) time complexity.

In-place sorting — doesn’t require extra space like Merge Sort.

Works well on random data.

Disadvantages:
Not stable — may change the relative order of equal elements.

Worst case is O(n²), which happens when the pivot selection is poor (e.g., always picking the first or last element).

Best Use Cases:
For large datasets where average-case O(n log n) time complexity is acceptable.

When you want a fast, in-place sorting algorithm for random data.

📊 Comparison Summary
Algorithm	Time Complexity	Space Complexity	Stable	In-place	Best Use Case
Selection Sort	O(n²)	O(1)	❌ No	✅ Yes	Small arrays
Bubble Sort	O(n²) (worst)	O(1)	✅ Yes	✅ Yes	Nearly sorted arrays
Insertion Sort	O(n²) (worst)	O(1)	✅ Yes	✅ Yes	Nearly sorted arrays
Merge Sort	O(n log n)	O(n)	✅ Yes	❌ No	Large datasets
Quick Sort	O(n log n) (avg)	O(log n)	❌ No	✅ Yes	Large datasets, random data

🎯 Conclusion
Selection Sort is easy to understand and in-place but inefficient for large arrays with its O(n²) time complexity.

Bubble Sort and Insertion Sort are adaptive and work well for nearly sorted data but suffer from inefficiency with larger arrays.

Merge Sort offers stable sorting and works efficiently with large datasets but is not in-place.

Quick Sort is in-place and generally the fastest for random data but can degrade to O(n²) if the pivot selection is poor.




"""