def checking(str):  # Email checking

    x = 0
    for ch in str:
        if ch == '@':
            x = x + 1
        if ch== '.':
            x = x + 1

    if x == 2:
        return True
    else:
        return False

mail = input('Mail : ')

if (checking(mail) == True):
    print('It is an email adress')
else:
    print('It is not an email adress')