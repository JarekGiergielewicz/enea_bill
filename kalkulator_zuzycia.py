
class CalcuEnea:

    def __init__(self):
        self.data = []
        self.base = {}


    def data_kw(self, kw):
        self.kw = kw
        self.data.append(self.kw)
        return self.data

    def base_kw(self, check_date):
        self.check_date = check_date
        self.base[self.check_date] = self.data

    def data_cal(self):
        self.cal = []

        for i in self.base:
           self.cal.append(sum(self.base[i]))

        return f'Zużyte kWh za podany okres to: {sum(self.cal)}'


    def data_sheet(self):
        self.base['Razem:'] = sum(self.cal)
        return self.base

    def save_data(self, time_save):
        self.time_save = time_save
        with open(f'/Users/jarek/Desktop/zużycie prądu/{self.time_save}.txt', 'a') as file:
            file.write(str(self.data_sheet()))
        print(f'dane zapisane w pliku: {self.time_save}.txt')




