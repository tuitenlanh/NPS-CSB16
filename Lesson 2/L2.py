# khai bao bien(ten = kdl)
# str1 = "hello world"
# str2 = 'hi!'
# print(str1)
# print (str1[3])
# str3 = """đây là đoạn chuỗi được viết trong 3 dấu ngoặc
# đây là dòng thứ 2
# đây là dòng thứ 3"""
# đối với 3 dấu ngoặc kép: có thể sử dụng để tạo chuỗi đa dòng
# print(str3)

#in ra số lượng ký tự trong chuỗi:len()
# print(len(str3))

# cộng string: string + string = string
# print(str1 +" "+str2)

# truyền biến vào trong chuỗi
# job = input("job: ")
# print(f"i am a {job}")

# tách chuỗi: hello world
# str1_tachchuoi = str1[6:11]
# print(str1_tachchuoi)

# int
# student = 20
# late_student = 0

# float
# height = 4.0
# weight = 12.

# toán tử
# a = 1
# b = 2
# print(a>b or a<b)
# print(a<b and a<0)
# c = True
# toán tử not
# print(not c)

# homewwork
# 1.in ra terminal câu "xin chào tên của 3 thành viên trong lớp", mỗi tên 1 dòng
# 2.hỏi người dùng nhập tên, sau đó in ra câu chào mọi người
# 3.viết chương trình tính tổng, hiểuk, tích, thương 2 số do người dùng nhập vào
# 4.sử dụng turtle vẽ hình lục giác, ngũ giác

# # bài 1
a = "lê anh"
b = "khuê"
c = "trí"
print(f"""xin chào
{a}
{b}
{c}""")

# # bài 2
d = input("tên bạn là gì: ")
print(f"hello {d}")

# # bài 3
e = float(input("số thứ nhất: "))
f = float(input("số thứ 2: "))
g = e+f
h = e-f
i = e*f
j = e/f
print(g)
print(h)
print(i)
print(j)


# bài 4
# lục giác
from turtle import *
forward(100)
left(60)
forward(100)
left(60)
forward(100)
left(60)
forward(100)
left(60)
forward(100)
left(60)
forward(100)
mainloop()

# ngữ giác
from turtle import *
forward(100)
left(72)
forward(100)
left(72)
forward(100)
left(72)
forward(100)
left(72)
forward(100)
mainloop()