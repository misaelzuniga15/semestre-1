def main ():
    print("Thank you for using the House service and Lawn Care program")
    userName = getUserName()
    
    print("The following list is the list of avalable services")
    availableServices = ["House Cleaning", "Lawn care", "Both"]
    selectedService = getTypeOfService(availableServices)

    HCtotal = 0
    LCtotal = 0

    if selectedService == 0:
        HCtotal = houseCleaningService()
    elif selectedService == 1:
        LCtotal = lawnCareService()
    else:
        HCtotal = houseCleaningService()
        print("\nNow to the next service\n")
        LCtotal = lawnCareService()

    print("In order to see if you qualify for additional discounts")
    discount = Seniordiscount()

    totalStatement(HCtotal, LCtotal, discount)
    # display results
    print(f"Thank you {userName} for using out program")

    

def totalStatement(HCtotal, LCtotal, discount):
    totalStatement = HCtotal + LCtotal
    discountStatement = (totalStatement - (totalStatement * discount))
    print(f"This brings your total to $ {discountStatement}")
    

def Seniordiscount():
    discount = 0
    age = eval(input("Please provide us with your age.\n\t"))
    if age >= 65:
        discount = .1
        print("Congratulations you apply for Senior discount of 10 %")
    return discount

def houseCleaningService():

    #Prompt for info
    HCtype_cleaning, HCselectedCost = HScleaning_type()
    
    #Prompt for more info
    HCsize, rooms = HChouse_size()
    
    #compute calculations
    HCtotal = HCcalculation(HCselectedCost, HCsize)
    
    #print findings
    HCstatement(HCtype_cleaning, HCtotal, rooms)

    return (HCtotal)

def HScleaning_type():
    
    #Make note of cleaning services and give value to each feature
    dustingCost = 20
    bathroomsCost = 110
    floorsCost = 30

    HCselectedCost = 0
    
    #Prompt type of cleaning
    HCtype_cleaning = input('Please Enter the type of cleaning you want from the following(dusting, bathrooms, or floors):\n\t')
    if (HCtype_cleaning == 'dusting'):
        HCselectedCost = dustingCost
    elif (HCtype_cleaning == 'bathrooms'):
        HCselectedCost = bathroomsCost
    elif (HCtype_cleaning == 'floors'):
        HCselectedCost = floorsCost
    else:
        print('please check your spelling and select from the following options:\n\t (dusting, bathrooms, floors)')
        input('\t')
        
    return(HCtype_cleaning, HCselectedCost)

def HChouse_size():
    
    #Assing multiple for different size of houses
    HCsize = 0
    
    #Prompt for number of rooms
    rooms = input('How many rooms does your house have? (one, two, three, four, five, six):\n\t')
    if rooms == 'one':
        HCsize = 2
    elif rooms == 'two':
        HCsize = 2
    elif rooms == 'three':
        HCsize = 5
    elif rooms == 'four':
        HCsize = 5
    elif rooms == 'five':
        HCsize = 5
    elif rooms == 'six':
        HCsize = 6
    else:
        print('PLease check your spelling and select from the following options:\n\t (one, two, three, four, five, six)')
        input('\t')
    return HCsize, rooms
        
def HCcalculation(HCselectedCost, HCsize):
    #add calculations
    HCtotal = HCselectedCost * HCsize
    return HCtotal
    
def HCstatement(HCtype_cleaning, HCtotal, rooms):
        
    #Printing the total cost on the screen
    print('You have selected the    ', HCtype_cleaning, ' service')
    print('for a house of           ', rooms, ' room(s)') 
    print('Total cost of cleaning :  ', HCtotal, ' dollars')
    return HCtotal

def lawnCareService():
    LCselectedsize = 0
    LCperimetersize = 0
    LCedgingCost = 0
    LCmowingPrice = 0
      #Prompt for info
    typeLawnCare, LCselectedCost2 = LawnCareService_type()
    if typeLawnCare == 'mowing':
        LCselectedsize, LCmowingPrice = LClawn_size()
    elif typeLawnCare == 'edging':
        LCperimetersize, LCedgingCost = LCedge_length()
    else:
        shrubs = LCpruning()
    #compute calculations
    LCtotal = LCcalculation(LCmowingPrice, LCedgingCost)
    
    #print findings
    LCtotal = LCstatement(typeLawnCare, LCselectedsize, LCmowingPrice, LCperimetersize, LCedgingCost, LCtotal)

    return (LCtotal)

