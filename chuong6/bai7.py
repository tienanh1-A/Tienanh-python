_list = [11, 2, 23, 45, 6, 9]

max_value = _list[0]  # giả sử phần tử đầu là lớn nhất

for num in _list:
    if num > max_value:
        max_value = num

print(max_value)