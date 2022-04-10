from ast import Str
from multiprocessing.dummy import Value
from pickle import FALSE
import time # imports time at which user enters code
import random # imports a random number
from random import randint # Imports a random integer from random
######################################################
#
# Starting Infomation #
# Each component to this code is split using a large
# hash tag wall e.g. ↧↧↧
######################################################
# This is to make less buildup in the folder for
# easier viewing of reviewers.
# All changes can be seen through the
# "Full_Order" versions
#
# Thanks for reading!
######################################################
# Create List of Items ###############################
# 12 Items With differing prices #####################
# Item List #
items = ['Mouse', 'Gaming Mouse', 'Keyboard', 'Gaming Keyboard',
         'Standard PC', 'Buiness PC', 'Editing PC',
         'Gaming PC', 'Laptop', 'Buiness Laptop', 'Editing laptop',
         'Gaming laptop', ] # List of choosable items 
# Item Prices #
item_prices = [15, 30, 20, 50, 150, 250, 325, 500, 150, 225, 275, 500, ] # Prices for each item above
# End ################################################
######################################################
# Create Customer Dictonary ##########################
# Has all needed stored customer info ################
customer_details = {} # Creates dictionary

order_list = []

order_cost = []
# End ################################################
######################################################
# Not Blank function #################################
# Makes it so that a question cant be left blank #####


def not_blank(string):
# Paramenter : string
# Returns : False / True
    if string == "": # If blank
        return False # Returns false
    else: # If else
        return True # Returns true


# End ###############################################
#####################################################
# Get String ########################################
# Parameters : question 
# Returns : String
def get_string(question):
    string = input(question) # string is equal to the question it is assigned to
    return string # Returns validated input

def validate_string(string):
# Parameter : string
# Returns : True / False
    counter=0 # Sets counter to 0
    if not_blank(string): # Checks if input isn't blank
        for a in string: # For a (alphabet numeric) in string
            if (a.isalpha()) == True: # Checks if the numeric is alpha
                counter+=1 # Adds to new string (validated) as it is a letter
            elif a == " ": # Includes spaces in validation
                counter+=1 # Adds to new validated string 
            else: # If other than the above
                print ("Your name can only consist of letters and spaces") # Error message
                return False # Returns false
    else: # If doesnt pass not_blank
        print ("Your name can only consist of letters and spaces") # Error message
        return False # Returns false
    return True # Once all letters have been validated returns true


# End ###############################################
#####################################################
# Pickup Info Entering                             ##
# Both Info entering create and print dictonary at ##
# the end of entering infomation                   ##
# This is used as a debugging device               ##


def pickup_info():
    # Aesthetics
    print ("###########################################################################################################")
    print ("")
    print ("__________.__        __                                 .__                 __             .___")
    print ("\______   \__| ____ |  | ____ ________     ______ ____  |  |   ____   _____/  |_  ____   __| _/")
    print (" |     ___/  |/ ___\|  |/ /  |  \____ \   /  ___// __ \ |  | _/ __ \_/ ___\   __\/ __ \ / __ | ")
    print (" |    |   |  \  \___|    <|  |  /  |_> >  \___ \ \  ___/|  |_\  ___/\  \___|  | \  ___// /_/ | ")
    print (" |____|   |__|\___  >__|_ \____/|   __/  /____  > \___  >____/\___  >\___  >__|  \___  >____ | ")
    print ("                  \/     \/     |__|          \/      \/          \/     \/          \/     \/ ")
    print ("")
    print ("###########################################################################################################")
    time.sleep(1)
    # End ######

    
    get_string_input("Please enter your name ", 'name') # Runs def
# print (customer_details['name']) #
    print ("---------------")
    phone() # Runs def
# print (customer_details['phone']) #
    print (customer_details)
    print ("---------------")

######################################################
# Phone Def ##########################################

