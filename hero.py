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
        self.health_points **= 2
        self.fly = True

    def fly_phrase(self):
        if self.fly:
            return "I'm flying!"
        else:
            return "I'm not flying."

class EarthHero(SuperHero):
    people = 'earth'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def fly_phrase(self):
        if self.fly:
            return "I'm flying!"
        else:
            return "I'm not flying."

class Villain(AirHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self, damage):
        return damage ** 2

air = AirHero('Peter Parker', 'AirHero', 'able to fly and shoot webs', 100, "With great power comes great responsibility", 20)
print(air.get_name())
air.double_health()
print(air)
air.fly_phrase()

earth = EarthHero('Bruce Banner', 'EarthHero', 'turns into a green monster', 200, "You wouldn't like me when I'm angry", 20)
print(earth.get_name())
earth.double_health()
print(earth)
earth.fly_phrase()

villain = Villain('Tom Hardy', 'Venom', 'alien symbiote with spider-like powers', 150, 'We are Venom!', 25)
print(villain.get_name())
villain.double_health()
print(villain)
villain.fly_phrase()

damage = 5
print(f"Damage: {damage}")
print(f"Crit damage: {villain.crit(damage)}")




# Hero = SuperHero('Clark Kent', 'SuperHero','capable of moving giant objects and delivering blows of incredible power', 100,  "You guys haven't learned anything yet. Do you really think bullets can stop me?")
# print(Hero.get_name())
# Hero.double_health()
# print(Hero)
# print(len(Hero))


