def binary_search(arr, value):
    if len(arr) == 1 and arr[0] != value:
        return -1
    if arr[0] == value:
        return 1
    mid_point = len(arr)//2
    if value < arr[mid_point]:
        return binary_search(arr[:mid_point], value)
    else:
        return binary_search(arr[mid_point:], value)

listing = list(range(200))
print(binary_search(listing, 204))
