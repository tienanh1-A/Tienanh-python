# ===== BÀI 1 =====
print("=== Bài 1 ===")
_tuple = ('a', 'b', 'd', 'e')

# Chuyển sang list để thêm phần tử
temp = list(_tuple)
temp.insert(2, 'c')

_new_tuple = tuple(temp)
print("Kết quả:", _new_tuple)


# ===== BÀI 2 =====
print("\n=== Bài 2 ===")
_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

_new_tuple = ()

for i in _tuple:
    if _tuple.count(i) == 1:
        _new_tuple += (i,)

print("Kết quả:", _new_tuple)


# ===== BÀI 3 =====
print("\n=== Bài 3 ===")
_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

_new_tuple = ()

for i in _tuple:
    if i not in _new_tuple:
        _new_tuple += (i,)

print("Kết quả:", _new_tuple)