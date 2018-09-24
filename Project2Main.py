import datetime
from dateutil.relativedelta import relativedelta as rd

def runTheProgram():
    breaker = True

def getAge():
    today = datetime.datetime.today()
    date = input("Enter your birthday (mm/dd/YYYY): ")
    try:
        date = datetime.datetime.strptime(date, "%m/%d/%Y")
    except:
        print("Error in the date")
        return
    age = rd(today, date).years

    print(str(age))

if __name__ == '__main__':
    getAge()