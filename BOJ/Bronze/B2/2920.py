list = list(map(int, input().split()))

list_asc = sorted(list)
list_dsc = sorted(list, reverse=True)

if list == list_asc:
    print('ascending')
elif list == list_dsc:
    print('descending')
else:
    print('mixed')