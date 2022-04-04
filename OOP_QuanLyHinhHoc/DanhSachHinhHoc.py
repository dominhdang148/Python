
from HinhHoc import HinhHoc
from HinhVuong import HinhVuong
from HinhTron import HinhTron
from HinhChuNhat import HinhChuNhat


class DanhSachHinhHoc:
    def __init__(self):
        self.danhSach = []
# region Input/Output

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

# region Generic
    def TimHinhCoChuVi(self, x, hinh=HinhHoc):
        result = DanhSachHinhHoc()
        for hh in self.danhSach:
            if type(hh) is hinh and hh.TinhChuVi() == x:
                result.ThemHinh(hh)
        return result

    def TimHinhCoDienTich(self, x, hinh=HinhHoc):
        result = DanhSachHinhHoc()
        for hh in self.danhSach:
            if type(hh) is hinh and hh.TinhDienTich() == x:
                result.ThemHinh(hh)
        return result

    def TimChuViMax(self, hinh=HinhHoc):
        max = -1
        for hh in self.danhSach:
            if type(hh) is hinh and hh.TinhChuVi() > max:
                max = hh.TinhChuVi()
        return max

    def TimChuViMin(self, hinh=HinhHoc):
        min = 1000000000000000000000000
        for hh in self.danhSach:
            if type(hh) is hinh and hh.TinhChuVi() < min:
                min = hh.TinhChuVi()
        return min

    def TimDienTichMax(self, hinh=HinhHoc):
        max = -1
        for hh in self.danhSach:
            if type(hh) is hinh and hh.TinhDienTich() > max:
                max = hh.TinhDienTich()
        return max

    def TimDienTichMin(self, hinh=HinhHoc):
        min = 1000000000000000000000000
        for hh in self.danhSach:
            if type(hh) is hinh and hh.TinhDienTich() < min:
                min = hh.TinhDienTich()
        return min

    def TimHinhCoChuViLonNhat(self, hinh=HinhHoc,):
        if hinh != HinhHoc:
            return self.TimHinhCoChuVi(self.TimChuViMax(hinh), hinh)
        else:
            return self.TimHinhChungCoChuVi(self.TimChuViHinhLonNhat())

    def TimHinhCoChuViNhoNhat(self, hinh=HinhHoc,):
        if hinh != HinhHoc:
            return self.TimHinhCoChuVi(self.TimChuViMin(hinh), hinh)
        else:
            return self.TimHinhChungCoChuVi(self.TimChuViHinhNhoNhat())

    def TimHinhCoDienTichLonNhat(self, hinh=HinhHoc):
        if hinh != HinhHoc:
            return self.TimHinhCoDienTich(self.TimDienTichMax(), hinh)
        else:
            return self.TimHinhChungCoDienTich(self.TimDienTichHinhLonNhat())

    def TimHinhCoDienTichNhoNhat(self, hinh=HinhHoc):
        if hinh != HinhHoc:
            return self.TimHinhCoDienTich(self.TimDienTichMin(), hinh)
        else:
            return self.TimHinhChungCoDienTich(self.TimDienTichHinhNhoNhat())

    def TinhTongDienTichHinh(self, hinh=HinhHoc):
        sum = 0
        for graph in self.danhSach:
            if type(graph) is hinh:
                sum += graph.TinhDienTich()
        return sum

    def TinhTongChuViHinh(self, hinh=HinhHoc):
        sum = 0
        for graph in self.danhSach:
            if type(graph) is hinh:
                sum += graph.TinhChuVi()
        return sum

    def DemSoLuongHinh(self, hinh=HinhHoc):
        count = 0
        for graph in self.danhSach:
            if type(graph) is hinh:
                count += 1
        return count

    # endregion

