from ast import Str
from multiprocessing.dummy import Value
from pickle import FALSE
import time
import random
from random import randint
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
         'Gaming laptop', ]
# Item Prices #
item_prices = [15, 30, 20, 50, 150, 250, 325, 500, 150, 225, 275, 500, ]
# End ################################################
######################################################
# Create Customer Dictonary ##########################
# Has all needed stored customer info ################
customer_details = {}

order_list = []

order_cost = []
# End ################################################
######################################################
# Not Blank function #################################
# Makes it so that a question cant be left blank #####


def not_blank(string):
    if string == "":
        return False
    else:
        return True



# End ###############################################
#####################################################
# Get String ########################################

def get_string(question):
    string = input(question)
    return string

def validate_string(string):
    counter=0
    if not_blank(string):
        for a in string:
            if (a.isalpha()) == True:
                counter+=1
            elif a == " ":
                counter+=1                
            else:
                return False
    else:
        return False
    return True


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

    
    question = ("Please enter your name ")
    string = get_string(question)
    while not validate_string(string):
        string = get_string(question)
        print ("Your name can only consist of letters and spaces")
    customer_details['name'] = string


# print (customer_details['name']) #
    print ("---------------")

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
# print (customer_details['phone']) #
    print (customer_details)
    print ("---------------")


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
    question = ("Please enter your name ")
    name = get_string(question)

    customer_details['name'] = not_blank(question)
# print (customer_details['name']) #
    print ("---------------")

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
# print (customer_details['phone']) #
    print ("---------------")

    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)
# print (customer_details['house']) #
    print ("---------------")

    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question) 
# print (customer_details['street']) #
    print ("---------------")

    question = ("Please enter your suburb ")
    customer_details['suburb'] = not_blank(question)
# print (customer_details['suburb']) #
    print (customer_details)


# End ##################################################
########################################################
# User Picking Delivery or Pickup ######################


