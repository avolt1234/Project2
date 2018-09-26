import datetime
from dateutil.relativedelta import relativedelta as rd

def getAge():
    today = datetime.datetime.today()
    #date = input("Enter your birthday (mm/dd/YYYY): ")
    date = "05/12/1991"
    try:
        date = datetime.datetime.strptime(date, "%m/%d/%Y")
    except:
        print("Error in the date")
        return
    age = rd(today, date).years
    print(age)
    return age

def approval(rentalList, age):

    appDict = {"EC" : 0, "E": 0, "E10": 10, "T": 13, "M": 17, "AO": 17}

    #List for movies than can be rented
    finalList = []

    #List for movies that cannot be rented
    failList = []

    for rental in rentalList.items():
        if age >= appDict[rental[1]]:
            finalList.append(rental)
        else:
            failList.append(rental)

    print("The user can rent the following movies: ")
    for item in finalList:
        print("Title: " + item[0] + "\t\t\tRating: " + item[1])


if __name__ == '__main__':

    rentalList = {"Tekken": "M", "Top Gun": "T", "TMNT": "E", "Speed": "AO", "Demolition Man": "E10", "Yea": "EC"}
    age = 9
    approval(rentalList, age)
    #getAge()