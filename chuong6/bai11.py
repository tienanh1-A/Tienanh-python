# Nhập n từ bàn phím
n = int(input("Nhập n: "))

# List cho trước
_list = ['abc', 'xyz', 'hello', 'python', 'hi']

# Tìm các từ có độ dài > n
ket_qua = []

for i in _list:
    if len(i) > n:
        ket_qua.append(i)

print("Các từ thỏa mãn:", ket_qua)