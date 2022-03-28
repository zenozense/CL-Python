menuList = []
priceList = []

def bill():
    name = "Summary"
    print("----",name,"----")
    for i in range(len(menuList)):
        print(str(i + 1) + ". " + menuList[i] + " Price " + str(priceList[i]))
    print("Total Price:", (priceList),"Bath")

while True:
    menu_Input = input("Please Enter Menu: ")
    if menu_Input.lower() == "exit":
        break
    else:
        price_Input = input("Price: ")
        menuList.append(menu_Input)
        priceList.append(price_Input)

print(menuList)
print(priceList)
bill()