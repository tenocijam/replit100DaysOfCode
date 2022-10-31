# Day 8

print("Hey there, Welcome to your daily affirmation generator")
name = input("What is your name? ")


if name =="Mark" or name == "mark":
 dow = input("What is the day of the week? ")
 if dow == "monday" or dow == "Monday":
   print("I hope its a great Monday for you", name)
 if dow == "tuesday" or dow == "Tuesday":
   print("You are doing a great job", name, "keep going!")
 if dow == "wednesday" or dow == "Wednesday":
   print("Happy wednesday", name)
 if dow == "thursday" or dow == "Thursday":
   print("You are nearing your weekend,", name)
 if dow == "friday" or dow == "Friday":
   print("Happy weekend,", name)

elif name == "David" or name== "david":
 dow = input("What is the day of the week? ")
 if dow == "monday" or dow == "Monday":
   print("I hope its a great Monday for you", name)
 if dow == "tuesday" or dow == "Tuesday":
   print("You look great in that color", name)
 if dow == "wednesday" or dow == "Wednesday":
   print("You look chipper today", name)
 if dow == "thursday" or dow == "Thursday":
   print("You are nearing your weekend", name)
 if dow == "friday" or dow == "Friday":
   print("Happy weekend", name)
else:
 print("I do not know your name, but I hope you are having a great day!")