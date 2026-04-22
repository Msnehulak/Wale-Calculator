from datetime import date
import requests

class whalecalculator:
    def __init__(self):
        self.standart5char = ["Jean", "Diluc", "Qiqi", "Mona", "Keqing", "Tighnari", "Dehya", "Mizuki"]
        self.limited5char = self.get_limited_character_count()
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
        self.primo = {
            "bplvup": 150,
            "refil rezin": 50,
            "pull": 160
        }
        self.total_spend = 0
            # Date
        self.release_date = date(2020, 9, 28)
        self.today_date = date.today()
        self.days_from_releas = self.today_date - self.release_date
        self.days_from_releas = self.days_from_releas.days
        self.versin_released = self.days_from_releas // (7 * 6) 

        self.Welkin_Moon()
        self.Batle_pass()
        self.Batle_pass_levl_up()
        self.Daly_resin_refill()
        
    def Welkin_Moon(self):
        self.welkin_moon_owned = self.days_from_releas // 30 
        self.welkin_moon_spend = self.welkin_moon_owned * self.prices["welkin"]
        
        self.total_spend += self.welkin_moon_spend

    def Batle_pass(self):
        self.BP_owned = self.versin_released
        self.BP_spend = self.BP_owned * self.prices["battle_pass"]
        
        self.total_spend += self.BP_spend

    def Batle_pass_levl_up(self):
        self.BP_LV_UP_count = self.BP_owned * 50
        self.BP_LV_UP_spend_primo = self.BP_LV_UP_count * self.primo["bplvup"]
        self.BP_LV_UP_spend = self.primo_to_usd(self.BP_LV_UP_spend_primo)

        self.total_spend += self.BP_LV_UP_spend 

    def Daly_resin_refill(self):
        self.resin_refill_limit = 5
        self.resin_refil_spend_primo = self.resin_refill_limit * self.days_from_releas
        self.resin_refil_spend = self.primo_to_usd(self.resin_refil_spend_primo)

        self.total_spend += self.resin_refil_spend

    def get_limited_character_count(self):
            # requests
        url = "https://genshin-db-api.vercel.app/api/characters?query=5&matchCategories=true"
        response = requests.get(url)
        
        if response.status_code == 200:
            characters = list(response.json())
        else:
            print("error, API don't work")
            return []
        
            # Filter Standart 5*
        limited5char = []
        for char in characters:
            if char in self.standart5char:
                pass
            else:
                limited5char.append(char)
        return limited5char

    def primo_to_usd(self, primo):
        bundles = self.prices["crystal"]

        costs_per_crystal = []
        for crys, price in bundles:
            costs_per_crystal.append(price / crys)
        
        average_cost_per_crystal = sum(costs_per_crystal) / len(costs_per_crystal)
        
        return round(primo * average_cost_per_crystal, 2)

    def main(self):
        print(f"""
{"="*40}
            Total Spend
Welkin Moon         {self.welkin_moon_spend:.2f} usd
Battle Pass         {self.BP_spend:.2f} usd
Battle Pass levl up {self.BP_LV_UP_spend:.2f} usd
Refil Resin         {self.resin_refil_spend:.2f} usd

total               {self.total_spend:.2f} usd
{"="*40}
""")


if __name__ == "__main__":    
    wc = whalecalculator()
    wc.main()