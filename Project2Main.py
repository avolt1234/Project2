import datetime
from dateutil.relativedelta import relativedelta as rd

def getAge(date):
    today = datetime.datetime.today()
    try:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
    except:
        print("Error in the date")
        return
    age = rd(today, date).years

    if age <= 0:
        print('Please enter age above 0')
        return
    approval(age)

def getTestAge(date):
    today = datetime.datetime.today()
    # date = "05/12/1991"
    try:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
    except:
        print("Error in the date")
        return
    age = rd(today, date).years

    if age <= 0:
        print('Please enter age above 0')
    return age

def approval(age, rentalList=None):

    appDict = {"EC" : 0, "E": 0, "E10": 10, "T": 13, "M": 17, "AO": 18}

    #List for movies than can be rented
    finalList = []

    #List for movies that cannot be rented
    failList = []

    if rentalList != None:
        if age <= 0:
            return
        else:
            print('\n\nAge of renter = ' + str(age))
            for rental in rentalList.items():
                if age >= appDict[rental[1]]:
                    finalList.append(rental)
                else:
                    failList.append(rental)
    else:
        while True:
            quitter = input("Enter C to checkout or press R to enter another movie: ")
            if quitter.capitalize() == 'C':
                break
            title = input("Enter the name of the movie: ")
            rating = input("Enter the rating of the movie (EC, E, E10, T, M, AO): ")
            try:
                if age >= appDict[rating.upper()]:
                    newList = [title, rating]
                    finalList.append(newList)
                else:
                    newList = [title, rating]
                    failList.append(newList)
            except Exception as e:
                print("The rating " + str(e) + " is invalid, please enter a valid rating")

    if len(finalList) > 0:
        print("\nThe user can rent the following movies: ")
        for item in finalList:
            print("Title: " + item[0] + "\t\t\tRating: " + item[1])

    if len(failList) != 0:
        print("\n\nThe user cannot rent the following movies:")
        for item in failList:
            print("Title: " + item[0] + "\t\t\tRating: " + item[1])



if __name__ == '__main__':

    debug = input("Enter Y to test: ")
    if debug.capitalize() == "Y":
        rentalList = {"Tekken": "M", "Top Gun": "T", "TMNT": "E", "Speed": "AO", "Demolition Man": "E10", "Yea": "EC"}
        todaysDate = datetime.datetime.today()

        #ageList contains
        ageList = [(todaysDate + rd(years=1)), todaysDate, (todaysDate + rd(years=-1)), (todaysDate + rd(years=-16))
                   , (todaysDate + rd(years=-17)), (todaysDate + rd(years=-18)), (todaysDate + rd(years=-17)),
                   (todaysDate + rd(years=-18)), (todaysDate + rd(years=-19))]
        for year in ageList:
            td = str(year.date())
            age = getTestAge(td)
            approval(age, rentalList)
    else:
        date = input("Enter your birthday (YYYY-mm-dd): ")
        getAge(date)