#For this problem, the prefilled code will contain a list of tuples. Write a program to replace the last number of each tuple in the list with the given number.

num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
n = int(input())
new_list = []
for each_tuple in num_list:
    updated_tuple = each_tuple[:-1] + (n,)
    new_list.append(updated_tuple)
print(new_list)
    
