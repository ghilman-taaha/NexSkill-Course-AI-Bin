print(" Arthemtic Operations")
ProductSale = 50.5
ProductProfit= 5

if ProductSale > 200:
    print("Geater than 200..................1")
    print("Geater than 200..................2")
    print("Geater than 200..................3")
elif ProductProfit < 10:
    print(" profit lesss then 10.......1")
    print(" profit lesss then 10.......2")
    print(" profit lesss then 10.......3")
elif ProductProfit < 3:
    print(" Profit less then 3..........1")
    print(" Profit less then 3..........2")
    print(" Profit less then 3..........3")
elif ProductProfit < 2:
    print("Profit less then 2......1")
    print("Profit less then 2......2")
    print("Profit less then 2......2")
else:
    print(" What ever.......1")
    print(" What ever.......2")
    print(" What ever.......3")

ProductProfitAdd = ProductProfit + 5
ProductProfitSub = ProductProfit - 5
ProductProfitMul = ProductProfit * 5
ProductProfitDiv = ProductProfit / 5
ProductProfitFloorDive = ProductProfit // 5
ProductProfitPower = ProductProfit ** 5
ProductProfitModu = ProductProfit % 5

print("+", ProductProfitAdd)
print("-", ProductProfitSub)
print("*", ProductProfitMul)
print("/", ProductProfitDiv)
print("//",ProductProfitFloorDive)
print("**", ProductProfitPower)
print("%",ProductProfitModu)
