Buổi 2
- kiểu giá trị String
    + khai báo biến String
    + thao tác với String: index, độ dài String, cộng/nhân String
-kiểu giá trị số:
    + phân biệt đươcj: int và float
    + các toan tử với số: +, -, *, /, **, %, //
    + phân biệt "5" và 5
    + biết cách chuyển từ String => Số và ngược lại
.index đại diện cho vị trí ký tự trong string

Buổi 3
- giới thiệu về kiểu dữ liệu: Boolean(True/False)
- các phép toán có thể trả về Boolean: toán tử so sánh:>,<,>=,<=,!=,==
- cách sử dụng câu lệnh điều kiện: if...

Buổi 4
- sử dụng vòng lặp
- phân biệt phong lặp for và while(khi sử dụng)

range(x): tạo ra 1 tập hợp các số nguyên với số đầu, số cuối, khoảng cách  giữa các số do người dùng nhập vào
- phạm vi này có số lượng là x phần tử
- chỉ áp dụng cho int number
- luôn bắt đầu từ số 0 đến x-1
- cú pháp:
range(start,stop,step):
range(start,stop): step mặc định là 1
range(stop): start bắt đầu từ 0

vòng lặp for: cú pháp
for var_name in <collection>:
    ........

buổi 6
- list in python: 
 +) list là 1 kiểu dữ liệu dùng để lưu trữ nhiều giá trị cùng 1 lúc
 +) khai báo list:
        a = []
+) khai báo biến có giá trị:
        shoppingList = []
- phương thức đếm số thứ tự danh sách: lend()
- list.append(): thêm phần tử vào cuối list
- list.clear: xoá toàn bộ phần tử
- tìm kiếm trong danh sách:
- duyệt danh sách với vòng lặp
- sao chép mảng
s = [1,2,3]
b=a.copy()
print(a)
- extend

- tuple: là kiểu dữ liệu dùng để lưu trữ tập hợp các phần tử. Tương tự với list nhưng có điểm khác biệt.
- turple: không thể thay đổi sau khi đc tạo. không thêm, bớt, sửa, xoá với nó.
- được định nghĩa bằng dấu ngoặc tròn () và các phần tử nằm bên trong ngoặc đó.
-tuple: thường nhanh hơn list khi thực hiện các thao tác tìm kiếm.