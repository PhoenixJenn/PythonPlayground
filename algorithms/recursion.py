#recursion will be in here

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print("Enter a number")
y = input()
result = fact(int(y))
print(result)
