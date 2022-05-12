def binary_search(li,val):

    left = 0
    right = len(li) - 1

    while left <= right:
        mid = (left + right) // 2
        print(li[mid])
        if li[mid] == val:
            return mid

        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    return None

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

binary_search(li,11)