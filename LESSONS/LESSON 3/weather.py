temp = int(input("enter your city temperature:"))
if temp>32:
    print("sunny")

elif temp>20 and temp<30:
    print("rainy")

elif temp>10 and temp<20:
    print("cold")

else:
    print("very chilled")