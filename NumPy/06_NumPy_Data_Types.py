# I. Kiểu dữ liệu trong Python

#     - Python có các kiểu dữ liệu build-in (dựng sẵn) sau:

#     +--------------+----------------------------------------------------------------------------+------------------+
#     | KIỂU DỮ LIỆU | PHẠM VI SỬ DỤNG                                                            | GIÁ TRỊ MIMH HỌA |
#     +--------------+----------------------------------------------------------------------------+------------------+
#     | str          | Dùng để biểu diễn dữ liệu văn bản (chuỗi) được đặt trong dấu quote         | "ABCD"           |
#     +--------------+----------------------------------------------------------------------------+------------------+
#     | int          | Dùng để biểu diễn số nguyên                                                | 1, 2, 3, -1, -4  |
#     +--------------+----------------------------------------------------------------------------+------------------+
#     | float        | Dùng để biểu diễn số thực (Dấu chấm động)                                  | 1.5, -2.6, 45.45 |
#     +--------------+----------------------------------------------------------------------------+------------------+
#     | bool         | Dùng để biểu diễn giá trị boolean                                          | True, False      |
#     +--------------+----------------------------------------------------------------------------+------------------+
#     | complex      | Dùng để biểu diễn số phức (phần ảo là j)                                   | 1.5 + 2.6j, 5j   |
#     +--------------+----------------------------------------------------------------------------+------------------+

# II. Kiểu dữ liệu trong NumPy

#    - NumPy có các kiểu dữ liệu mở rộng thêm, vã mỗi kiểu dữ liệu được tham chiếu với 1 chữ cái tương ứng:

#     +--------------+--------------------+---------------------------------------------------------------------+---------------------+
#     | KIỂU DỮ LIỆU | Ý NGHĨA            | PHẠM VI SỬ DỤNG                                                     | GIÁ TRỊ MIMH HỌA    |
#     +--------------+--------------------+---------------------------------------------------------------------+---------------------+
#     | i            | interger           | Sử dụng để biểu diễn các số nguyên                                  | -1, -2, -3, -4      |
#     +--------------+--------------------+---------------------------------------------------------------------+---------------------+
#     | b            | boolean            | Sử dụng để biểu diễn giá trị boolean                                | True, False         |
#     +--------------+--------------------+---------------------------------------------------------------------+---------------------+
#     | u            | unsigned interger  | Sử dụng để biểu diễn số nguyên không âm                             | 1, 2, 3, 4          |
#     +--------------+--------------------+---------------------------------------------------------------------+---------------------+
#     | f            | float              | Sử dụng để biểu diễn số thực                                        | -4.2, 5.1           |
#     +--------------+--------------------+---------------------------------------------------------------------+---------------------+
#     | c            | complex float      | Sử dụng để biểu diễn số phức (bao gồm dấu chấm động)                |  5.2 + 4.0j         |
#     +--------------+--------------------+---------------------------------------------------------------------+---------------------+
#     | m            | timedelta          | Sử dụng để biểu diễn khoảng thời gian chênh lệch                    | 21 days, 2:12:20    |
#     +--------------+--------------------+---------------------------------------------------------------------+---------------------+
#     | M            | datetime           | Sử dụng để biểu diễn 1 mốc thời gian                                | 2019-03-04 00:00:00 |
#     +--------------+--------------------+---------------------------------------------------------------------+---------------------+
#     | O            | object             | Sử dụng để biểu diễn 1 đối tượng                                    | student1, array     |
#     +--------------+--------------------+---------------------------------------------------------------------+---------------------+
#     | S            | string             | Sử dụng để biểu diễn chuỗi                                          | "ABCD"              |
#     +--------------+--------------------+---------------------------------------------------------------------+---------------------+
#     | U            | unicode string     | Sử dụng để biểu diễn chuõi theo chuẩn Unicode                       | "Tiếng Việt"        |
#     +--------------+--------------------+---------------------------------------------------------------------+---------------------+
#     | V            | void               | Sử dụng để biểu diễn dữ liệu thô                                    | JSON                |
#     +--------------+--------------------+---------------------------------------------------------------------+---------------------+

#  III. Kiểm tra kiểu dữ liệu của một mảng

#    - Đối tượng Array của NumPy có một thuộc tính tên dtype trả về kiểu dữ liệu của array đó

from os import system
import numpy as np

system('cls')
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(["apple", "banana", "cherry"])
print(arr.dtype)

# IV. Tạo Mảng với kiểu dữ liệu được định nghĩa trước

#    - Phương thức array còn có 1 tham số tùy ý: dtype cho phép định nghĩa kiểu dữ liệu của mảng ngay khi tạo lập mảng đó

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

#   - Đối với i, u, f, S và U, chúng ta có thể định nghĩa kích thước của kiểu dữ liệu

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

# V. Trường hợp giá trị của phần tử không thể ép kiểu

#    - Nếu một phần tử không thể ép sang 1 kiểu dữ liệu khác, NumPy sẽ báo lỗi ValueError.
#    * ValueError: trong Python, ValueError được gọi khi kiểu của đối số được truyền vào 1 hàm không trùng khớp với kiểu của tham số của hàm đó.

# arr = np.array(['a', '2', '3'], dtype='i')

# VI. Ép kiểu trên một mảng cho sẵn

#    - Cách tốt nhất để chuyển kiểu dữ liệu trên một mảng có sẵn chính là tạo 1 bản sao của mảng đó với phương thức astype().
#    - Hàm astype() sẽ tạo 1 bản sao của mảng đang ép kiểu, và hàm này cho phép ta chuyển hàm đó sang 1 kiểu dữ liệu mới bằng cách truyền tham số vào hàm đó
#    - Kiểu dữ liệu được truyền vào có thể được xác định bằng cách sử dụng chuỗi, như là 'f' cho số thực, 'i' cho số nguyên,... Hoặc cũng có thể sử dụng từ khóa của kiểu dữ liệu đó như float,
#    cho số thực hoặc int cho số nguyên

arr = np.array([1.1, 2.1, 3.1])
newArr = arr.astype('i')
print(newArr)
print(newArr.dtype)

arr = np.array([1,0,3])
newArr=arr.astype(bool)
print(newArr)
print(newArr.dtype)
