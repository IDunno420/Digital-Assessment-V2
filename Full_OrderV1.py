######################################################
# Create List of Items ###############################
# 12 Items With differing prices #####################
# Item List   #
items = ['Mouse','Gaming Mouse','Keyboard','Gaming Keyboard'
        ,'Standard PC','Buiness PC','Editing PC',
        'Gaming PC','Laptop','Buiness Laptop','Editing laptop',
        'Gaming laptop',]
# Item Prices #
item_prices = [15,30,20,50,150,250,325,500,150,225,275,500]
# End ################################################
######################################################
# Create Customer Dictonary ##########################
customer_details = {}
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
    # End ######

    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])
    print ("")

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])
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
    # End ######

    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])
    print ("")


    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])
    print ("")


    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house'])
    print ("")

    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question)
    print (customer_details['street'])
    print ("")

    question = ("Please enter your suburb ")
    customer_details['suburb'] = not_blank(question)
    print (customer_details['suburb'])
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
    return del_pick

## Using Def ##
order_type()
## End ########

# End ##################################################
########################################################
# Item Def #############################################
# Prints the list of items in a neat vertical list #####
def menu():
    number_pizza = 12
    for count in range (number_pizza) :
        print ("----------------")
        print (count+1, items[count],item_prices[count])
menu()
# End ##################################################
########################################################