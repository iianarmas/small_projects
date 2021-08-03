def search(lst, low, high, n):
    lst.sort()

    if low <= high:
        mid = (low + high) // 2
        if lst[mid] > n:
            return search(lst, low, mid - 1, n)
        elif lst[mid] < n:
            return search(lst, mid + 1, high, n)
        return mid
    return -1


my_list = [34, 25, 6, 9, 12, 134, 54, 68, 2, 7]

user = int(input('Enter number to search: '))

search = search(my_list, 0, len(my_list) - 1, user)

if search != -1:
    print(f'Found at index {search}')
else:
    print('Not Found')
