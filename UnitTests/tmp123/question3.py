n = input("number input: ")
n = int(n)
def integral1(n):
    dict1 = {}
    for i in range(1,n+1):
        dict1[i] = i*i
    return dict1

print(integral1(n))

# {x:y for x in range(1,n+1):
x = n
print({x:x*x for x in range(1,x+1)})
