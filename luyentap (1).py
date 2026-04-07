# Bảng mã hóa
encode_dict = {'a': '!', 'b': '@', 'c': '#', 'd': '$'}

# Tạo bảng giải mã (đảo ngược)
decode_dict = {v: k for k, v in encode_dict.items()}


# Hàm mã hóa
def encode(text):
    result = ""
    for ch in text:
        if ch in encode_dict:
            result += encode_dict[ch]
        else:
            result += ch  # giữ nguyên nếu không có trong bảng
    return result


# Hàm giải mã
def decode(text):
    result = ""
    for ch in text:
        if ch in decode_dict:
            result += decode_dict[ch]
        else:
            result += ch
    return result


# ====== TEST ======
text = input("Nhập văn bản: ")

ma_hoa = encode(text)
print("Mã hóa:", ma_hoa)

giai_ma = decode(ma_hoa)
print("Giải mã:", giai_ma)