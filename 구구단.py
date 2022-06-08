# for x in range(2, 10):
#     print("{0} 단".format(x))
#     for y in range(1, 10):
#         print(x, "X", y, "=", x*y)

for num in range(2, 10):
    print("{0} 단".format(num))
    y = 1
    while y < 10:
        print(num, "X", y, "=", num*y)
        y += 1
