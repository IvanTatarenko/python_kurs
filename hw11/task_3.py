class Currency:
    def __init__(self, uah, usd, eur, pln):
        self.uah = uah
        self.usd = usd
        self.eur = eur
        self.pln = pln   
     
    def summary(self):
        return f'UAH: {self.uah} USD: {self.usd} EUR: {self.eur} PLN: {self.pln}'
        
    def eqvival(self, rate):
        if rate == 'USD':
            return f'UAH: {self.uah / 26} USD: {self.usd} EUR: {self.eur  / 29} PLN: {self.pln / 5.5}'
        elif rate == 'EUR':
            return f'UAH: {self.uah / 29} USD: {self.usd * 0.88} EUR: {self.eur} PLN: {self.pln * 0.17}'
        elif rate == 'PLN':
            return f'UAH: {self.uah / 5.5} USD: {self.usd * 0.18} EUR: {self.eur  / 5.83} PLN: {self.pln}'
        elif rate == 'UAH':
            return f'UAH: {self.uah} USD: {self.usd * 0.038} EUR: {self.eur / 32.6} PLN: {self.pln / 0.09}'    
    
    def __eq__(self, other):
        if self.uah == other.uah and self.usd == other.usd and self.eur == other.eur and self.pln == other.pln:
            return True
        else:
            return False
            
    def __add__(self, other):
        self.uah += other.uah
        self.usd += other.usd
        self.eur += other.eur
        self.pln += other.pln
        return f'UAH: {self.uah} USD: {self.usd} EUR: {self.eur} PLN: {self.pln}'



my_saving = Currency(33, 100, 200, 100)
your_saving = Currency(34, 100, 200, 100)
print(my_saving.summary())
print(my_saving.uah)
print(my_saving.eqvival("UAH"))
print(my_saving == your_saving)
print(my_saving + your_saving)