class NhanVien:
    'Lớp mô tả cho mọi nhân viên'
    dem = 0

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        
        NhanVien.dem += 1

    def hien_thi_so_luong(self):
        print("Tổng số nhân viên được tạo: %d" % NhanVien.dem)

    def hien_thi_nhan_vien(self):
        print("Tên:", self.__name, ", Lương:", self.__salary)

    def cap_nhat(self, name=None, salary=None):
        if name is not None:
            self.__name = name
        if salary is not None:
            self.__salary = salary



nhan_vien_dev = NhanVien('Nguyen Van A', 1000)
nhan_vien_test = NhanVien('Nguyen Van B', 1200)

print("--- Thông tin nhân viên ---")
nhan_vien_dev.hien_thi_nhan_vien()
nhan_vien_test.hien_thi_nhan_vien()

print("\n--- Biến của Class ---")
print("Tổng số nhân viên (dùng biến dem):", nhan_vien_dev.dem)

print("\n--- Truy cập thuộc tính ---")

print("Tên Dev (Cách 1):", nhan_vien_dev._NhanVien__name) 
print("Tên Test (Cách 1):", nhan_vien_test._NhanVien__name)