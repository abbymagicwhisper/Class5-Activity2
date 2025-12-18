CostPrice = int(input("Enter the cost of your item: "))
SellingPrice = int(input("Enter the selling price of your item:"))

if CostPrice > SellingPrice:
    print("You have had a loss on your item")
    print("The loss amount is ", CostPrice - SellingPrice)
    print("The loss percentage on this item is ", ((CostPrice - SellingPrice) / CostPrice) * 100)

else:
    print("You have made a profit on this item")
    print("The profit amount is ", SellingPrice - CostPrice)
    print("The  profit percentage on this item is ", ((SellingPrice - CostPrice) / CostPrice) * 100)




