#Name:  Misael Zuniga
#Date:  Nov 08, 2022
#Class: CMIS 102
#create a program to figure the share per person on a group vacation.

#Give the program a sequential order
def main ():
    print("Thank you for using the House service and Lawn Care program")
    name = welcome()
    #4. receive discount
    print("We have a few end of the year discounts")
    print("Please answer the following to see if you apply")
    seniorDiscount = getSeniorDiscountEligible()
    militaryDiscount = getMilitaryDiscountEligible()
    
    #1. Offer two services House Cleaning and Lawn services
    print("We offer House Cleaning 'HC' services and Lawn Care 'LC'")
    service = getTypeOfService()
    if (service == 1):
        size = getHouseSize()
        #2. house small medium and large houses 3 services
        dusting = 20
        bathrooms = 110
        floors = 30
        HouseCleaningServices = getHouseCleaningServices()
        for services in HouseCleaningServices:
            if 'dusting' in services:
                totalForDusting = dusting * size
            elif 'bathrooms' in services:
                totalForBathrooms = bathrooms * size
            elif 'floors' in services:
                totalForFloors = floors * size
            else:
                print("We do not offer the service you requested")
                getHouseCleaningServices()
        HouseCleaningPrice = getPriceHouseCleaning(totalForDusting, totalForBathrooms, totalForFloors)
        
    elif (service == 2):
        #3. lawn price of mow per square ft and edging linear ft, shrub pruning
        
        LawnSquareFeet = getLawnSquareFeet()
        
        LawnLinearFeet = getLawnLinearFeet()
        
        AmountofShrubs = getAmountOfShrubs()

        LawnCarePrice = getPriceLawnCareService(LawnSquareFeet, LawnLinearFeet, AmountofShrubs, grassMowing, edging, shrub)

    elif (servise == 3):
        size = getHouseSize()
        #2. house small medium and large houses 3 services
        dusting = 20
        bathrooms = 110
        floors = 30
        HouseCleaningServices = getHouseCleaningServices()
        for services in HouseCleaningServices:
            if 'dusting' in services:
                totalForDusting = dusting * size
            elif 'bathrooms' in services:
                totalForBathrooms = bathrooms * size
            elif 'floors' in services:
                totalForFloors = floors * size
            else:
                print("We do not offer the service you requested")
                getHouseCleaningServices()
        LawnSquareFeet = getLawnSquareFeet()
        
        LawnLinearFeet = getLinearFeet()
        
        AmountofShrubs = getAmountOfShrubs()
    grassMowing = 1.2
    edging = .3
    shrub = 2
    HouseCleaningPrice = getPriceHouseCleaning(totalForDusting, totalForBathrooms, totalForFloors)     
    LawnCarePrice = getPriceLawnCareService(LawnSquareFeet, LawnLinearFeet, AmountofShrubs, grassMowing, edging, shrub)
    


    display(name, seniorDiscount, militaryDiscount, HouseCleaningServices, LawnSquareFeet, LawnLinearFeet, AmountofShrubs, LawnCarePricetotalForDusting, totalForBathrooms, totalForFloors, size, grassMowing, edging, shrub)
        
          #
def welcome():
    name = input("What is your name?\n\t")
    if not name.isalpha:
        print("Please use only alpha characters")
        welcome()
    else:
        return name

def getSeniorDiscountEligible():
    seniorDiscount = 1
    age = eval(input("How old are you?\n\t"))
    if (age >= 65):
        seniorDiscount = 1.1
    else:
        seniorDiscount = 1
    return seniorDiscount

def getMilitaryDiscountEligible():  
    militaryDiscount = 1
    military = input("Are you a active duty military or veteran?(Y/N)\n\t")
    if (military == 'Y' or military == 'y'):
        militaryDiscount = 1.1
    elif (military == 'N' or military == 'n'):
        militaryDiscount = 1
    elif (military != ('Y' or 'y' or 'N' or 'n')) :
        print("I'm sorry the selection you made is not acceptable only type 'Y' or 'N'")
        getMilitaryDiscountEligible()
    return militaryDiscount
    
def getTypeOfService():
    service = 0
    typeOfService = input("What service do you require? ('HC', 'LC', or 'Both'\n\t")
    if (typeOfService == ('HC' or'hc' or 'Hc')):
        
        service = 1
    elif (typeOfService == ('LC' or 'lc' or 'Lc')):
        service = 2
    elif (typeOfService == ('Both' or 'both')):
        service = 3
    else:
        print("the selection you typed is not acceptable only allowable answers are:")
        print(" 'HC' for House Cleaning, 'LC' for Lawn Care or Both")
        getTypeOfService()
    return service

def getHouseSize():
    small, medium, large = 1, 1.5, 2
    size = input('How many rooms does your house have? (one, two, three, four, five, six):\n\t')
    if size == ('one' or 'two'):
        size = small
    elif size == ('three' or 'four'):
        size = medium
    elif size == ('five' or 'six'):
        size = large
    else:
        print("Your response was not recongize please check your spelling")
        getHouseSize()
    return size

def getHouseServices():
    addedHouseCleaningServices = []
    HouseCleaningServices = ['dusting', 'bathrooms', 'floors']
    for service in HouseCleaningServices:
        input(f'Would you like the {HouseCleaningService} service?(Y/N)')
        if service == ('Y' or 'yes' or 'Yes' or 'YES'):
            addedHouseCleaningServices.append(HouseCleaningService)
        elif service ==('N' or 'no' or 'No' or 'NO'):
            None
    return addedHouseCleaningService

