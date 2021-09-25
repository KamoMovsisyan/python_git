#1
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
dict4={6:50,7:60}
list_dict = [dict1, dict2, dict3, dict4]

new_dict = dict()

for i in list_dict:
    new_dict.update(i)
print(new_dict)

#2
my_dict = dict()
n = int(input('Enter the range: '))
for i in range(1,n+1): 
    my_dict[i] = i*i
print(my_dict)

#3
my_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}
new_dict = dict()
for (key, value) in my_dict.items():
     if value != None:
         new_dict[key] = value

print(new_dict)

#4
your_text = input('Enter your text here: ')

def count_words(text_example : str) -> str:

    my_dict = dict()
    new_list = text_example.split()
    for i in new_list:
        my_dict[i] = new_list.count(i)

    return my_dict

print(count_words(your_text))