def bubble_sort(arr):
    n = len (arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

def request_input():
    user_input = input("Enter numbers separated by spaces: ")
    arr = list(map(int, user_input.split()))
    return arr

if __name__ == "__main__":
    arr = request_input()
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)
