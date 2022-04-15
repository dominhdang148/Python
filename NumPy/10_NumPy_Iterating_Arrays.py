# I. Lặp trên mảng (Iterating Arrays)

#   - Iterating (lặp) nghĩa là đi qua từng phần tử 1 trong một Array (Có thể hiểu là duyệt mảng)
#   - Khi xử lý mảng nhiều chiều trong NumPy, chúng ta có thể duyệt mảng bằng vòng lặp for cơ bản trong Python
# Nếu chúng ta duyệt 1 mảng 1 chiều, nó sẽ đi qua từng phần tử 1 của mảng đó

from os import system
import numpy as np

system('cls')

arr = np.array([1, 2, 3])
for x in arr:
    print(x)

#  II. Duyệt mảng 2 chiều

#   - Khi duyệt mảng 2 chiều, nó sẽ đi qua các hàng của mảng đó

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)

#   NOTE: Nếu ta duyệt mảng n chiều, nó sẽ sẽ đi qua từng chiều thứ n-1 của mảng đó
#   - Để trả về giá trị thực sự của các phần tử, ta phải duyệt từng chiều của mảng đó:

for x in arr:
    for y in x:
        print(y)

# III. Duyệt mảng 3 chiều

#   - Khi duyệt mảng 3 chiều, quá trình duyệt mảng sẽ đi qua mảng 2 chiều

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print(x)

#   - Để trả về giá trị thực sự của các phần tử, ta phải duyệt từng chiều của mảng đó

for x in arr:
    for y in x:
        for z in y:
            print(z)

# IV. Duyệt mảng bằng nditer()

#   - Hàm nditer() là 1 hàm hỗ trợ (helping function) có thể được sử dụng cho các thuật tnán duyệt từ đơn giản nhất đến phức tạp nhất. Nó giải quyết một số vấn đề cơ bản thường hay gặp
#   trong khi duyệt mảng.

#   * Duyệt từng phần tử vô hướng của 1 mảng n chiều:

#   - Đối với vòng lặp for của python thuần, muốn duyệt các phần tử vô hương, ta phải dùng n vòng lặp -> gây khó khăn đối với những mảng có số chiều rất cao.
#   - Trong khi đó, hàm nditer(array) sẽ giúp ta duyệt các phần tử vô hướng của mảng n chiều chỉ với 1 vòng lặp

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)

# V. Duyệt mảng với cá c kiểu dữ liệu khác nhau:

#   - Chúng ta có thể sử dụng đối số op_dtypes và tryền vào phương thức nditer() kí tự đại diện cho các kiểu mà NumPy quy ước để thay đổi kiểu dữ liệu của các phần tử khi duyệt mảng
#   - NumPy không thay đổi kiểu dữ liệu của các phần tử một cách trực tiếp --> Cần 1 khoảng trống trong bộ nhớ để chuyển kdl cho các phần tử.
#   - Khoảng trống này được gọi là bộ nhớ đệm (buffer) và để kích hoạt buffer trong nditer(), truyền flags=['buffered']

arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

# VI. Duyệt mảng với bước duyệt khác nhau

#   - Ta có thể sử dụng bộ lọc, theo sao đó là thao tác duyệt

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):    # Duyệt tất cả phần tử vô hướng và bỏ qua 1 phần tử
    print(x)

# VII. Duyệt liệt kê bằng ndenumerate()

#   - Liệt kê (Enumeration) nghĩa là đề cập đến số thứ tự của từng phần tử một trong Array

#   - Trong quá trình duyệt mảng, đôi khi duyệt cả chỉ số index của phần tử đang duyệt cũng cần thiết. Vì thế, phương thúc ndenumerate() được sử dụng cho phép liệt kê này.

arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)