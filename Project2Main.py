import datetime
from dateutil.relativedelta import relativedelta as rd

def getAge():
    today = datetime.datetime.today()
    date = input("Enter your birthday (mm/dd/YYYY): ")
    date = datetime.datetime.strptime(date, "%m/%d/%Y")

    age = rd(today, date).years

    print(str(age))

if __name__ == '__main__':
    getAge()