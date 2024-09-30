def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

def get_input():
    user_input = input("Enter numbers separated by spaces: ")
    arr = list(map(int, user_input.split()))
    return arr

if __name__ == "__main__":
    arr = get_input()
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)
