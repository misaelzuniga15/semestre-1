def main():
    #Display Welcome Message
    print("Welcome to Z's Cleaning Services")
    print("This program will help you calculate the cost assossiated with our services")
    
    #Prompt for info
    type_cleaning, size = calculations()

    #Calculate the total and final cost of items
    total = type_cleaning * size
    
    #Display output
    Display_bill(type_cleaning, size, total)
        

def calculations():

    #Make note of cleaning services and give value to each feature
    dusting = 20
    bathrooms = 110
    floors = 30

    #Assing multiple for different size of houses
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6

    #Prompt type of cleaning
    type_cleaning = input('Please Enter the type of cleaning you want(dusting, bathrooms, or floors):\n   ')
    if (type_cleaning == 'dusting'):
        type_cleaning = dusting
    elif (type_cleaning == 'bathrooms'):
        type_cleaning = bathrooms
    elif (type_cleaning == 'floors'):
        type_cleaning = floors
    else:
        print('please check your spelling and select from the following options:\n\t (dusting, bathrooms, floors)')
        input('\t')

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

    return(type_cleaning, size)

def Display_bill(type_cleaning, size, total):
        
    #Printing the total cost on the screen
    print('You have selected the    ', type_cleaning, ' service')
    print('for a house of           ', size, ' room(s)') 
    print('Total cost of cleaning:  ', total, ' dollars')

main()
    
