list = []
for num in range(2000,3201):
    if num%13 ==  0 and num%5 != 0:
        list.append(str(num))
        # list = list + str(num) + ","
# print(list)
print(", ".join(list))

out1 = [str(i) for i in range(2000,3201)  if i%13 ==  0 and i%5 != 0]

# print(out1)
print(", ".join(out1))

user = ('hentam', 'hkgfDHLFGDF')
print(user[1])