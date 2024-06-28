# bài 1
# a = input("Username: ")
# b = int(input("Password: "))
# c = input("Email: ")
# print(f"""== Registration ==
# Username: {a}
# Password: {b}
# Email: {c}
# Registered successfully.
#       """)

# bài 2
a = input("Username: ")
b = int(input("Password: "))
c = int(input("Repeat password: "))
d = input("Email: ")
while b==c:
    if b==c:
        print(f"""== Registration ==
        Username: {a}
        Password: {b}
        Email: {d}
        Registered successfully.
          """
          )
else:
    print("Passwords not match. Please input again. ")
    c = int(input("Repeat password: "))

