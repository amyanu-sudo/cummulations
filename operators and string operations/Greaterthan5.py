#check if both of the given numbers are positive and if atleast one of them is greater than 5

a = int(input())
b = int(input())
if(a>0 & b>0 & (a>5 || b>5)):
    print(True)
else:
    print(False)
