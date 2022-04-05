
# --------------- File thực thi (Khi chạy chương trình thì gọi file này) --------------

from HinhHoc import HinhHoc
from HinhVuong import HinhVuong
from HinhTron import HinhTron
from HinhChuNhat import HinhChuNhat
# ==================== Khai báo thư viện (modules) ====================
from DanhSachHinhHoc import DanhSachHinhHoc
from os import system
import MenuModule
# =====================================================================

menu = 'a'
#danhSach=DanhSachHinhHoc()
while menu != 0:
    menu = MenuModule.ChonMenu()
    MenuModule.XuLyMenu(menu)
system('cls')


