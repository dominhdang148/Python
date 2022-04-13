# I. Tái định hình array

#   - Tái định hình nghĩa là thay đổi kích thước của mảng
#   - Kích thước của 1 array là số phần tử trong mỗi chiều của array đó
#   - Bằng cách tái định hình array, ta có thể thêm vào hoặc xóa bỏ các chiều hoặc thay đổi số phần tử ở trong mỗi chiều của array đó

# II. Tái định hình từ mảng 1-D --> 2-D

from os import system
import numpy as np

system('cls')

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newArr = arr.reshape(4, 3)
print(newArr)

# III. Tái định hình tử mảng 1-D --> 3-D

newArr = arr.reshape(2, 3, 2)
print(newArr)

# IV. Có thể tái định hình sang bất kỳ kích thước khác không?

#   - Theo lý thuyết, có thể tại định hình sang bất kì kích thước nào khác, miễn sao có thể chia đủ được số phần tử cho cả hai kích thước
#   - Ta có thể tái định hình mảng 1-D có 8 phần tử sang mảng 2-D có 2 hàng 4 cột. Nhưng ta không thể tái định hình Array đó sang mảng 2
#   chiều gồm 3 hàng 3 cột được do mảng đó gồm 3X3=9 phần tử

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newArr = arr.reshape(3, 3)
# print(newArr)

# V. Trả về mảng copy hay view?

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)

#   Ví dụ trên trả về mảng gốc, do đó đây là mảng view

# VI. Chiều không xác định

#   - Được phép truyền vào 1 chiều không xác định vào trong hàm reshape()
#   - Nghĩa là chúng ta không cần thiết phải đưa ra tất cả các con số chính xác cho hàm replace. Tuy nhiên, chỉ được duy nhất 1 con số là
#   không chính xác
#   - Truyền số -1 vào hàm reshape, NumPy sẽ tự tính toán để đưa ra con số thích hợp

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newArr = arr.reshape(2, 2, -1)
print(newArr)

#   NOTE: không thể truyền số -1 cho nhiều hơn 1 chiều cùng 1 lúc

# VII. Làm phẳng mảng (flattening)

#   - Làm phẳng mảng có nghĩa là chuyển 1 mảng nhiều chiều thành mảng 1 chiều
#   - Có thể sử dụng hàm reshape() với tham số duy nhất -1 để làm điều đó

arr = np.array([[1, 2, 3], [4, 5, 6]])
newArr = arr.reshape(-1)
print(newArr)

# NOTE: Có rất nhiều hàm hỗ trợ cho việc chuyển đối kích thước của Array trong NumPy như flatten, ravel cũng như sắp xếp lại các phần tử
#      như rot90, flip, flipud,... 