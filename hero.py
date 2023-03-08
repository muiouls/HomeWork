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
               f'i' \
               f'I am {self.superpower}\n' \
               f'My health_points is {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

Hero = SuperHero('Clark Kent', 'SuperHero','capable of moving giant objects and delivering blows of incredible power', 100,  "You guys haven't learned anything yet. Do you really think bullets can stop me?")
print(Hero.get_name())
Hero.double_health()
print(Hero)
print(len(Hero))


