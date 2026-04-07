class HocVien:
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    # b) Hiển thị thông tin
    def show_info(self):
        print("Họ tên:", self.ho_ten)
        print("Ngày sinh:", self.ngay_sinh)
        print("Email:", self.email)
        print("Điện thoại:", self.dien_thoai)
        print("Địa chỉ:", self.dia_chi)
        print("Lớp:", self.lop)

    # c) Thay đổi thông tin
    def change_info(self, dia_chi="Hà Nội", lop="IT12.x"):
        self.dia_chi = dia_chi
        self.lop = lop


# d) Chương trình chính
hv = HocVien("Nguyen Van A", "01/01/2000", "a@gmail.com", "0123456789", "HCM", "IT10")

print("=== Thông tin ban đầu ===")
hv.show_info()

hv.change_info()  # dùng mặc định

print("\n=== Sau khi cập nhật ===")
hv.show_info()