# region Non_Generic

    def TimHinhVuongCoCanh(self, edge):
        result = DanhSachHinhHoc()
        for hinh in self.danhSach:
            if type(hinh) is HinhVuong and hinh.canh == edge:
                result.ThemHinh(hinh)
        return result

    def TimHinhTronCoBanKinh(self, radius):
        result = DanhSachHinhHoc()
        for hinh in self.danhSach:
            if type(hinh) is HinhTron and hinh.banKinh == radius:
                result.ThemHinh(hinh)
        return result

    # Truyền số 0 vào hàm -> Tìm chiều rộng
    # Truyền số 1 vào hàm _> Tìm chiều dài
    def TimHinhChuNhatCoChieuDai_ChieuRong(self, edge, condition):
        result = DanhSachHinhHoc()
        for hinh in self.danhSach:
            if condition != 0:
                if type(hinh) is HinhChuNhat and hinh.chieuDai == edge:
                    result.ThemHinh(hinh)
            else:
                if type(hinh) is HinhChuNhat and hinh.chieuRong == edge:
                    result.ThemHinh(hinh)
        return result

    def TimCanhHinhVuongLonNhat(self):
        max = -1
        for Hinh in self.danhSach:
            if type(Hinh) is HinhVuong and Hinh.canh > max:
                max = Hinh.canh
        return max

    def TimBanKinhHinhTronLonNhat(self):
        max = -1
        for Hinh in self.danhSach:
            if type(Hinh) is HinhTron and Hinh.banKinh > max:
                max = Hinh.banKinh
        return max

    def TimChieuDaiHinhChuNhatLonNhat(self):
        max = -1
        for Hinh in self.danhSach:
            if type(Hinh) is HinhChuNhat and Hinh.chieuDai > max:
                max = Hinh.chieuDai
        return max

    def TimCanhHinhVuongNhoNhat(self):
        min = 10000000000000000000
        for Hinh in self.danhSach:
            if type(Hinh) is HinhVuong and Hinh.canh < min:
                min = Hinh.canh
        return min

    def TimBanKinhHinhTronNhoNhat(self):
        min = 10000000000000000000
        for Hinh in self.danhSach:
            if type(Hinh) is HinhTron and Hinh.banKinh < min:
                min = Hinh.banKinh
        return min

    def TimChieuRongHinhChuNhatNhoNhat(self):
        min = 10000000000000000000
        for Hinh in self.danhSach:
            if type(Hinh) is HinhChuNhat and Hinh.chieuRong < min:
                min = Hinh.chieuRong
        return min

    # Truyền số 0 vào hàm -> Tìm hình vuông có cạnh nhỏ nhất
    # Truyền số 1 vào hàm -> Tìm hình vuông có cạnh lớn nhất
    def TimHinhVuongCoCanhLonNhat_NhoNhat(self, condition):
        if condition == 0:
            return self.TimHinhVuongCoCanh(self.TimCanhHinhVuongNhoNhat())
        else:
            return self.TimHinhVuongCoCanh(self.TimCanhHinhVuongLonNhat())

    # Truyền số 0 vào hàm -> Tìm hình tròn có bán kính nhỏ nhất
    # Truyền số 1 vào hàm -> Tìm hình tròn có bán kính lớn nhất
    def TimHinhTronCoBanKinhLonNhat_NhoNhat(self, condition):
        if condition == 0:
            return self.TimHinhTronCoBanKinh(self.TimBanKinhHinhTronNhoNhat())
        else:
            return self.TimHinhTronCoBanKinh(self.TimBanKinhHinhTronLonNhat())

    # Truyền số 0 vào hàm -> Tìm hình chữ nhật có chiều rộng nhỏ nhất
    # Truyền số 1 vào hàm -> Tìm hình chữ nhật có chiều dàilớn nhất
    def TimHinhChuNhatCoCD_CRLonNhat_NhoNhat(self, condition):
        if condition == 0:
            return self.TimHinhChuNhatCoChieuDai_ChieuRong(self.TimChieuRongHinhChuNhatNhoNhat(), condition)
        else:
            return self.TimHinhChuNhatCoChieuDai_ChieuRong(self.TimChieuDaiHinhChuNhatLonNhat(), condition)

    # def SapXepDanhSachHinh(self, condition)
    #     self.danhSach.sort(key=)/

    def TimChuViHinhLonNhat(self):
        max = -1
        for hinh in self.danhSach:
            if hinh.TinhChuVi() > max:
                max = hinh.TinhChuVi()
        return max

    def TimChuViHinhNhoNhat(self):
        min = 1000000000000000000
        for hinh in self.danhSach:
            if hinh.TinhChuVi() < min:
                min = hinh.TinhChuVi()
        return min

    def TimHinhChungCoChuVi(self, x):
        result = DanhSachHinhHoc()
        for hinh in self.danhSach:
            if hinh.TinhChuVi() == x:
                result.ThemHinh(hinh)
        return result

    def TimDienTichHinhLonNhat(self):
        max = -1
        for hinh in self.danhSach:
            if hinh.TinhDienTich() > max:
                max = hinh.TinhDienTich()
        return max

    def TimDienTichHinhNhoNhat(self):
        min = 1000000000000000
        for hinh in self.danhSach:
            if hinh.TinhDienTich() < min:
                min = hinh.TinhDienTich()
        return min

    def TimHinhChungCoDienTich(self, x):
        result = DanhSachHinhHoc()
        for hinh in self.danhSach:
            if hinh.TinhDienTich() == x:
                result.ThemHinh(hinh)
        return result

    def XoaHinhCoChuVi(self, x):
        for hinh in self.danhSach:
            if hinh.TinhChuVi() == x:
                self.danhSach.remove(hinh)

    def XoaHinhCoDienTich(self, x):
        for hinh in self.danhSach:
            if hinh.TinhDienTich() == x:
                self.danhSach.remove(hinh)

    # condition = 0 -> Xóa hình có chu vi nhỏ nhất
    # condition = 1 -> Xóa hính có chu vi lớn nhất
    def XoaHinhCoChuViLonNhat_NhoNhat(self, condition):
        if condition == 0:
            self.XoaHinhCoChuVi(self.TimChuViHinhNhoNhat())
        else:
            self.XoaHinhCoChuVi(self.TimChuViHinhLonNhat())

    # condition = 0 -> Xóa hình có chu vi nhỏ nhất
    # condition = 1 -> Xóa hính có chu vi lớn nhất
    def XoaHinhCoDienTichLonNhat_NhoNhat(self, condition):
        if condition == 0:
            self.XoaHinhCoDienTich(self.TimDienTichHinhNhoNhat())
        else:
            self.XoaHinhCoDienTich(self.TimDienTichHinhLonNhat())
# endregion