def getLawnSquareFeet():
    LawnSquareFeet = input("What is your property's Square Footage?\n\t")
    if not LawnSquareFeet.isdigit():
        print('PLease type only integers')
    else:
        return LawnSquareFeet

def getLawnLinearFeet():
    LawnLinearFeet = input("What is your property's Perimeter's linear Footage?\n\t")
    if not LawnLinearFeet.isdigit():
        print('PLease type only integers')
    return LawnLinearFeet

def getAmountOfShrubs():
    AmountOfShrubs = input("How many Shrubs will be worked?\n\t")
    if not AmountOfShrubs.isdigit():
        print('PLease type only integers')
    return AmountOfShrubs

def getPriceHouseCleaning(totalForDusting, totalForBathrooms, totalForFloors):
     HouseCleaningPrice = totalForDusting + totalForBathrooms + totalForFloors

def getPriceLawnCareService(LawnSquareFeet, LawnLinearFeet, AmountofShrubs, grassMowing, edging, shrub):
    priceOfMowing = LawnSquareFeet * grassMowing
    priceOfEdging = LawnLinearFeet * edging
    priceOfPruning = AmountofShrub * shrub

    LawnCarePrice = priceOfMowing + priceOfEdging + priceOfPruning
    return(LawnCarePrice, priceOfMowing, priceOfEdging, priceOfPruning)
    
   #5. output is cost of service
def display(name, seniorDiscount, militaryDiscount, HouseCleaningServices, LawnSquareFeet, LawnLinearFeet, AmountofShrubs, LawnCarePrice, totalForDusting, totalForBathrooms, totalForFloors, size, grassMowing, edging, shrub):
    print(f"Thank you {name}. for utilizing our program")
    if ((seniorDiscount, militaryDiscount) != (0,0)):
        print("I'm sorry you do not qualified for any discounts")
    elif (seniorDiscount == 1.1):
        print("You qualify for Senior Discount of 10%")
    elif (militaryDiscount == 1.1):
        print("You qualify for Military Discount of 10%")
    elif ((seniorDiscount, militaryDiscount) == (1.1, 1.1)):
        print("Congratulations! you are eligible for both Senior and Military Discounts for 20%")
    if (service == 1):
        print("You have choosen to do House Cleaning Services only")
        print(f"The services selected were:{HouseCleaningServices}")
        print(f'For a {size} house like yours')
        if 'duting' in HouseCleaningServices:
            print(f'Dusting will cost $', totalForDusting)
        elif 'bathrooms' in  HouseCleaningServices:
            print(f'Bathrooms cleaning will cost $', totalForBathrooms)
        elif 'floors' in HouseCleaningServices:
            print(f'Floors cleaning will cost $', totalForFloors)
        print(f'The total cost for the selected services is ${HouseCleaningPrice}')
        print("The price with dicount is $", HouseCleaningPrice * militaryDiscount * seniorDiscount)
            
    elif (service == 2):
        print("You have choosen to do Lawn Care Services only")
        if (LawnSquareFeet >= 1):
            print(f"You selected Lawn Mowing for a house of {LawnSquareFeet} with a cost of $", LawnSquareFeet * gressMowing)
        elif (LawnLinearFeet >= 1):
            print(f"You selected Lawn Mowing for a house of {LawnLinearFeet} with a cost of $", LawnLinearFeet * edging)
        elif (AmountofShrubs >= 1):
            print(f"You selected Lawn Mowing for a house of {AmountofShrubs} with a cost of $", AmountofShrubs * shrub)
        print(f"The total cost of Lawn Care services is $ {LawnCarePrice}")
        print("The price with dicount is $", LawnCarePrice * militaryDiscount * seniorDiscount)
        
    elif (service == 3):
        print("You have choosen to do House Cleaning and Lawn Care Services")
        print(f"The services selected for House Cleaning were:{HouseCleaningServices}")
        print(f'For a {size} house like yours')
        if 'duting' in HouseCleaningServices:
            print(f'Dusting will cost $', totalForDusting)
        elif 'bathrooms' in  HouseCleaningServices:
            print(f'Bathrooms cleaning will cost $', totalForBathrooms)
        elif 'floors' in HouseCleaningServices:
            print(f'Floors cleaning will cost $', totalForFloors)
        print(f'The total cost for the selected services is ${HouseCleaningPrice}')
        print("For the Lawn Care Services")
        if (LawnSquareFeet >= 1):
            print(f"You selected Lawn Mowing for a house of {LawnSquareFeet} with a cost of $", LawnSquareFeet * gressMowing)
        elif (LawnLinearFeet >= 1):
            print(f"You selected Lawn Mowing for a house of {LawnLinearFeet} with a cost of $", LawnLinearFeet * edging)
        elif (AmountofShrubs >= 1):
            print(f"You selected Lawn Mowing for a house of {AmountofShrubs} with a cost of $", AmountofShrubs * shrub)
        print(f"The total cost of Lawn Care services is $ {LawnCarePrice}")
        totalCost = HouseCleaningPrice + LawnCarePrice
        print("All together the cost will be $", totalCost)
        print("The price with dicount is $", totalCost * militaryDiscount * seniorDiscount)
    
        
main()        
    
 
    
    
