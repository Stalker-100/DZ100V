spisokKino = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
joinKino = []

vvod = input("Введите любимый фильм: ")

if vvod in spisokKino:
    joinKino.append(vvod)
    print(f"Ваш любимый фильм! {vvod}")
else:
    print("Неверный фильм")