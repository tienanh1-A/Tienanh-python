class HocVien:
    # a) Tạo class học viên với các thuộc tính
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    # b) Tạo phương thức show_info trả về đầy đủ thông tin
    def show_info(self):
        thong_tin = (
            f"Họ tên: {self.ho_ten}\n"
            f"Ngày sinh: {self.ngay_sinh}\n"
            f"Email: {self.email}\n"
            f"Điện thoại: {self.dien_thoai}\n"
            f"Địa chỉ: {self.dia_chi}\n"
            f"Lớp: {self.lop}"
        )
        return thong_tin

    # c) Tạo phương thức change_info với tham số mặc định
    def change_info(self, dia_chi="Hà Nội", lop="IT12.x"):
        self.dia_chi = dia_chi
        self.lop = lop

# d) Chương trình chính
if __name__ == "__main__":
    # Tạo đối tượng thuộc lớp HocVien
    hoc_vien_1 = HocVien(
        ho_ten="Đỗ Văn Tiến Anh", 
        ngay_sinh="20/10/2005", 
        email="tienanhdo94@gmail.com", 
        dien_thoai="0347487198", 
        dia_chi="Hà Nội", 
        lop="IT14"
    )

    # Gọi phương thức show_info để in thông tin ban đầu
    print("=== THÔNG TIN BAN ĐẦU ===")
    print(hoc_vien_1.show_info())

    # Gọi phương thức change_info (không truyền tham số để dùng giá trị mặc định)
    hoc_vien_1.change_info()

    # Gọi lại show_info để kiểm tra sau khi thay đổi
    print("\n=== THÔNG TIN SAU KHI THAY ĐỔI ===")
    print(hoc_vien_1.show_info())