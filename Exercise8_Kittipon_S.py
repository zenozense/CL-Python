print("Welcome, Please enter your username and password!")

usenameInput = input("Username: ")
passwordInput = input("Password: ")
if usenameInput == "admin" and passwordInput == "1234":
    print("Success!")
    if True:
        print("----------- Zee Store -----------")
        print(''' What's you want?
        1. Vandal   (2900)
        2. Phantom  (2900)
        3. Odin     (3200)
        4. Operator (4900)
        ''')
        addtochart = int(input("Select Number: "))
        if addtochart == 1:
            productname = "Vandal"
            productprice = 2900
        elif addtochart == 2:
            productname = "Phantom"
            productprice = 2900
        elif addtochart == 3:
            productname = "Odin"
            productprice = 3200
        elif addtochart == 4:
            productname = "Operator"
            productprice = 4900
        print("---------- Calculator ----------")
        print("Product you selected: ", productname)
        qty = int(input("Quantity: "))
        print("Summary: ",productprice*qty, "Bath")
else:
    print("The Password is incorrect!")