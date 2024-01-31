name, age, city = input(), int(input()), input()
print("Меня зовут %s. Мне %d года. Я живу в городе %s." % (name, age, city))
print("Меня зовут {name}. Мне {age} года. Я живу в городе {city}.".format(name = name, age = age, city = city))
print(f"Меня зовут {name}. Мне {age} года. Я живу в городе {city}.")