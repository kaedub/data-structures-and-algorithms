def binary_search(arr, target):
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if arr[mid] == target:
            found = True
        else:
            if target < arr[mid]:
                last = mid  - 1
            else:
                first = mid + 1

    return mid if found else -1
    

def count_zeroes(arr):
    if arr[0] == 0:
        return len(arr)
    elif arr[-1] == 1:
        return 0

    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2
    while mid < len(arr)-1 and mid > 0:
        # if mid item is a 0
        if arr[mid] == 0:
            # if item to left is 1, return zero count
            if arr[mid-1] == 1:
                return len(arr) - mid
            # else set right to item to the left of mid and move mid to left
            else:
                right = mid - 1
                mid = mid // 2
        # if mid item is a 1
        if arr[mid] == 1:
            # return zero count if item to right is a 0
            if arr[mid+1] == 0:
                return len(arr) - (mid + 1)
            # else set left to item to the right of mid and move mid to right
            else:
                left = mid + 1
                mid = (left + right) // 2
    return 0


def sorted_frequency(arr, target):
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2

    while left <= right:
        if arr[mid] > target:
            pass
        elif arr[mid] < target:
            pass
        else:
            pass


print(sorted_frequency([1,1,2,2,2,2,3],2))  # 4
print(sorted_frequency([1,1,2,2,2,2,3],3))  # 1
print(sorted_frequency([1,1,2,2,2,2,3],1))  # 2
print(sorted_frequency([1,1,2,2,2,2,3],4) ) # -1

    

z = [[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0], 
    [1,1,1,1,1,1,1], 
    [1,1,1,1,1,1,1,0], 
    [1,0,0,0,0,0], 
    [0,0,0]]
print('\n---> count_zeroes()')
print('z1 should have 11 zeros:      ', count_zeroes(z[0]) == 11)
print('z2 should have  0 zeros:      ', count_zeroes(z[1]) == 0)
print('z3 should have  1 zeros:      ', count_zeroes(z[2]) == 1)
print('z4 should have  5 zeros:      ', count_zeroes(z[3]) == 5)
print('z5 should have  3 zeros:      ', count_zeroes(z[4]) == 3)

a = [1,2,3,4,5,6,7,8]
b = list(range(10,50))
print('\n---> binary_seach()')
print('find  6 in [1,2,3,4,5,6,7,8]: ', binary_search(a, 6))
print('find 29 in [10,...,49]:       ', binary_search(b, 29))
print('find  2 in [10,...,49]:       ', binary_search(b, 2))
print('find 88 in [10,...,49]:       ', binary_search(b, 88))