n = "vadim shavlovskiy"

print("Hello world")

print(n.title())
print(n.upper())
x = 1  # Добавил эту строку чтобы не ругался что x не определено типа
for x in range(0, 25):
    print(x)
print(n.lower())
while True:
    x = x+1
    print(x)
    if x == 47:
        break

cities = ['Minsk', 'Москва', 'London', 'Париж', 'Berlin', 'Madrid', 'Варшава', 'Берлин', 'Милан', 'Рим', 'Лондон',
          'Стамбул']

print(cities)
print("________________________________________________________________")
cities.remove('Москва')
print(cities)
print("________________________________________________________________")
print("Последний город в списке удален - это город: ", cities.pop())
print("Новый список городов: ", cities)
print("________________________________________________________________")
