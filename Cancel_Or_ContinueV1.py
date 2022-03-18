def confirm_cancel ():
    print ("Do you want to start another order?")
    print ("To start another order press 1")
    print ("To exit press 2")
    while True:
        try:
            confirm = int(input(("Please enter a number")))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ("New order") # USE ASCII
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear()
                    main()
                    break
                elif:
                    print ("Thanks for shopping with us!")
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear()
                    sys.exit()
                    break
            else:
                print ("Please enter a 1 or 2")
        except ValueError:
            print ("That input was invalid")
            print ("Please enter a 1-2")
