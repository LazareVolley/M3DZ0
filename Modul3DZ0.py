Задача №1. Описание Домашних животных

struct Animal:
    name: str,
    type: str,
    age: int,
    weight: float,
    vaccination: bool

Например:

Parrot = Animal("Kesha", "bird", 5, 1.2, True)
Dolphin = Animal("", "fish", 24 ,243.11, False)
Makaka = Animal("ChiChiChi", "Monkey", 10, 28.7, True)
Gaduka = Animal("Djafar", "Snake", 1, 4.97, False)

Задача №2. "Ритуалы и традиции в волшебном обществе"

struct Artefact:
    stuff: str, #материал, из которого изготовлен артефакт
    historical_meaning: str, #историческое значение артефакта
    streight: float #сила артефакта

struct Ritual_date:
    day: int, #день, в который проходит ритуал
    mounth: int, #месяц, в который проходит ритуал
    year: int #год, в который проходит ритуал

struct Villager:
    role: str, #роль члена общества
    cloth:, str, #одежда члена общества
    social_class: str, #общественный слой члена общества
    artifact: struct #артефакт, принадлежащий члену общества

struct Main_villagers:
    name: str #имя ключевой сущности / члена общества

1. Определить ключевые сущности в ритуалах и традициях этого волшебного общества:

Villager1 = Main_villagers("Dmitriy_Rak")
Villager2 = Main_villagers("Jurabek")
Villager3 = Main_villagers("Nedoprogrammist")

2. Ключевые сущности волшебного мира:

Villager1 = Villager("Имеет высший авторитет и является духовным лидером общества, принимает важные решения и решает споры между членами общества", "Темный костюм с накидкой из синего бархата", "Magic_Ministr", Книга заклинаний)
Villager2 = Villager("Отвечает за проведение магических ритуалов и церемоний, обладает обширным знанием о мистических силами", "Длинный плащ из черного бархата", "Magic_Senior", Планшет всесилия)
Villager3 = Villager("Обеспечивает руководство и стратегическое направление для всего общества", "Костюм из золотистого шелка", "Caster", Прямая рука)

3. Анализ, как сущности взаимодействуют друг с другом во время ритуалов:

Во время ритуалов сущность 'Nedoprogrammist' тратит всю энергию (или её часть) на изучение нового материала, сущность 'Jurabek' помогает сущности 'Nedoprogrammist' кастуя баффы при помощи Artefact('Планшет всесилия'). Сущность 'Dmitriy_Rak' регулирует весь процесс, направляя отряд при помоищи Artefact('Книга заклинаний').

*Сущность 'Nedoprogrammist' может использовать Artefact('Прямая рука') только один раз за ритуал. Результатом действия Artefact('Прямая рука') для сущности 'Nedoprogrammist' является: Ускорение обучения и применения навыков. Длительность: 30 минут.

Задача №3. "Городской фермерский рынок"

struct Stand:
    product_type: str

struct Farmer:
    name: str,
    age: int,
    products_range: list

struct Item:
    name: str,
    count: int,
    manufacturing_date: struct

struct shopper:
    name: str,
    age: int,
    demography: str,
    product_preferences: list[str],
    cash_amount: int

