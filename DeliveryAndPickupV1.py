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
# Pickup Info Entering ##############################
def pickup_info():
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
# End ##################################################
########################################################