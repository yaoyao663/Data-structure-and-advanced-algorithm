def IntegerMirror(num):
    newnum = 0
    while num > 0:
        digit = num % 10
        newnum = newnum * 10 + digit
        num = num // 10
    return newnum
a = int(input())
newnum = IntegerMirror(a)
print(newnum)

'''
1. Arithmetic operations for d-digit number is 4d, where d is the number of digits in the input number.
2. The time complexity in terms of input n is O(log n) since d ≈ log₁₀ n
'''