# Password generator
import random
def password_genetator():
    password = []
    while len(password) <= 8:
        order = random.randint(65,90)
        letter = chr(order)
        password.append(letter)
    password = ''.join(password)
    return password

print(password_genetator())

# Even Num Generator
from random import randint

start_ = int(input('Please enter the start number : '))
stop_ = int(input('Please enter the stop number : '))

def even_num_generator(start,stop):
    for i in range(start,stop):
        i = randint(start,stop)
        i = i if i % 2 == 0 else i + 1
        yield i  

random_ = even_num_generator(start_,stop_)

print(next(random_))