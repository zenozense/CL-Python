price = int(input("Enter Price: "))
def vatCal(price):
    result = price+(price*7/100)
    return result

print("Total Vat Incl. :",vatCal(price))