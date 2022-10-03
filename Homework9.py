import re

reg = re.compile(r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}(?P<reg>\d{2,3})$')
car_id = input("Введите номер").

match = reg.match(car_id)
if match:
    print(f"Результат: Номер {car_id} валиден. Регион: {match['reg']}")
else:
    print(f"Результат: Номер {car_id} не валиден")
