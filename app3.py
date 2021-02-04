account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

user_list = [user1, user2, user3, user4]

key_input = input('Введите ключ (name или account): ')  
key = key_input.lower()  

try:
    circle_i = 1
    for i in user_list:
        print(f'значение ключа для user{circle_i} = {i[key]}')
        circle_i +=1
except KeyError:
    print('Введенный ключ не найден')
    
print(' ') 

user_number = input('Введите порядковый номер: ') 

try:
     user_list[(int(user_number)-1)] 
     print(f'Данные по user{user_number}:')
     print(f'имя: {user_list[(int(user_number)-1)]["name"]}')
     print(f'возраст: {user_list[(int(user_number)-1)]["age"]}')
     print(f"логин: {user_list[(int(user_number)-1)]['account']['login']}")
     print(f"пароль: {user_list[(int(user_number)-1)]['account']['password']}")     
except IndexError:
    print('Пользователь с указанным номером не найден')

print(' ') 


user_move = input('Введите номер пользователя для переноса в конец списка: ') 

try:
    user_list[(int(user_move)-1)] 
    print('Список до изменения') 
    print(user_list)
    print(' ') 
    print(f'Пользователь с именем {user_list[(int(user_move)-1)]["name"]} перемещен в конец списка')
    print(' ') 
    user_to_end = user_list.pop((int(user_move)-1)) 
    user_list.append(user_to_end) 
    print('Список после изменения') 
    print(user_list)
    print(' ') 
except IndexError:
    print('Пользователь с указанным номером не найден')

middle_age = 0 
for j in user_list: 
    middle_age += int(j['age'])

print(f'Средний возраст пользователей: {middle_age/len(user_list)}')