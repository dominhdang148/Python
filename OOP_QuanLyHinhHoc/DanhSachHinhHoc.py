from HinhHoc import HinhHoc
from HinhVuong import HinhVuong
from HinhTron import HinhTron
from HinhChuNhat import HinhChuNhat


class DanhSachHinhHoc():
    def __init__(self):
        self.danhSach = []
# region Input/Output``

    def ThemHinh(self, hinhHoc):
        self.danhSach.append(hinhHoc)

    def DocFile(self, path):
        line = "123"
        with open(path, 'r') as fileReader:
            hh = 0
            while ((line := fileReader.readline()) != ""):
                str = line.split(' ')
                if str[0] == "HV":
                    hh = HinhVuong(int(str[1]))
                elif str[0] == "HT":
                    hh = HinhTron(int(str[1]))
                elif str[0] == "HCN":
                    hh = HinhChuNhat(int(str[1]), int(str[2]))
                self.ThemHinh(hh)

    def __str__(self):
        s = "\n=============================== DANH SACH HINH HOC ===============================\n"
        for hinh in self.danhSach:
            s += str(self.danhSach.index(hinh)+1)+". "+str(hinh)+'\n'
        s += "==================================================================================\n"
        return s
# endregion

# region Hình Vuông
    def TimHinhVuongCoChuVi(self, x):
        result = DanhSachHinhHoc()
        for hinh in self.danhSach:
            if (type(hinh) is HinhVuong and hinh.TinhChuVi() == x):
                result.ThemHinh(hinh)
        return result

    def TimHinhVuongCoDienTich(self, x):
        result = DanhSachHinhHoc()
        for hinh in self.danhSach:
            if (type(hinh) is HinhVuong and hinh.TinhDienTich() == x):
                result.ThemHinh(hinh)
        return result

    def TimChuViHinhVuongNhoNhat(self):
        min = 10000000000000000000000
        for hinh in self.danhSach:
            if type(hinh) is HinhVuong and hinh.TinhChuVi() < min:
                min = hinh.TinhChuVi()
        return min

    def TimChuViHinhVuongLonNhat(self):
        max = -1
        for hinh in self.danhSach:
            if type(hinh) is HinhVuong and hinh.TinhChuVi() > max:
                max = hinh.TinhChuVi()
        return max

    def TimHinhVuongCoChuViNhoNhat(self):
        return self.TimHinhVuongCoChuVi(self.TimChuViHinhVuongNhoNhat())

    def TimHinhVuongCoChuViLonNhat(self):
        return self.TimHinhVuongCoChuVi(self.TimChuViHinhVuongLonNhat())

# endregion

# region Hình Tròn
    def TimHinhTronCoChuVi(self, x):
        result = DanhSachHinhHoc()
        for hinh in self.danhSach:
            if (type(hinh) is HinhTron and hinh.TinhChuVi() == x):
                result.ThemHinh(hinh)
        return result

    def TimHinhTronCoDienTich(self, x):
        result = DanhSachHinhHoc()
        for hinh in self.danhSach:
            if (type(hinh) is HinhTron and hinh.TinhDienTich() == x):
                result.ThemHinh(hinh)
        return result

    def TimChuViHinhTronNhoNhat(self):
        min = 10000000000000000000000
        for hinh in self.danhSach:
            if type(hinh) is HinhTron and hinh.TinhChuVi() < min:
                min = hinh.TinhChuVi()
        return min

    def TimChuViHinhTronLonNhat(self):
        max = -1
        for hinh in self.danhSach:
            if type(hinh) is HinhTron and hinh.TinhChuVi() > max:
                max = hinh.TinhChuVi()
        return max

    def TimHinhTronCoChuViNhoNhat(self):
        return self.TimHinhTronCoChuVi(self.TimChuViHinhTronNhoNhat())

    def TimHinhTronCoChuViLonNhat(self):
        return self.TimHinhTronCoChuVi(self.TimChuViHinhTronLonNhat())
    
# endregion

# region Hình Chữ Nhật
    def TimHinhChuNhatCoChuVi(self, x):
        result = DanhSachHinhHoc()
        for hinh in self.danhSach:
            if type(hinh) is HinhChuNhat and hinh.TinhChuVi() == x:
                result.ThemHinh(hinh)
        return result

    def TimHinhChuNhatCoDienTich(self, x):
        result = DanhSachHinhHoc()
        for hinh in self.danhSach:
            if type(hinh) is HinhChuNhat and hinh.TinhDienTich() == x:
                result.ThemHinh(hinh)
        return result
    
    def TimChuViHinhChuNhatNhoNhat(self):
        min = 10000000000000000000000
        for hinh in self.danhSach:
            if type(hinh) is HinhChuNhat and hinh.TinhChuVi() < min:
                min = hinh.TinhChuVi()
        return min

    def TimChuViHinhChuNhatLonNhat(self):
        max = -1
        for hinh in self.danhSach:
            if type(hinh) is HinhChuNhat and hinh.TinhChuVi() > max:
                max = hinh.TinhChuVi()
        return max

    def TimHinhChuNhatCoChuViNhoNhat(self):
        return self.TimHinhChuNhatCoChuVi(self.TimChuViHinhChuNhatNhoNhat())

    def TimHinhChuNhatCoChuViLonNhat(self):
        return self.TimHinhChuNhatCoChuVi(self.TimChuViHinhChuNhatLonNhat())
# endregion
