count = 0
print("You have 0 coins.")
coin = "yes"
while coin == "yes":
    coin = input("Do you want a coin?")
    if coin == "yes":
        count += 1
        print("You have " + str(count) + " coins.")
    # else:
    