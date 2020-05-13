class Animals:

  def __init__(self, name, weight, voice):
    self.name = name
    self.weight = weight
    self.voice = voice
    self.action = None


  def feed(self):
    self.action = 'кормить'

class Cow(Animals):
    def milk(self):
      self.action = 'доить'

class Goat(Cow):
    pass

class Sheep(Animals):
    def cut(self):
      self.action = 'стричь'

class Chicken(Animals):
    def eggs(self):
      self.action = 'собирать яйца'

class Gose(Chicken):
    pass

class Duck(Chicken):
    pass

cow = Cow(name='Манька', weight=300, voice='Му')
goat1 = Goat(name='Рога', weight=30, voice='Ме')
goat2 = Goat(name='Копыта', weight=34, voice='Ме')
sheep1 = Sheep(name='Барашек', weight=50, voice='Бе')
sheep2 = Sheep(name='Кудрявый', weight=52, voice='Бе')
сhicken1 = Chicken(name='Ко-Ко', weight=3, voice='Коко')
сhicken2 = Chicken(name='Кукареку', weight=4, voice='Коко')
duck = Duck(name='Кряква', weight=5, voice='Кря')
gose1 = Gose(name='Серый', weight=10, voice='Га')
gose2 = Gose(name='Серый', weight=12, voice='Га')

gose1.eggs()
print(gose1.action)

cow.feed()
print(cow.action)

goat2.milk()
print(goat2.action)

sheep2.cut()
print(sheep2.action)

# animals = [cow, goat1, goat2, sheep1, sheep2, сhicken1, сhicken2, duck, gose1, gose2]

# cows = [cow]
# goats = [goat1, goat2]
# sheeps = [sheep1, sheep2]
# сhickens = [сhicken1, сhicken2]
# ducks = [duck]
# goses = [gose1, gose2]


print(f'Вес коров - {cow.weight} кг')
print('Вес коз -', goat1.weight+goat2.weight, 'кг')
print('Вес баранов -', sheep1.weight+sheep2.weight, 'кг')
print('Вес куриц -', сhicken1.weight+сhicken2.weight, 'кг')
print(f'Вес уток - {duck.weight} кг')
print('Вес гусей -', gose1.weight+gose2.weight, 'кг')

animal_max_weight = (max(cow.weight, goat1.weight, goat2.weight,sheep1.weight, sheep2.weight, сhicken1.weight, сhicken1.weight, duck.weight, gose1.weight, gose2.weight))
if animal_max_weight == 300:
    print(cow.name)
elif animal_max_weight == 30:
    print(goat1.name)
elif animal_max_weight == 34:
    print(goat2.name)
elif animal_max_weight == 50:
    print(sheep1.name)
elif animal_max_weight == 52:
    print(sheep2.name)
elif animal_max_weight == 3:
    print(сhicken1.name)
elif animal_max_weight == 4:
    print(сhicken2.name)
elif animal_max_weight == 5:
    print(duck.name)    
elif animal_max_weight == 10:
    print(gose1.name)
elif animal_max_weight == 12:
    print(gose2.name)

  