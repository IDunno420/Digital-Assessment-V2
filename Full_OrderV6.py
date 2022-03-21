######################################################

# Starting Infomation #
# Every component to this code is split using the 
# hash tag wall e.g. ↧↧↧
######################################################
# This is to make less buildup in the folder
# All changes can be seen through the 
# "Full_Order" versions 

######################################################
# Create List of Items ###############################
# 12 Items With differing prices #####################
# Item List   #
items = ['Mouse','Gaming Mouse','Keyboard','Gaming Keyboard'
        ,'Standard PC','Buiness PC','Editing PC',
        'Gaming PC','Laptop','Buiness Laptop','Editing laptop',
        'Gaming laptop',]
# Item Prices #
item_prices = [15,30,20,50,150,250,325,500,150,225,275,500,]
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
def not_blank(question):
    valid = False
    while not valid:
        responce = input(question)
        if responce != "":
            return responce.title()
        else:
            print ("This cannot be blank")
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
    print ("__________.__        __                                .__                 __             .___")
    print ("\______   \__| ____ |  | ____ ________     ______ ____ |  |   ____   _____/  |_  ____   __| _/")
    print (" |     ___/  |/ ___\|  |/ /  |  \____ \   /  ___// __ \|  | _/ __ \_/ ___\   __\/ __ \ / __ | ")
    print (" |    |   |  \  \___|    <|  |  /  |_> >  \___ \\  ___/|  |_\  ___/\  \___|  | \  ___// /_/ | ")
    print (" |____|   |__|\___  >__|_ \____/|   __/  /____  >\___  >____/\___  >\___  >__|  \___  >____ | ")
    print ("                  \/     \/     |__|          \/     \/          \/     \/          \/     \/ ")
    print ("")
    print ("###########################################################################################################")
    time.sleep(1)
    # End ######

    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    #print (customer_details['name'])
    print ("")

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    #print (customer_details['phone'])
    print (customer_details)
    print ("")
# End ################################################
######################################################
# Delivery Info Entering #############################
def delivery_info():

    # Aesthetics
    print ("###########################################################################################################")
    print ("")
    print ("________         .__  .__                                          .__                 __             .___")
    print ("\______ \   ____ |  | |__|__  __ ___________ ___.__.   ______ ____ |  |   ____   _____/  |_  ____   __| _/")
    print (" |    |  \_/ __ \|  | |  \  \/ // __ \_  __ <   |  |  /  ___// __ \|  | _/ __ \_/ ___\   __\/ __ \ / __ | ")
    print (" |____/   \  ___/|  |_|  |\   /\  ___/|  | \/\___  |  \___ \\  ___/|  |_\  ___/\  \___|  | \  ___// /_/ | ")
    print ("/_______  /\___  >____/__| \_/  \___  >__|   / ____| /____  >\___  >____/\___  >\___  >__|  \___  >____ | ")
    print ("        \/     \/                   \/       \/           \/     \/          \/     \/          \/     \/ ")
    print ("")
    print ("###########################################################################################################")
    time.sleep(1)
    # End ######
    # All #'s are for debugging #

    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    #print (customer_details['name'])
    print ("")


    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    #print (customer_details['phone'])
    print ("")


    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)
    #print (customer_details['house'])
    print ("")

    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question)
    #print (customer_details['street'])
    print ("")

    question = ("Please enter your suburb ")
    customer_details['suburb'] = not_blank(question)
    #print (customer_details['suburb'])
    print (customer_details)
