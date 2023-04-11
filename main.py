def q1():
    import random
    a = [random.randint(1, 10) for i in range(5)]
    b = int(input('Введите число:'))
    if b in a:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")
    print('Были загаданы числа:', *a)

def q2():
    import random
    n = [random.randint(1, 10) for i in range(10)]
    m = [i for i in set(n) if n.count(i) > 1]
    if len(m) == 0:
        print("Повторяющихся элементов нет")
    else:
        print(*n)
        print(*m)

def q3():
    d = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
    a = int(input('кол-во выходных: '))
    q = d[:-a]
    w = d[:-a - 1:-1]
    if 1 < a < 7:
        print('выходные дни:', *w)
        print('рабочие дни:', *q)

def q4():
    import random
    my = ['Гусева', 'Голикова', 'Пахомов', 'Зверева', 'Никифоров', 'Морозов', 'Пименов', 'Юдина', 'Шмелева', 'Золотарев']
    other = ['Казакова', 'Кузнецов', 'Семенов', 'Морозов', 'Быкова', 'Васильева', 'Кузьмина', 'Ершова', 'Ильинская', 'Покровский']
    team = tuple(random.sample(my, 5) + random.sample(other, 5))
    print('1ая:', *my)
    print('2ая:', *other)
    print('солянка:', *team)
    print('длина:', len(team))
    team = tuple(sorted(team))
    if 'Иванов' in team:
        print(team.count('Иванов'))
    else:
        print('Иванова не существует')

q1()