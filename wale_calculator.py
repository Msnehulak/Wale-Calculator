from datetime import date

class whalecalculator:
    def __init__(self):
        self.total = 0
        self.prices = {
            "welkin": 4.99,
            "battle_pass": 9.99,
            "crystal": [
                [60, 0.99],
                [300, 4.99],
                [980, 14.99],
                [1980, 29.99],
                [3280, 49.99],
                [6480, 99.99]
            ]
        }

            # Date
        self.releasedate = date(2020, 9, 28)
        self.todaydate = date.today()
        self.daysfromreleas = self.todaydate - self.releasedate
        self.daysfromreleas = self.daysfromreleas.days
        self.versincrelease = self.daysfromreleas // (7 * 6) 

            # Welkin Moon
        self.welkinowned = self.daysfromreleas // 30
        self.spendwelkin = self.welkinowned * self.prices["welkin"]
        self.total += self.spendwelkin

            # Batle pass
        self.batlepassownd = self.versincrelease
        self.spendbp = self.batlepassownd * self.prices["battle_pass"]
        
        self.promobplv = 150
        self.bpleve = self.primo_to_usd(self.promobplv)
        self.maxlvbp = self.bpleve * 50
        self.spendbplv = self.maxlvbp * self.batlepassownd 

        self.total += self.spendbp + self.spendbplv

            # characters
        self.total5char = 65 
        self.standart5char = 8
        self.limited5char = self.total5char - self.standart5char 
        
        self.pulls1copy = 90 * 2
        self.pullsC6 = self.pulls1copy * 7
        self.priceC6 = self.primo_to_usd(self.pullsC6)
        self.spendallchar = self.priceC6 * self.limited5char

        self.total += self.spendallchar

    def primo_to_usd(self, primo):
        bundles = self.prices["crystal"]

        costs_per_crystal = []
        for crys, price in bundles:
            costs_per_crystal.append(price / crys)
        
        average_cost_per_crystal = sum(costs_per_crystal) / len(costs_per_crystal)
        
        return round(primo * average_cost_per_crystal, 2)

    def main(self):
        print(f"""
Welkin Moon
ownd                {self.welkinowned}
spend               {self.spendwelkin:.2f} usd

Battle Pass
ownd                {self.batlepassownd}
spend on bp         {self.spendbp:.2f} usd
spend on levls      {self.spendbplv:.2f} usd

Characters
1 copy              {self.pulls1copy} usd
C6                  {self.pullsC6} usd
spend               {self.spendallchar:.2f} usd

total               {self.total:.2f} usd
""")

if __name__ == "__main__":    
    wc = whalecalculator()
    wc.main()