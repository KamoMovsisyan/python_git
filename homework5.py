#1
height = int(input("Enter the height of your triangle in cm's: "))
base = int(input("Enter the base of triangle in cm's: "))
def area_of_triangle(height_ : int, base_ : int) -> float:
    '''
    the function takes two arguments (height and base) and returns us the area of a triangle

    Parameters:
        height_ (int): the height of triangle 
        base_ (int): the base of triangle

    Returns:
        the area of triangle
    '''
    area = height_ * base_ / 2
    return f'The area of your triangle is {area}'

print(area_of_triangle(height, base))

#2
word = input('Enter your word ang get it reversed: ')
def reverse_(word_ : int) -> int:
    '''
    enter word and see how it will be reversed
    Parameters:
        word_ (int): the word you want to reverse
    Returns:
        the word reversed
    '''
    new_word = word_[::-1]
    return new_word

print(reverse_(word))

#3
word = input('Enter your text: ')
def upper_and_lower(word_ : str) -> str:
    '''
    You are giving a text and get the number of lower case and upper case letters

    Parameters:
        the word which letters you want to count
    
    Returns:
        number of upper and lower case letters
    '''
    count_1 = 0
    count_2 = 0
    word_ = word
    for i in word_:
        if i.isupper():
            count_1 += 1
        elif i.islower():
            count_2 += 1
        else:
            continue
    return f'you have {count_1} upper case letters and {count_2} lower case letters'

print(upper_and_lower(word))

#4
word = input('Enter your word here and check if it is palindrome or not: ')
def is_palindrome(word_ : str) -> str:
    '''
    check if the word is palindrome or not

    Parameters:
        word_ (str): the word you want to check
    Returns:
        True if the word is palindrome,False if it is not palindrome
    '''
    new_word = word_[::-1]
    if new_word == word_ :
        return True
    else:
        return False

print(is_palindrome(word))

#5
import random
user_choice = int(input('Choose one, 1: Rock, 2:Paper, 3:Scissors : '))
computer_choice = random.randint(1,3)
if user_choice == 1 and computer_choice == 1:
    print('No one win,you both choose the same')
elif user_choice == 1 and computer_choice == 2:
    print(f'Computer win, you choose {user_choice}, he choose {computer_choice}')
elif user_choice == 1 and computer_choice == 3:
    print(f'You win, you choose {user_choice}, he choose {computer_choice}')
elif user_choice == 2 and computer_choice == 1:
    print(f'You win, you choose {user_choice}, he choose {computer_choice}')
elif user_choice == 2 and computer_choice == 2:
    print('No one win,you both choose the same')
elif user_choice == 2 and computer_choice == 3:
    print(f'Computer win, you choose {user_choice}, he choose {computer_choice}')
elif user_choice == 3 and computer_choice == 1:
    print(f'Computer win, you choose {user_choice}, he choose {computer_choice}')
elif user_choice == 3 and computer_choice == 2:
    print(f'You win, you choose {user_choice}, he choose {computer_choice}')
elif user_choice == 3 and computer_choice == 3:
    print('No one win,you both choose the same')
else:
    print('Wrong values')