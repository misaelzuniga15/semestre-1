#Name:  Misael Zuniga
#Date:  Oct 17, 2022
#Class: CMIS 102

#Python program to compute the cost of house cleaning divided in fuctions

def welcome():
    print("Welcome to Z's Cleaning Services")
    print("This program will help you calculate the cost assossiated with our services")
    
def cleaning_type(type_cleaning):
    
    #Make note of cleaning services and give value to each feature
    dusting = 20
    bathrooms = 110
    floors = 30
    
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
        
    return(type_cleaning)

def house_size(size):
    
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
        
def calculation(type_cleaning, size, total):
    
    #add calculations
    total = type_cleaning * size
    return(type_cleaning, size, total)
    
def statement(type_cleaning, size, total):
        
    #Printing the total cost on the screen
    print('You have selected the    ', type_cleaning, ' service')
    print('for a house of           ', size, ' room(s)') 
    print('Total cost of cleaning:  ', total, ' dollars')

def main():
    #Display Welcome Message
    welcome()
    
    #Prompt for info
    type_cleaning = cleaning_type(type_cleaning)
    
    #Prompt for more info
    size = house_size(size)
    
    #compute calculations
    total = calculation(type_cleaning, size, total)
    
    #print findings
    statement(type_cleaning, size, total)
    

main()
