#Name:  Misael Zuniga
#Date:  Nov 08, 2022
#Class: CMIS 102
#create a program to figure the share per person on a group vacation.

#Give the program a sequential order
def main ():
    #Welcome the user
    print("Welcome to vacations expense split program")
    user = input("Please type your name to continue\n\t")
    if not user.isalpha():
        print("****Please enter alpha characters only****\n")
        main()
    else:
        print("Thank you", user,", let's start with listing people")
    #1. Get number of people
    people = getPeoplesName()
    #2. get number of days
    NumberOfDays = getNumberOfDays()
    #todo: verify is numeric
    
    #3. get cost of food
    costOfFoodByDay = getCostOfDaysByCategory(NumberOfDays, 'Food')
    #4. get cost of gas
    costOfGasByDay = getCostOfDaysByCategory(NumberOfDays, 'Gas')

    displayResults(costOfFoodByDay, costOfGasByDay, people, user)
    

def getPeoplesName():
    #return an array of people
    names = []
    #request input with a loop to end when 'done' is typed
    name = input("Type a person on this trip (Type 'done' to end)\t")
    while (name != 'done'):
        #ensure only alpha characters are being used
        if not name.isalpha():
            print("Please type alpha characters only")
            getPeoplesName()
        else:
            names.append(name)
            name = input("Type a person on this trip (Type 'done' to end)\t")
    #return the list of names
    return names

def getNumberOfDays():
    # ask user amount of days and fill an array with it
    NumberOfDays = eval(input("how many days was this trip?\t"))
    if NumberOfDays <= 0:
        print("Please Type an appropriate number of days")
        getNumberOfDays()
    else:
    #return the number of days
        return NumberOfDays


def getCostOfDaysByCategory(NumberOfDays, Category):
    #build an array for cost of both food and gas utilizing the same fuction
    #changing the category for food and gas
    cost = []
    day = 1
    digits = ('1234567890')
    #loop the input for the days of the vacation
    while day <= NumberOfDays:
        spendByDay = eval(input(f'How much did you spend on {Category} on day {day}?\t'))
        if isinstance(spendByDay, int):
            cost.append(spendByDay)
            day = day + 1
            
        else:
            print("Please print numeric characters only")
            getCostOfDaysByCategory(NumberOfDays, Category)
            
    #return the cost
    return cost

def displayResults(costOfFoodByDay, costOfGasByDay, people, user):
    #5. print cost for category
    print("Here's the break down of food expenses per day")
    print(*('{} {}'.format(i,s) for i,s  in enumerate(costOfFoodByDay, start=1)), sep='\n')
    print("Here's the break down of gas expenses per day")
    print(*('{} {}'.format(i,s) for i,s  in enumerate(costOfGasByDay, start=1)), sep='\n')
    #6. print cost of the trip
    totalCost = ((sum(costOfFoodByDay)) + (sum(costOfGasByDay)))
    print("The total cost of the trip is:\t", totalCost)
    #7. print share of each person
    shareByPerson = totalCost / len(people)
    for name in people:
        print(f'The share for {name} is {shareByPerson}')
    print("Thank you", user," for using this program!")

#start the program    
main()
