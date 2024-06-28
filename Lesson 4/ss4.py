# for: vòng lặp for dùng để thực hiện một việc gì đó lặp đi lặp lại nhiều lần với số lần biết trước
# ví dụ về vòng lặp for: bài toán in ra các số từ 1-10
# for i in range(1, 11, 1):
#     print(i)
# for i in range(11):
#     print(i)

# while: vòng lặp while dùng để thực hiện một việc gì đó lặp đi lặp lại nhiều lần với số lần không biết trước
# while <expression>:
# ví dụ về vòng lặp while: bài toán in ra các số từ 0-10
# i = 0
# while i<11:
#     print(i)
#     i = i + 1

# n = 1
# while n<5:
#     print("Hi")
#     n += 1


# bài 1
# for i in range(7):
#     print(i)
# for i in range(100, 106, 1):
#     print(i)
# for i in range(2, 10, 1):
#     print(i)
# n=9 
# while n>1:
#     print(n)
#     n -= 1

# bài 2
# for i in range(21):
#     if i%3==0:
#         print(i)

# bài 3
# a = 0
# n = int(input("nhập số n: "))
# while a<n+1:
#     print(a)
#     a=a+1

#bài 4
# n = int(input("nhập số n: "))
# scs = 0
# while n>0: 
#     n = n//10
#     scs += 1
# print(scs)

# bài 6
# n = int(input("nhập số n: "))
# if n%1==0 and n%n==0 and n%2!=0 or n%3!=0:
#     print("true")
# else:
#     print("false")

# n = int(input("nhập số n: "))
# dem = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         dem += 1
# if dem ==2:
#     print(f"{n}" là số nguyên tố)
# else:
#        print(f"{n}" là không số nguyên tố)

# bài 5
# n = int(input("nhập số n: "))
# gt = 1
# for i in range(1,n+1):
#     gt = gt*i
# print(gt)