import random

class Fighter():
  def __init__(self, style, nickname):
    self.style = style
    self.nickname = nickname
    self.record = {'wins': 0, 'losses': 0, 'draws': 0}

  def win(self):
    self.record['wins'] += 1

  def lose(self):
    self.record['losses'] += 1

  def draw(self):
    self.record['draws'] += 1
    
  def __repr__(self):
    record = f"{self.record['wins']}-{self.record['losses']}-{self.record['draws']}"
    return f"{self.nickname} ({self.style}): {record}"

class Boxer(Fighter):
  def __init__(self):
    self.age = random.randint(20, 40)
    self.height = random.randint(160, 200)
    self.weight = random.randint(60, 100)
    self.record = {"wins": random.randint(0, 100), "losses": random.randint(0, 10)}
    self.nickname = random.choice(["Флойд Майвезер", "Кличко1", "Майк Тайсон", "Мухамед Алі", "Кличко2",]) + ' ' + random.choice(["Лютий", "Дикий", "Хоробрий", "Безстрашний", "Могутній" ]) + ' ' + random.choice(["Лев", "Тигр", "Ведмідь", "Лев", "Акула",]) 
       
boxers = []
for i in range(5):
  boxer = Boxer()
  boxers.append(boxer)
  print(f"{boxer.nickname} ({boxer.age} років, {boxer.height} см, {boxer.weight} кг) - {boxer.record['wins']} перемог, {boxer.record['losses']} поразок")