def phone():
# Paramenters : question, number, ph_low, ph_high
# Returns : False / True
    ph_low = 7 # Sets a literal of 7
    ph_high = 10 # Sets a literal of 10

    question = ("Please enter your phone number ") # Asks and sets question
    number = get_string(question) # Gets input and sets to letters
    while not validate_phone(number, ph_low, ph_high): # If not true continues looping
        number = get_string(question) # Continues in loop due to false return
    customer_details['phone'] = number # Sets validated input to 'phone' in dictionary


# End ################################################
######################################################
# House Input Validation Def #########################

def house():
# Paramenter : none
# Returns : False / True
    question = ("Please enter your house number ") # Asks and sets question
    number = get_string(question) # Gets input and sets to letters
    while not validate_house(number): # If not true continues loop
        number = get_string(question) # Enters loop
    customer_details['house'] = number # Sets validated input to 'house' in dictonary

def validate_house(number):
# Paramenter : number
# Returns : False / True
    if validate_num(number): # If passes as true from validate_num code continues
        return True # Returns as true
    else: # If returns false
        print ("Please enter a number (must only contain digits)") # Error Message
        return False # Returns as false
    

# End ################################################
######################################################
# Phone Num Validator ################################

def validate_phone(number, ph_low, ph_high):
# Paramenters : number, ph_low, ph_high
    if validate_num(number): # Makes sure that the input is a integer
        test_num = int(number) # Converts to integer
        num_digits = 0 # Sets a literal
        while test_num > 0: # Makes sure it isn't blank
            test_num = test_num//10 
            num_digits = num_digits + 1 # Tests each digits to see if its a integer
        if num_digits >= ph_low and num_digits <= ph_high: # If between 7 and 10 digits long
            return True # Returns true
        else:
            print ("NZ phone numbers have 7-10 digits") # Error message
            return False # Returns as false
    else: # If itn't a integer instantly returns false
        print ("Please enter a number") # Error message
        return False # Returns false
        
def validate_num(number):
# Paramenter : number
    try: # Enters loop
        num = int(number) # Converts number to an integer 
        return True # If it correctly converts returns true
    except ValueError: # Catches exceptions
        return False # If not an integer return flase

# End ################################################
######################################################
# House Num Validator ################################

# End ################################################
######################################################
# Delivery Info Entering #############################


def delivery_info():
    # Aesthetics
    print ("###########################################################################################################")
    print ("")
    print ("________         .__  .__                                           .__                 __             .___")
    print ("\______ \   ____ |  | |__|__  __ ___________ ___.__.   ______ ____  |  |   ____   _____/  |_  ____   __| _/")
    print (" |    |  \_/ __ \|  | |  \  \/ // __ \_  __ <   |  |  /  ___// __ \ |  | _/ __ \_/ ___\   __\/ __ \ / __ | ")
    print (" |____/   \  ___/|  |_|  |\   /\  ___/|  | \/\___  |  \___ \ \  ___/|  |_\  ___/\  \___|  | \  ___// /_/ | ")
    print ("/_______  /\___  >____/__| \_/  \___  >__|   / ____| /____  > \___  >____/\___  >\___  >__|  \___  >____ | ")
    print ("        \/     \/                   \/       \/           \/      \/          \/     \/          \/     \/ ")
    print ("")
    print ("###########################################################################################################")
    time.sleep(1)
# End ######
# All #'s are for debugging #
# Add Try accepts Here #

    get_string_input("Please enter your name ", 'name')
# print (customer_details['name']) #
    print ("---------------")
    phone()
# print (customer_details['phone']) #
    print ("---------------")

    house()
# print (customer_details['house']) #
    print ("---------------")

    get_string_input("Please enter your street ", 'street')
# print (customer_details['street']) #
    print ("---------------")
    get_string_input("Please enter your suburb ", 'suburb')
# print (customer_details['suburb']) #
    print (customer_details)


# End ##################################################
########################################################
# Repeated input validator #############################

def get_string_input(question, field):
# Parameters : question, field, string
# Returns : True / False 
    string = get_string(question)
    while not validate_string(string):
        string = get_string(question)
    customer_details[field] = string


# End ##################################################
########################################################
# User Picking Delivery or Pickup ######################


