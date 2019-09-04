#1
bill = int(input("Total bill amount? "))
tip = str(input("Level of service? "))

if tip =="good":
    tipamount = bill * .2
    print("Tip amount: " + str(tipamount))
elif tip =="fair":
    tipamount = bill * .15
    print("Tip amount: " + str(bill * .15))
elif tip == "bad":
    tipamount = bill * .1
    print("Tip amount: $" + str(bill * .1))

total = tipamount + bill
print("Your total is: $" + str(total))

#2
#will add comments above to show which is from part 2
