shoppingList = ["snack", "fish", "đậu"]
# print(len(shoppingList;))
# print(shoppingList[0])

# shoppingList.append("banana")
# print(shoppingList)

# shoppingList.remove("snack")
# print(shoppingList)

# print("đậu" in shoppingList)


#### duyệt danh sách với vòng lặp:
# for item in shoppingList:
#     print(item)

## in ra toàn bộ list, tuy nhiên item/ đại diện cho vị trí phần tử trong list
# for i in range(len(shoppingList)):
    # print(i)
# a=[1,2,3]
# b=a.copy()
# print(a)


# a=[1,2,3]
# b=[4,5,6]
# # print(a+b)#cách 1
# b.extend(a)
# print(b)#cách 2

###### khai báo 1 turple
# const1 = (3.14, "123")
# print(3.14 in const1)

#bai 1 + 2
# food = ["ga", "bo", "chao"]
# a = input("ban thich an gi: ")
# food.append(a)
# for i in food:
#     print(i)

# b = input("ban muon bo mon nao:")
# food.remove(b)
# print(food)

#bai 3
c = [1, 2, -3, 4, 5]
tong = 0
for i in c:
    tong += i
print(tong)