def binary_search(arr, value):
    if len(arr) == 1 and arr[0] != value:
        return False
    if arr[0] == value:
        return True
    mid_point = len(arr)//2
    if value < arr[mid_point]:
        return binary_search(arr[:mid_point], value)
    else:
        return binary_search(arr[mid_point:], value)

def find_sum(s, x):
    for elem in s:
        value = x - elem
        if binary_search(s, value):
            return 1
    return -1
        
if __name__ == '__main__':
    s = list(range(1000))
    x = 1500
    print(find_sum(s, x))
