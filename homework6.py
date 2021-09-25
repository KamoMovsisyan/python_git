#1
#1.1
my_list = [1,1,5]
def remove_duplicates(your_list : list) -> list:
    for i in your_list:
        for j in your_list:
            if i == j:
                your_list.remove(i)
                your_list.remove(j)
    return your_list
print(remove_duplicates(my_list))


#1.2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    if i in b:
        c.append(i)

new_list = []

for j in c:
    if j not in new_list:
        new_list.append(j)     

print(new_list)

#2

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
def divisers_of_5(your_list : list) -> list:
    '''
    takes a list and print out all the numbers which are divisers of 5
    '''
    for i in your_list:
        if i % 5 == 0:
            new_list.append(i)
    return new_list

print(divisers_of_5(a))

#3

text_1 = input('Enter your text here: ')
def revers_text(your_text : str) -> str:
    '''
    takes a string and returns the string reversed
    '''
    text_2 = your_text.split()
    text_3 = text_2[::-1]
    return ' '.join(text_3)

print(revers_text(text_1))

#4
my_tuple = (1,True,321,'text',12)
def reversed_tuple(your_tuple : tuple) -> tuple:
    '''
    takes a tuple as argument and returns it reversed
    '''
    new_tuple = your_tuple[::-1]
    return new_tuple
print(reversed_tuple(my_tuple))

#5
my_list = [1,42,2,421,7,3]
new_list = []
def list_sort(your_list : list) -> list:
    for i in range(len(your_list)):
        minimum_number = your_list[0]
        for j in your_list:
            if j < minimum_number:
                minimum_number = j
        new_list.append(minimum_number)
        your_list.remove(minimum_number)
    return new_list

print(list_sort(my_list))

#6
my_list = [1,42,2,421,7,3]
new_list = []
def list_sort(your_list : list) -> list:
    for i in range(len(your_list)):
        minimum_number = your_list[0]
        for j in your_list:
            if j < minimum_number:
                minimum_number = j
        new_list.append(minimum_number)
        your_list.remove(minimum_number)
    return new_list[-2] # sortingic heto veradardznuma naxaverjin tivy, aysinqn erkrord amenamec tivy

print(list_sort(my_list))

#6.2
my_list = [1,42,2,421,7,3]
maximum_1 = max(my_list)
my_list.remove(maximum_1)
maximum_2 = max(my_list)
print(maximum_2)