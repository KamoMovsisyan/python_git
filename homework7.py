#2
list_example = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
new_list = []
for i in list_example:
    if i not in new_list:
        new_list.append(i)
print(new_list)

#3
my_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
new_list = []
for i in my_list:
    if type(i) == list:
        for j in i:
            new_list.append(j)
    else:
        new_list.append(i)
print(new_list)

#4
my_list = [1, 1, 2, 3, 4, 4, 5, 1]
new_list_1 = []
new_list_2 = []
list_length = int(input('Length of the first part of the list: '))

for i in my_list:
    if len(new_list_1) < list_length:
        new_list_1.append(i)
    else:
        new_list_2.append(i)

print(new_list_1,new_list_2,sep='\n')