def order_type():
# Parameters : none
# Returns : del_pick 
    del_pick = "" # Sets as empty text
    print ("Is your order for pickup or delivery?") # User infomation
    print ("For pickup enter 1")
    print ("For delivery enter 2")
    print ("---------------") # Aesthetic
    while True: # Creates loop
        try: # Tries
            delivery = int(input("Please enter 1 or 2 ")) # User input
            if delivery >= 1 and delivery <= 2: # Validates that input is either 1 or 2
                if delivery == 1: # If input is 1
                    print ("Pickup selected") 
                    pickup_info() # Runs pickup info def
                    del_pick = "pickup" # Sets del_pick as pickup
                    break # Breaks loop
                elif delivery == 2: # If input is 2
                    print ("Delivery selected")
                    delivery_info() # Runs delivery info def
                    del_pick = "delivery" # Sets del_pick as delivery
                    break # Breaks loop
            else: # If not 1 or 2
                print ("The number must be between 1-2") # Error message
        except ValueError: # If input is invalid
            print ("That input was invalid") # Error messages
            print ("Please enter a 1-2")
    return del_pick # Returns del_picks value


# End ##################################################
########################################################
# Item Def #############################################
# Prints the list of items in a neat vertical list #####


def menu():
# Parameters : none
# Returns : none
    number_items = 12 # Sets as a literal of 12

    # Aesthetic #
    print (" █████  █████                                    ")
    print ("░░███  ░░███                                     ")
    print (" ░███  ███████    ██████  █████████████    █████ ")
    print (" ░███ ░░░███░    ███░░███░░███░░███░░███  ███░░  ")
    print (" ░███   ░███    ░███████  ░███ ░███ ░███ ░░█████ ")
    print (" ░███   ░███ ███░███░░░   ░███ ░███ ░███  ░░░░███")
    print (" █████  ░░█████ ░░██████  █████░███ █████ ██████ ")
    print ("░░░░░    ░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░ ░░░░░░  ")
    time.sleep(1)
    # End Aethetic #

    for count in range(number_items): # Creates 12 item long list
        # Little Aesthetic # Made for list #
        print ("----------------")
        print (count+1, items[count], item_prices[count]) # List creation in order
        # End # 


# End ##################################################
########################################################
# Ordering Items #######################################
# Where the user picks items they want to order and ####
# how many things they want to order ###################


def order_item():
# Parameters : none
# Returns : value
    num_items = 0 # Sets num_items to 0
    while True: # Enters loop
        try:
            max_items = 5 # Literals for number of items
            min_items = 1 # *see above
            print ("---------------") # Aesthetic
            num_items = int(input("How many items do you want to order?")) # User infomation
            value = num_items # Creates value for the same value as num_items
            if num_items >= min_items and num_items <= max_items: # Makes it so there is a max of 5 items and a min of 1
                break # Breaks loop
            else: # If not 1-5 
                print("Your order must be between 1 and 5") # Error message
        except ValueError: # For invalid inputs
            print ("That was not a valid input") # Error messages
            print ("Please enter 1 to 5")

    for item in range(num_items): # For item in num_items lists ordered items
        while num_items > 0: # While num_items is greater than 0
            while True: # Enters loop
                try:
                    print ("---------------")
                    items_ordered = int(input("Please choose your items by entering the number from the menu")) # Creates items_ordered varible
                    if items_ordered >= 1 and items_ordered <= 12: # Makes that it must be 1-12 
                        break # Breaks loop
                    else: # If not 1-12 
                        print ("Your order must be between 1-12") # Error message
                except ValueError: # If input is invalid
                    print ("That was invalid") # Error messages
                    print ("Your order must be between 1-12")
            items_ordered = items_ordered-1 # 
            order_list.append(items[items_ordered])
            order_cost.append(item_prices[items_ordered])
            print ("{} ${:.2f}".format(items[items_ordered], item_prices[items_ordered])) # Orders list in 2dp in order of code
            num_items = num_items-1 # Reduces items ordered by 1 to allow to continue
    return value 


