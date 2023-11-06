import random
import time

# Deterministic Quicksort
def deterministic_partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False

    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1

        while arr[right] >= pivot and right >= left:
            right = right - 1

        if right < left:
            done = True
        else:
            # Swap arr[left] and arr[right]
            arr[left], arr[right] = arr[right], arr[left]

    # Swap arr[low] and arr[right]
    arr[low], arr[right] = arr[right], arr[low]

    return right

def deterministic_quicksort(arr, low, high):
    if low < high:
        pivot_index = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pivot_index - 1)
        deterministic_quicksort(arr, pivot_index + 1, high)

# Randomized Quicksort
def randomized_partition(arr, low, high):
    random_pivot_index = random.randint(low, high)
    arr[low], arr[random_pivot_index] = arr[random_pivot_index], arr[low]
    return deterministic_partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

# Analysis Function
def analyze_quicksort_performance(arr, variant, num_runs=10):
    total_time = 0
    for _ in range(num_runs):
        arr_copy = list(arr)  # Create a copy of the original array
        start_time = time.time()
        if variant == "deterministic":
            deterministic_quicksort(arr_copy, 0, len(arr_copy) - 1)
        elif variant == "randomized":
            randomized_quicksort(arr_copy, 0, len(arr_copy) - 1)
        end_time = time.time()
        total_time += end_time - start_time

    avg_time = total_time / num_runs
    return avg_time, arr_copy  # Return the sorted array

if __name__ == "__main__":
    input_str = input("Enter the array elements separated by spaces: ")
    arr = [int(x) for x in input_str.split()]

    deterministic_time, deterministic_sorted_array = analyze_quicksort_performance(arr, "deterministic")
    randomized_time, randomized_sorted_array = analyze_quicksort_performance(arr, "randomized")

    print("Original Array:", arr)
    print("Deterministic Quicksort Time:", deterministic_time)
    print("Sorted Array (Deterministic):", deterministic_sorted_array)
    print("Randomized Quicksort Time:", randomized_time)
    print("Sorted Array (Randomized):", randomized_sorted_array)
