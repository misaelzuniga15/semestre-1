def main ():
    # print("Thank you for using the House service and Lawn Care program")
    # userName = getUserName()
    availableServices = ["House Cleaning", "Lawn care", "Both"]
    selectedService = getTypeOfService(availableServices)

    total = 0

    if selectedService == 0:
        type_cleaning, size, total = houseCleaningService()
    elif selectedService == 1:
        total = lawnCareService()
    else:
        total = houseCleaningService()
        # print("Tnow next service")
        total = lawnCareService() + total

    # apply discount
    # display results

def houseCleaningService():

    #Prompt for info
    type_cleaning, selectedCost = HScleaning_type()
    
    #Prompt for more info
    size = HChouse_size()
    
    #compute calculations
    total = HCcalculation(selectedCost, size)
    
    #print findings
    #HCstatement(type_cleaning, size, total)

    return (type_cleaning, size, total)

def HScleaning_type():
    
    #Make note of cleaning services and give value to each feature
    dustingCost = 20
    bathroomsCost = 110
    floorsCost = 30

    selectedCost = 0
    
    #Prompt type of cleaning
    type_cleaning = input('Please Enter the type of cleaning you want(dusting, bathrooms, or floors):\n   ')
    if (type_cleaning == 'dusting'):
        selectedCost = dustingCost
    elif (type_cleaning == 'bathrooms'):
        selectedCost = bathroomsCost
    elif (type_cleaning == 'floors'):
        selectedCost = floorsCost
    else:
        print('please check your spelling and select from the following options:\n\t (dusting, bathrooms, floors)')
        input('\t')
        
    return(type_cleaning, selectedCost)

def HChouse_size():
    
    #Assing multiple for different size of houses
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    
    #Prompt for number of rooms
    size = input('How many rooms does your house have? (one, two, three, four, five, six):\n   ')
    if size == 'one':
        size = one
    elif size == 'two':
        size = two
    elif size == 'three':
        size = three
    elif size == 'four':
        size = four
    elif size == 'five':
        size = five
    elif size == 'six':
        size = six
    else:
        print('PLease check your spelling and select from the following options:\n\t (one, two, three, four, five, six)')
        input('\t')
    return(size)
        
def HCcalculation(type_cleaning, size):
    
    #add calculations
    total = type_cleaning * size
    return total
    
def HCstatement(type_cleaning, size, total):
        
    #Printing the total cost on the screen
    print('You have selected the    ', type_cleaning, ' service')
    print('for a house of           ', size, ' room(s)') 
    print('Total cost of cleaning :  ', total, ' dollars')


def lawnCareService():
    return ''

def getTypeOfService(availableServices):
    
    print(*('{} {}'.format(i,s) for i,s  in enumerate(availableServices, start=1)), sep='\n')

    selectedService = input("Please enter the number from the avalable services")

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