# End ##################################################
########################################################
# Order Print Out ######################################
# Prints out every single detail including:
# Name
# Phone Number
# Full Address
# Every item choosen and prices
# Prints Total Cost


def print_order(del_pick, value):
# Parameters : del_pick / Delivery or Pickup 
# Returns : total_cost  
    shipping_cost = 9 # Cost of shipping
    total_cost = sum(order_cost) # Calculates total cost
    print ("Your details")
    if del_pick == "pickup": # If order is pickup
        print ("Your order is for pickup") # The below is to print all customer details
        print (f"Customer Name: {customer_details['name']} Customer Phone: {customer_details['phone']}")
        print ("---------------")
    elif del_pick == "delivery": # If order is delivery
        print ("Your order is for delivery") # The below is to print all customer details
        print (f"Customer Name: {customer_details['name']} Customer Phone: {customer_details['phone']} Customer Address:{customer_details['house']}{customer_details['street']}{customer_details['suburb']}")
        print ("---------------") # Aesthetic
        if value <= 4: # Adds delivery cost if less than 4 items
            total_cost = total_cost + shipping_cost # Adds 9 to total cost


    # ADD ASCII FOR BELOW #
    print("Order details")
    count = 0 # Count is intially 0
    for item in order_list: # For every item in the list of items it prints them in 2dp 
        print ("---------------") # Aesthetic
        print ("ordered: {} cost ${:.2f}".format(item, order_cost[count])) # Displays costs in 2dp along with formating it in item and their cost for that item
        count = count+1 # This is done so the list displays the items in correct order
    print ("---------------") # Aesthetic
    print("total order cost")
    print (f"${total_cost:.2f}") # Prints the total at 2dp
    return total_cost # Returns total cost


# End ##################################################
########################################################
########################################################
# Welcome Def ##########################################
# Includes Welcome #####################################
# Uses random name Generator ###########################
# Random name Generator #
names = ["Mark", "Pheobe", "Sally", "Micheal", "Denise", "Jack", "William", "Afton", "Lara", "Caleb"] # List of names able to be choosen through random name generator
# End #


def welcome():
    num = randint(0, 9) # Creates a random number from 1-9
    name = (names[num]) # Name is choosen from 1-9 and uses it the number to choose the name from list
    print ("################################################################################")
    print ("")
    print(f"█████   ███   █████       ████                                            ")
    print(f"░░███   ░███  ░░███       ░░███                                            ")
    print(f"░███   ░███   ░███ ██████ ░███   ██████   ██████  █████████████    ██████")
    print(f"░███   ░███   ░██████░░███░███  ███░░███ ███░░███░░███░░███░░███  ███░░██")
    print(f"░░███  █████  ███░███████ ░███ ░███ ░░░ ░███ ░███ ░███ ░███ ░███ ░███████")
    print(f"  ░░░█████░█████░ ░███░░░  ░███ ░███  ███░███ ░███ ░███ ░███ ░███ ░███░░░ ")
    print(f"    ░░███ ░░███   ░░██████ █████░░██████ ░░██████  █████░███ █████░░██████​")
    print(f"     ░░░   ░░░     ░░░░░░ ░░░░░  ░░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░​")
    print ("")
    print ("################################################################################")
    print("")
    time.sleep(1) # Sleeps the program allowing it to pause and user is able to see aesthetic
    print("My name is", name,) # Brings name from the above and plugs it in so it is used
    print("I will be here to help you order with us")
    print ("---------------")


# END ##################################################
########################################################
# Reopen order / new exit ##############################


