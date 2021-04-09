my_list = [1, 3, 6, 10]

#generator expression
a = (x**2 for x in my_list)
print(next(a))

print(next(a))

print(next(a))

print(next(a))


#Generator expressions can be used as function arguments. When used in such a way, the round parentheses can be dropped.

print(sum(x**2 for x in my_list))