def order_type():
    del_pick = ""
    print ("Is your order for pickup or delivery?")
    print ("For pickup enter 1")
    print ("For delivery enter 2")
    print ("---------------")
    while True:
        try:
            delivery = int(input("Please enter 1 or 2 "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Pickup selected")
                    pickup_info()
                    del_pick = "pickup"
                    break
                elif delivery == 2:
                    print ("Delivery selected")
                    delivery_info()
                    del_pick = "delivery"
                    break
            else:
                print ("The number must be between 1-2")
        except ValueError:
            print ("That input was invalid")
            print ("Please enter a 1-2")
    return del_pick


# End ##################################################
########################################################
# Item Def #############################################
# Prints the list of items in a neat vertical list #####


def menu():
    number_items = 12

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

    for count in range(number_items):
        # Little Aesthetic # Made for list #
        print ("----------------")
        print (count+1, items[count], item_prices[count])
        # End # 


# End ##################################################
########################################################
# Ordering Items #######################################
# Where the user picks items they want to order and ####
# how many things they want to order ###################


def order_item():
    num_items = 0
    while True:
        try:
            max_items = 5 # Constants for number of items
            min_items = 1 # *see above
            print ("---------------")
            num_items = int(input("How many items do you want to order?"))
            value = num_items
            if num_items >= min_items and num_items <= max_items:
                break
            else:
                print("Your order must be between 1 and 5")
        except ValueError:
            print ("That was not a valid input")
            print ("Please enter 1 to 5")

    for item in range(num_items):
        while num_items > 0:
            while True:
                try:
                    print ("---------------")
                    items_ordered = int(input("Please choose your items by entering the number from the menu"))
                    if items_ordered >= 1 and items_ordered <= 12:
                        break
                    else:
                        print ("Your order must be between 1-12")
                except ValueError:
                    print ("That was invalid")
                    print ("Your order must be between 1-12")
            items_ordered = items_ordered-1
            order_list.append(items[items_ordered])
            order_cost.append(item_prices[items_ordered])
            print ("{} ${:.2f}".format(items[items_ordered], item_prices[items_ordered]))
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
    # Parameter : del_pick / Delivery or Pickup 
    shipping_cost = 9 # Cost of shipping
    total_cost = sum(order_cost)
    print ("Your details")
    if del_pick == "pickup":
        print ("Your order is for pickup")
        print (f"Customer Name: {customer_details['name']} Customer Phone: {customer_details['phone']}")
        print ("---------------")
    elif del_pick == "delivery":
        print ("Your order is for delivery")
        print (f"Customer Name: {customer_details['name']} Customer Phone: {customer_details['phone']} Customer Address:{customer_details['house']}{customer_details['street']}{customer_details['suburb']}")
        print ("---------------")
        if value <= 4:
            total_cost = total_cost + shipping_cost


    # ADD ASCII FOR BELOW #
    print("Order details")
    count = 0 # Count is intially 0
    for item in order_list: # For every item in the list of items it prints them in 2dp 
        print ("---------------")
        print ("ordered: {} cost ${:.2f}".format(item, order_cost[count])) # Displays costs in 2dp along with formating it in item and their cost for that item
        count = count+1 # This is done so the list displays the items in correct order
    print ("---------------")
    print("total order cost")
    print (f"${total_cost:.2f}")
    return total_cost


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
    print ("---------------")
    print ("Please confirm your order")
    print ("To confirm please press 1")
    print ("If the order is incorrect please enter 2")
    print ("---------------")
    while True:
        try:
            confirm = int(input(("Please enter a number ")))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ("")
                    print (" ██████╗ ██████╗ ███╗   ██╗███████╗██╗██████╗ ███╗   ███╗███████╗██████╗ ██╗")
                    print ("██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔══██╗████╗ ████║██╔════╝██╔══██╗██║")
                    print ("██║     ██║   ██║██╔██╗ ██║█████╗  ██║██████╔╝██╔████╔██║█████╗  ██║  ██║██║")
                    print ("██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██╔══██╗██║╚██╔╝██║██╔══╝  ██║  ██║╚═╝")
                    print ("╚██████╗╚██████╔╝██║ ╚████║██║     ██║██║  ██║██║ ╚═╝ ██║███████╗██████╔╝██╗")
                    print (" ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝")
                    print("")
                    time.sleep(1)
                    print ("---------------")
                    print ("Order Confirmed")
                    print ("Your order has been sent to the shop")
                    print ("---------------")
                    new_exit()
                    break
                elif confirm == 2:
                    print ("")
                    print (" ██████╗ █████╗ ███╗   ██╗ ██████╗███████╗██╗     ██╗     ███████╗██████╗ ██╗")
                    print ("██╔════╝██╔══██╗████╗  ██║██╔════╝██╔════╝██║     ██║     ██╔════╝██╔══██╗██║")
                    print ("██║     ███████║██╔██╗ ██║██║     █████╗  ██║     ██║     █████╗  ██║  ██║██║")
                    print ("██║     ██╔══██║██║╚██╗██║██║     ██╔══╝  ██║     ██║     ██╔══╝  ██║  ██║╚═╝")
                    print ("╚██████╗██║  ██║██║ ╚████║╚██████╗███████╗███████╗███████╗███████╗██████╔╝██╗")
                    print (" ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝╚══════╝╚══════╝╚═════╝ ╚═╝")
                    print ("")
                    time.sleep(1)

                    print ("---------------")
                    print ("Order Cancelled")
                    print ("You can restart your order or exit")
                    print ("---------------")
                    new_exit()
                    break
            else:
                print ("Please enter a 1-2")
        except ValueError:
            print ("That input was invalid")
            print ("Please enter a 1-2")


# End ##################################################
########################################################
# Free shipping / Paid shipping ########################


def shipping():
    print ()
        



# End ##################################################
########################################################
# Main Def #############################################
# Creates most defs and uses them ######################


def main():
    welcome()
    del_pick = order_type()
    menu()
    value = order_item()
    print_order(del_pick, value)
    #shipping(del_pick)
    #print_order(del_pick)
    confirm_cancel()
main()


# End ##################################################
########################################################
