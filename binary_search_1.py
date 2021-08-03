def search(lst, n):
    lst.sort()
    global low, high

    if low <= high:
        mid = (low + high) // 2
        if lst[mid] > n:
            high = mid - 1
            return search(lst, n)
        elif lst[mid] < n:
            low = mid + 1
            return search(lst, n)
        return mid
    return -1


my_list = [34, 25, 6, 9, 12, 134, 54, 68, 2, 7]

low = 0
high = len(my_list) - 1

user = int(input('Enter number to search: '))

search = search(my_list, user)


if search != -1:
    print(f'Found at index {search}')
else:
    print('Not Found')
