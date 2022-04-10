# I. Cài đặt NumPy.

#   - Để cài đặt NumPy một cách dễ dàng, cần cài trước Python và PiP vào máy
#   - Sau đó, mở cửa sổ Terminal/CMD/CommandPromp và gõ dòng lệnh sau để cài đặt NumPy:

#    +------------------------------------------------------------------------+
#    | C:\Users\YourPC> pip install numpy                                     |
#    +------------------------------------------------------------------------+

# II. Gọi thư viện NumPy

#   - Khi NumPy đã được cài đặt, có thể thêm NumPy vào ứng đụng Python bằng từ khóa "import":

import numpy

#   - Bây giờ NumPy đã được thêm vào và sẵn sàng để sử dụng:

arr = numpy.array([1, 2, 3, 4, 5])
print(arr)

# III. Nickname của NumPy

#   - Thông thường, để cho thuận tiện, các lập trính viên sẽ sử dụng từ "np" để thay thế cho NumPy
#   - Sử dụng từ khóa "as" để đặt tên thay thế cho thư viện:

import numpy as np

#   - Bây giờ Thư viện NumPy có thể được gọi bằng "np" thay vì numpy

arr1 = np.array([4, 5, 6, 7, 8])
print(arr1)

# IV. Kiểm tra phiên bản của NumPy

#   - Thông tin về phiên bản của NumPy được lưu trong thuộc tính __version__

print(np.__version__)