def LawnCareService_type():
    #Make note of cleaning services and give value to each feature
    mowingLawnCost = 1.12
    edgingCost = 1.02
    Pruning = 30

    selectedCost2 = 0
    
    #Prompt type of cleaning
    typeLawnCare = input('Please Enter the type of Lawn Care you want(mowing, edging, or pruning):\n\t')
    if (typeLawnCare == 'mowing'):
        selectedCost2 = mowingLawnCost
    elif (typeLawnCare == 'edging'):
        selectedCost2 = edgingCost
    elif (typeLawnCare == 'pruning'):
        selectedCost2 = Pruning
    else:
        print('please check your spelling and select from the following options:\n\t (dusting, bathrooms, floors)')
        input('\t')
        
    return(typeLawnCare, selectedCost2)

def LCpruning():
    shrubs = eval(input("How many shrubs do you have?"))
    return shrubs

def LClawn_size():
    propertySize = ["2000-7000", "7000-8500", "8500+"]
    LCmowingPrice = 0
    print(*('{} {}'.format(i,s) for i,s  in enumerate(propertySize, start=1)), sep='\t')

    LCselectedsize = input("Please enter the number which indicates your property size in Square Footage\n\t")

    if not LCselectedsize.isdigit():
        print("Please enter a valid option")
        LClawn_size()
    else:
        LCselectedsize = int(LCselectedsize) - 1

    if LCselectedsize >= len(propertySize):
        print("Please enter a valid option")
        LClawn_size()
    if LCselectedsize == 0:
        LCselectedsize = "2000-7000"
        LCmowingPrice = 30
    elif LCselectedsize == 1:
        LCselectedsize = "7000-8500"
        LCmowingPrice = 40
    elif LCselectedsize == 2:
        LCselectedsize = "8500+"
        LCmowingPrice = 50
    return LCmowingPrice, LCselectedsize

def LCedge_length():
    propertySize = ['0-300', '300-450', '450+']
    LCedgingCost = 0

    print(*('{} {}'.format(i,s) for i,s  in enumerate(propertySize, start=1)), sep='\t')

    LCperimetersize = input("Please enter the number which indicates your property's perimeter size")

    if not LCperimetersize.isdigit():
        print("Please enter a valid option")
        LClawn_size()
    else:
        LCperimetersize = int(LCperimetersize) - 1

    if LCperimetersize >= len(propertySize):
        print("Please enter a valid option")
        LClawn_size()
    if LCperimetersize == 0:
        LCperimetersize = '0-300'
        LCedgingCost = 5
    elif LCperimetersize == 1:
        LCperimetersize = '300-450'
        LCedgingCost = 10
    elif LCperimetersize == 2:
        LCperimetersize = '450+'
        LCedgingCost = 15
    return LCperimetersize, LCedgingCost

def LCcalculation(LCmowingPrice, LCedgingCost):
    LCtotal = (LCmowingPrice + LCedgingCost)
    return LCtotal

def LCstatement(typeLawnCare, LCselectedsize, LCperimetersize, LCtotal):
        
    #Printing the total cost on the screen
    print('You have selected the       ', typeLawnCare, ' service')
    if (LCselectedsize > 0):
        print('for a house with            ', LCselectedsize, "square footage") 
    elif (LCperimetersize > 0):
        print('for a house with            ', LCperimetersize, "linear footage")
    print('Total cost of Lawn Care is: ', LCtotal, ' dollars')

def getTypeOfService(availableServices):
    
    print(*('{} {}'.format(i,s) for i,s  in enumerate(availableServices, start=1)), sep='\n')

    selectedService = input("Please enter the number from the avalable services\n\t")

    if not selectedService.isdigit():
        print("Please enter a valid option")
        getTypeOfService(availableServices)
    else:
        selectedService = int(selectedService) - 1

    if selectedService >= len(availableServices):
        print("Please enter a valid option")
        getTypeOfService(availableServices)
    
    return selectedService
    
def getUserName():
    name = input("What is your name?\n\t")
    if not name.isalpha:
        print("Please use only alpha characters")
        getUserName()
    else:
        return name

main() 
