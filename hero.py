class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return (f'My name is {self.name}')

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f'My nickname is {self.nickname}\n' \
               f'I am {self.superpower}\n' \
               f'My health_points is {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)
class AirHero(SuperHero):
    people = 'air'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.fly = True
        return f"double health: {self.health_points ** 2}"

    def fly_phrase(self):
        print(f'fly in the {self.fly}_phrase')


class EarthHero(SuperHero):
    people = 'earth'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage= False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.fly = True
        return f"double health: {self.health_points ** 2}"

    def fly_phrase(self):
        print(f'fly in the {self.fly}_phrase')

class Villain(AirHero):
    SuperHero.people = 'monster'

    def gen_x(self):
        pass

    def crit(self, hero):
        return f"damage of EarthHero: {hero.damage ** 2}"


air = AirHero('Peter Parker', 'AirHero', 'able to fly and shoot webs', 100, "With great power comes great responsibility", 20)
print(air.get_name())
print(air.double_health())
print(air)
air.fly_phrase()

earth = EarthHero('Bruce Banner', 'EarthHero', 'turns into a green monster', 200, "You wouldn't like me when I'm angry", 20)
print(earth.get_name())
print(earth.double_health())
print(earth)
earth.fly_phrase()

villain1 = Villain('Tom Hardy', 'Venom', 'alien symbiote with spider-like powers', 150, 'We are Venom!', 25)
print(villain1.get_name())
villain1.double_health()
print(villain1)
villain1.fly_phrase()

print(Villain.crit(villain1, earth))



# Hero = SuperHero('Clark Kent', 'SuperHero','capable of moving giant objects and delivering blows of incredible power', 100,  "You guys haven't learned anything yet. Do you really think bullets can stop me?")
# print(Hero.get_name())
# Hero.double_health()
# print(Hero)
# print(len(Hero))

