from HinhHoc import HinhHoc


class HinhChuNhat(HinhHoc):
    def __init__(self, a, b):
        if a > b:
            self.chieuDai = a
            self.chieuRong = b
        else:
            self.chieuRong = a
            self.chieuDai = b

    def TinhChuVi(self):
        return float((self.chieuDai+self.chieuRong)*2)

    def TinhDienTich(self):
        return float(self.chieuDai*self.chieuRong)

    def __str__(self):
        return "Hinh chu nhat chieu dai "+str(self.chieuDai)+" chieu rong "+str(self.chieuRong)+" co dien tich "+str(self.TinhDienTich()) + " va chu vi "+str(self.TinhChuVi())
