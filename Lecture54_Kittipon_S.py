def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Login Success!")
        showMenu()
    else:
        print("Error, Try it agian.")
        return login()

def showMenu():
    print("----- ZenX Service -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input("Select: "))
    if userSelected == 1:
        return vatCalculator()
    elif userSelected == 2:
        return priceCalculator()
    else:
        return showMenu()

def vatCalculator():
    totalPrice = int(input("Price: "))
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    print("Total Vat Incl. : ",result)
    return showMenu()

def priceCalculator():
    a = int and float(input("1st Number: "))
    b = int and float(input("2nd Number: "))
    print("---------- Calculator ----------")
    print("(", a, ")", "Add (+)", "(", b, ")", "=", a + b)
    print("(", a, ")", "Subtract (-)", "(", b, ")", "=", a - b)
    print("(", a, ")", "Multiply (x)", "(", b, ")", "=", a * b)
    print("(", a, ")", "Divide (/)", "(", b, ")", "=", a / b)
    return showMenu()

print(login())