def new_exit():
    print ("Do want to reopen the program?")
    print ("To start another order press 1")
    print ("To exit press 2")
    while True:
        try:
            reopen = int(input(("Please enter a number")))
            print ("################################################################################")
            if reopen >= 1 and reopen <= 2: # Makes it so that it must be between 1 or 2 or doesnt continue code
                if reopen == 1: # if it = to 1 it creates new order and clears all lists, costs and details
                    print ("")
                    print ("███╗   ██╗███████╗██╗    ██╗     ██████╗ ██████╗ ██████╗ ███████╗██████╗ ")
                    print ("████╗  ██║██╔════╝██║    ██║    ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
                    print ("██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║█████╗  ██████╔╝")
                    print ("██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔══██╗██║  ██║██╔══╝  ██╔══██╗")
                    print ("██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║")
                    print ("╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝")
                    print ("")
                    time.sleep(1)
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear()
                    main() # Reopens the main def so it completely resets with new code 
                    break # Breaks off try accept
                elif reopen == 2:
                    print ("Thanks for shopping with us!")
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear()
                    exit()
            else:
                print ("Please enter a 1 or 2")
        except ValueError:
            print ("That input was invalid")
            print ("Please enter a 1-2")


# End ##################################################
########################################################
# Confirm order ########################################


def confirm_cancel():
# Parameters : None
# Returns : None
    print ("---------------")
    print ("Please confirm your order")
    print ("To confirm please press 1")
    print ("If the order is incorrect please enter 2")
    print ("---------------")
    while True: # Enters loop
        try:
            confirm = int(input(("Please enter a number "))) # Creates confirm varible
            if confirm >= 1 and confirm <= 2: # Validates so that confirm must be 1 or 2
                if confirm == 1: # If confirm equals 1
                    print ("")
                    print (" ██████╗ ██████╗ ███╗   ██╗███████╗██╗██████╗ ███╗   ███╗███████╗██████╗ ██╗")
                    print ("██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔══██╗████╗ ████║██╔════╝██╔══██╗██║")
                    print ("██║     ██║   ██║██╔██╗ ██║█████╗  ██║██████╔╝██╔████╔██║█████╗  ██║  ██║██║")
                    print ("██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██╔══██╗██║╚██╔╝██║██╔══╝  ██║  ██║╚═╝")
                    print ("╚██████╗╚██████╔╝██║ ╚████║██║     ██║██║  ██║██║ ╚═╝ ██║███████╗██████╔╝██╗")
                    print (" ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝")
                    print("")
                    time.sleep(1) # Sleeps the program
                    print ("---------------") # Aesthetic
                    print ("Order Confirmed")
                    print ("Your order has been sent to the shop")
                    print ("---------------")
                    new_exit() # Opens the exit or reset bot def
                    break # Breaks loop
                elif confirm == 2: # If confirm is equal to 2
                    print ("")
                    print (" ██████╗ █████╗ ███╗   ██╗ ██████╗███████╗██╗     ██╗     ███████╗██████╗ ██╗")
                    print ("██╔════╝██╔══██╗████╗  ██║██╔════╝██╔════╝██║     ██║     ██╔════╝██╔══██╗██║")
                    print ("██║     ███████║██╔██╗ ██║██║     █████╗  ██║     ██║     █████╗  ██║  ██║██║")
                    print ("██║     ██╔══██║██║╚██╗██║██║     ██╔══╝  ██║     ██║     ██╔══╝  ██║  ██║╚═╝")
                    print ("╚██████╗██║  ██║██║ ╚████║╚██████╗███████╗███████╗███████╗███████╗██████╔╝██╗")
                    print (" ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝╚══════╝╚══════╝╚═════╝ ╚═╝")
                    print ("")
                    time.sleep(1) # Sleeps the program
                    print ("---------------")
                    print ("Order Cancelled")
                    print ("You can restart your order or exit")
                    print ("---------------")
                    new_exit() # Opens the exit or reset bot def
                    break # Breaks loop
            else: # If not 1 or 2
                print ("Please enter a 1-2") # Reset message
        except ValueError: # If input is invalid
            print ("That input was invalid") # Error messages
            print ("Please enter a 1-2")


# End ##################################################
########################################################
# Main Def #############################################
# Creates most defs and uses them ######################
# Parameters : None
# Returns : None

def main(): # Runs the complete program
    welcome() # Runs opening def
    del_pick = order_type() # Del_pick is equal to input in order_type
    menu() # Prints list
    value = order_item() # Value is equal to inputs in order_item
    print_order(del_pick, value) # Prints order
    confirm_cancel() # Confirms the users order
main() # Runs main def


# End ##################################################
########################################################
