#check if the given two digit number is greater than 25 and its first digit is greater than its second digit.

a = input()
b = int(a)
num = b>25
c = int(a[0])>int(a[1])
print(num and c)
