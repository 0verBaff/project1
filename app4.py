cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
     {'name': 'Мария', 'age': 22},
     {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
      {'user': users[1], 'city': cities[0]},
      {'user': users[2], 'city': cities[1]}]

city = input('Введите город: ')


if city.lower() == tourists[0]['city'].lower():

  print(f"Турист {tourists[0]['user']['name']} возраст {tourists[0]['user']['age']}. Посетил город {city}")
elif city.lower() == tourists[1]['city'].lower():
  print(f"Турист {tourists[1]['user']['name']} возраст {tourists[1]['user']['age']}. Посетил город {city}")
elif city.lower() == tourists[2]['city'].lower():
  print(f"Турист {tourists[2]['user']['name']} возраст {tourists[2]['user']['age']}. Посетил город {city}")
else: 
  print('Такого города нет в списке')