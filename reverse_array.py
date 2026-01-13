def reverse_array(arr, index):
    if index < 0:
        return
    print(arr[index], end=" ")
    reverse_array(arr, index - 1)
n = int(input())
arr = list(map(int, input().split()))
reverse_array(arr, n - 1)
