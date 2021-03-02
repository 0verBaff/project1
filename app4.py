# Данные к задаче
cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
     {'name': 'Мария', 'age': 22},
     {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
      {'user': users[1], 'city': cities[0]},
      {'user': users[2], 'city': cities[1]}]

city = input('Введите город: ')

# Решение
# Поскольку мы работаем со строками, то сравнение строк будем выполнять в нижнем регистре.
# Введенное значение city преобразовываем к нижнему регистру методом lower().
# Выполняем проверку на равенство city и каждого элемента из списка tourists.
# Элемент списка tourists тоже переводим в нижний регистр:
#   tourists[0]         - получаем значение по индексу 0 из списка tourists т.е. первый элемент списка
#   tourists[0]['city']     - получаем значение ключа 'city'
#   tourists[0]['city'].lower() - преобразовываем в нижний регистр
if city.lower() == tourists[0]['city'].lower():
  # Если значение ключа 'city' для элемент списка tourists равен city, 
  # то выводим значения по ключам:
  #   tourists[0]         - элемент списка tourists
  #   tourists[0]['user']     - это словарь т.к. значение ключа 'user' - это элемент из списка словарей users
  #   tourists[0]['user']['name'] - значение ключа 'name'
  #   tourists[0]['user']['age'] - значение ключа 'age'
  print(f"Турист {tourists[0]['user']['name']} возраст {tourists[0]['user']['age']}. Посетил город {city}")
elif city.lower() == tourists[1]['city'].lower():
  print(f"Турист {tourists[1]['user']['name']} возраст {tourists[1]['user']['age']}. Посетил город {city}")
elif city.lower() == tourists[2]['city'].lower():
  print(f"Турист {tourists[2]['user']['name']} возраст {tourists[2]['user']['age']}. Посетил город {city}")
else: 
  print('Такого города нет в списке')