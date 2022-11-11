# Day 19

print("Loan calculator")

amount = 1000
new_amount = 1000
apr = 0.05

print()
print("Amount:", amount)
print("APR: ", apr*100, "%", sep="")
print()

for i in range(10):
    new_amount += (apr * new_amount)
    print("Year", i+1, ":", round(new_amount, 2))

print("You owe", round(new_amount - amount, 2), "extra")