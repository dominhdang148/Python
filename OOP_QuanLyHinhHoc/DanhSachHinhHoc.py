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

    def TimHinhCoDienTich(self,x, hinh=HinhHoc):
        result =DanhSachHinhHoc()
        for hh in self.danhSach:
            if type(hh)is hinh and hh.TinhDienTich()==x:
                result.ThemHinh(hh)
        return result

    def TimChuViMax(self,hinh=HinhHoc):
        max= -1
        for hh in self.danhSach:
            if type(hh)is hinh and hh.TinhChuVi()>max:
                max=hh.TinhChuVi()
        return max
    
    def TimChuViMin(self,hinh=HinhHoc):
        min= 1000000000000000000000000
        for hh in self.danhSach:
            if type(hh)is hinh and hh.TinhChuVi()<min:
                min=hh.TinhChuVi()
        return min
    
    def TimDienTichTinhDienTichMax(self,hinh=HinhHoc):
        max= -1
        for hh in self.danhSach:
            if type(hh)is hinh and hh.TinhDienTich()>max:
                max=hh.TinhDienTich()
        return max

    def TimDienTichTinhDienTichMin(self,hinh=HinhHoc):
        min= 1000000000000000000000000
        for hh in self.danhSach:
            if type(hh)is hinh and hh.TinhDienTich()<min:
                min=hh.TinhDienTich()
        return min

    def TimHinhCoChuViLonNhat(self, hinh=HinhHoc,):
        return self.TimHinhCoChuVi(self.TimChuViMax(hinh),hinh)

    def TimHinhCoChuViNhoNhat(self, hinh=HinhHoc,):
        return self.TimHinhCoChuVi(self.TimChuViMin(hinh),hinh)

# endregion
