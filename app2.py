
check = 1
in_pass = input('Введите пароль:')
quanty = len(in_pass)


try:    
    passw = check/quanty
    passw2 = int(in_pass)
    print('Ваш пароль состоит только из цифр')
except ZeroDivisionError:
    print('Вы нечего не ввели')
except ValueError:
    print('В пароле содержаться буквы')