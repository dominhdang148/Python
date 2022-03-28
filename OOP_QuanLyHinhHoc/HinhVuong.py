from mimetypes import init
from HinhHoc import HinhHoc


class HinhVuong(HinhHoc):
    canh = 0

    def __init__(self, edge):
        self.canh = edge

    def TinhChuVi(self):
        return float(self.canh*4)

    def TinhDienTich(self):
        return float(self.canh*self.canh)

    def __str__(self):
        return "Hinh vuong canh "+str(self.canh)+" co dien tich "+str(self.TinhDienTich())+" va chu vi "+str(self.TinhChuVi())
