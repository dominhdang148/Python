# I. Tạo một đối tượng ndarray của NumPy

#   - NumPy được sử đụng để làm việc với mảng. Các đối tượng mảng trong NumPy được gọi là ndarray.
#   - Chúng ta có thể tạo ndarray bằng hàm array()

from os import system
from tempfile import tempdir
import numpy as np  # Gọi thư viện NumPy và đặt tên thay thế là np

system('cls')  # Lệnh xóa màn hình CMD

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

#   * type(): Hàm type() là một hàm có sẵn trong Python để cho biết kiểu của đối tượng tham gia làm đối số  của hàm type() đó. Như ví dụ trên, kiểu của đối tượng arr chính là numpy.ndarray
#   - Để tạo một ndarray, chúng ta cũng co thể tryền vào một đối tượng kiểu list, tuple hoặc các cấu trúc dữ liệu tương đương với mảng vào phương thức array()
#   - Phương thức này sẽ chuyển đối tượng làm đối số thành 1 đối tượng ndarray.

arrTup = np.array((6, 7, 8, 9, 10))  # Truyền
print(arrTup)

# II. Các chiều của Array:

#   - Chiều của Array là độ sâu của mảng (Mảng lồng nhau)
#   * Mảng lồng nhau (Mảng đa chiều): là mảng chứa nhiều mảng làm phần tử của nó.

# 1. 0-D Array (Mảng 0 chiều)

#   - Mảng 0 chiều, hoặc mảng vô hướng, là tất cả các phần tử của một Array. Môt giá trị trong 1 mảng được xem là 0-D array

arrZero = np.array(42)
print(arrZero)

# 2. 1-D Array (Mảng 1 chiều)

#   - Một array chứa các phần tử là mảng vô hướng được gọi là mảng 1 chiều (uni-dimensional array) hoặc 1-D array
#   - Đây là mảng phổ biết và cơ bản nhất

arrUni = np.array([2, 4, 5, 6, 7])
print(arrUni)

# 3. 2-D Array (Mảng 2 chiều)

#   - Một mảng chứa các phần tử là mảng 1 chiều được gọi là 2-D array
#   - Mảng 2 chiều thường được dùng để biểu diễn Matrix (Ma trận ) hoặc Tensor 2D
#   * NumPy cũng có một module chuyên dùng để thao tác với ma trận, module này tên là numpy.mat

arrMat = np.array([[1, 2, 3], [4, 5, 6]])
print(arrMat)

# 4. 3-D Array (Mảng 3 chiều)

#   - Một mảng chứa các phần tử là mảng 2 chiều được gọi là 3-D Array (Mảng 3 chiều)
#   - Mảng 3 chiều thường được dùng để biểu diễn Tensor 3D

arrTens = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arrTens)

# III. Kiểm tra số chiều của một Array

#   - Array của NumPy có cung cấp một thuộc tính tên ndim. Thuộc tính này sẽ trả về một số nguyên cho biết số chiều của đối tượng Array đó.

print(arrZero.ndim)
print(arrUni.ndim)
print(arrMat.ndim)
print(arrTens.ndim)

# IV. Thêm chiều cho mảng

#   - Một Array có thể có Nhiều chiều theo ý muốn của lập trình viên
#   - Khi một array được tạo ra, có thể xác định số chiều của Array đó bằng tham số ndmin

arr_5D = np.array([1, 2, 3, 4], ndmin=5)        # Tuy ta chỉ truyền list 1 chiều vào trong hàm, nhưng hàm sẽ tạo ra 1 mảng 5 chiều do ta đã truyền tham số ndmin=5 vào hàm
print(arr_5D)
print("Chiều của arr_5D là: ", arr_5D.ndim)

#   - Trong Array arr_5D, chiều cuối cùng (chiều thứ 5) có 4 phần tử, chiều thứ 4 có 1 phần tử là vector, chiều thứ 3 có 1 phần từ là ma trận với vector, chiều thứ 2 có 1 phần tử là một
#   mảng 3 chiều và chiều thứ nhất có một phần tử là một mảng 4 chiều.
