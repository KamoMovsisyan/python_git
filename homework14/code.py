import os

print(os.getcwd())
os.chdir(f'{os.getcwd()}/homework14')

question = input('Do you want to delete folders (y - yes,n- no): ')

if question == 'n':
    pass
elif question == 'y':
    os.rmdir(f'{os.getcwd()}/dir1/dir3/dir4')

    os.chdir(f'{os.getcwd()}/dir1/dir3')

    for path in os.listdir():
        if os.listdir():
            os.remove(path)   

    os.chdir('../..')
    os.rmdir(f'{os.getcwd()}/dir1/dir3')
    os.rmdir(f'{os.getcwd()}/dir1/dir2')

    os.chdir(f'{os.getcwd()}/dir1')

    for path in os.listdir():
        if os.listdir():
            os.remove(path) 
    os.chdir('../')
    os.rmdir(f'{os.getcwd()}/dir1')
else:
    print('Wrong input!!')