# End ##################################################
########################################################
# User Picking Delivery or Pickup ######################
def order_type():
    del_pick = ""
    print ("Is your oder for pickup or delivery?")
    print ("For pickup enter 1")
    print ("For delivery enter 2")
    while True:
        try:
            delivery = int(input("Please enter 1 or 2 "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Pickup selected")
                    pickup_info()
                    del_pick = "pickup"
                    break
                elif delivery ==2:
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
    number_pizza = 12

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

    for count in range (number_pizza) :
        print ("----------------")
        print (count+1, items[count],item_prices[count])

# End ##################################################
########################################################
# Ordering Items #######################################
# Where the user picks items they want to order and ####
# how many things they want to order ###################
def order_item():
    num_items = 0
    while True:
        try:
            num_items = int(input("How many items do you want to order?"))
            if num_items >= 1 and num_items <= 5:
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
                    items_ordered = int(input("Please choose your items by entering the number from the menu"))
                    if items_ordered >= 1 and items_ordered <= 12:
                        break
                    else:
                        print ("Your order must be between 1-12")
                except ValueError:
                    print ("That was invalid")
                    print ("Your order must be between 1-12")
            items_ordered = items_ordered -1
            order_list.append(items[items_ordered])
            order_cost.append(item_prices[items_ordered])
            print ("{} ${:.2f}".format(items[items_ordered],item_prices[items_ordered]))
            num_items = num_items -1

# End ##################################################
########################################################
# Order Print Out ######################################

def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print ("Your details")
    if del_pick == "pickup":
        print ("Your order is for pickup")
        print (f"Customer Name: {customer_details['name']} /nCustomer Phone: {customer_details['phone']}")
    elif del_pick == "delivery":
            print ("Your order is for delivery")
            print (f"Customer Name: {customer_details['name']} /nCustomer Phone: {customer_details['phone']} /ncustomer Address:{customer_details['house']}{customer_details['street']}{customer_details['suburb']}")
    print()
    print("Order details")
    count = 0
    for item in order_list:
        print ("ordered: {} cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("total order cost")
    print (f"${total_cost:.2f}")

# End ##################################################
########################################################
########################################################
# Welcome Def ##########################################
# Includes Welcome #####################################
# Uses random name Generator ###########################

# Random name Generator #
import time
import random
from random import randint
names = ["Mark","Pheobe","Sally","Micheal","Denise","Jack","William","Afton","Lara",]   
# End #

def welcome():
    num = randint (0,9)
    name = (names[num])
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
    time.sleep(1)
    print("My name is",name,)
    print("I will be here to help you order with us")

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
            if reopen >= 1 and reopen <= 2:
                if reopen == 1:

                    print ("███╗   ██╗███████╗██╗    ██╗     ██████╗ ██████╗ ██████╗ ███████╗██████╗ ")
                    print ("████╗  ██║██╔════╝██║    ██║    ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
                    print ("██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║█████╗  ██████╔╝")
                    print ("██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔══██╗██║  ██║██╔══╝  ██╔══██╗")
                    print ("██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║")
                    print ("╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝")
                    time.wait(1)
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear()
                    main()
                    break
                elif reopen == 2:
                    print ("Thanks for shopping with us!")
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear()
                    exit()
                    break
            else:
                print ("Please enter a 1 or 2")
        except ValueError:
            print ("That input was invalid")
            print ("Please enter a 1-2")

# End ##################################################
########################################################
# Confirm order ########################################

def confirm_cancel():
    # Add ASCII
    print ("")
    print ("Please confirm your order")
    print ("To confirm please press 1")
    print ("If the order is incorrect please enter 2")
    while True:
        try:
            confirm = int(input(("Please enter a number ")))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:

                    print (" ██████╗ ██████╗ ███╗   ██╗███████╗██╗██████╗ ███╗   ███╗███████╗██████╗ ██╗")
                    print ("██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔══██╗████╗ ████║██╔════╝██╔══██╗██║")
                    print ("██║     ██║   ██║██╔██╗ ██║█████╗  ██║██████╔╝██╔████╔██║█████╗  ██║  ██║██║")
                    print ("██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██╔══██╗██║╚██╔╝██║██╔══╝  ██║  ██║╚═╝")
                    print ("╚██████╗╚██████╔╝██║ ╚████║██║     ██║██║  ██║██║ ╚═╝ ██║███████╗██████╔╝██╗")
                    print (" ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝")
                    time.wait(1)
                    
                    print ("Order Confirmed")
                    print ("Your order has been sent to the shop")
                    new_exit()
                    break
                elif confirm ==2:

                    print (" ██████╗ █████╗ ███╗   ██╗ ██████╗███████╗██╗     ██╗     ███████╗██████╗ ██╗")
                    print ("██╔════╝██╔══██╗████╗  ██║██╔════╝██╔════╝██║     ██║     ██╔════╝██╔══██╗██║")
                    print ("██║     ███████║██╔██╗ ██║██║     █████╗  ██║     ██║     █████╗  ██║  ██║██║")
                    print ("██║     ██╔══██║██║╚██╗██║██║     ██╔══╝  ██║     ██║     ██╔══╝  ██║  ██║╚═╝")
                    print ("╚██████╗██║  ██║██║ ╚████║╚██████╗███████╗███████╗███████╗███████╗██████╔╝██╗")
                    print (" ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝╚══════╝╚══════╝╚═════╝ ╚═╝")
                    time.wait(1)

                    print ("Order Cancelled")
                    print ("You can restart your order or exit")
                    new_exit()
                    break
            else:
                print ("Please enter a 1-2")
        except ValueError:
            print ("That input was invalid")
            print ("Please enter a 1-2")

# End ##################################################
########################################################
# Main Def #############################################
# Creates most defs and uses them ######################

def main():
    welcome()
    del_pick=order_type()
    menu()
    order_item()
    print_order(del_pick)
    confirm_cancel()
main()

# End ##################################################
########################################################