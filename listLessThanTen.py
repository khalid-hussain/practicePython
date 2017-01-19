a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

# CASE 1
# for element in a:
#     if element < 5:
#         print(element)

# CASE 2
# for element in a:
#     if element < 5:
#         b.append(element)

# for element in b:
#     print(element)

# CASE 3
b = [x for x in a if x < 5]
print(b)
