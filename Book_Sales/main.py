bookName = input("Enter Book Title: ")
price = float(input("Enter Price $: "))
qty = float(input("Enter Quantity: "))

amt = price * qty
print("The Total Amount for "+bookName+ "=","$", amt)

if(amt >= 10000):
    discount = 20
elif(amt >= 5000 and amt<=9999):
    discount = 10
else:
    discount = 5

    disAmt = (amt * discount)/100
    totalAmt = amt - disAmt

    print("Discount = %d%% and Discount Amount = $%.2f"%(discount, disAmt))

    print ("Book price after discounted = " + "$",totalAmt)