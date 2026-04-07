# Nhập n
n = int(input("Nhập n: "))

# List cho trước
_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']

dem = 0

for i in _list:
    if len(i) >= n and i[0] == i[-1]:
        dem += 1

print("Số chuỗi thỏa mãn:", dem)