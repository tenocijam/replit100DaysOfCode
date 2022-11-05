# Day 13

print()
print("Welcome to your Grade Generator")
print()

test_name = input("Enter the name of your test: ")
max_marks = int(input("Enter the maximum marks of the test: "))
user_marks = int(input("Enter the marks you scored: "))

percentage = round((user_marks / max_marks) * 100)

if percentage >=90 and percentage <= 100:
    grade = "A+"
elif percentage >=80 and percentage <= 89:
    grade = "A"
elif percentage >= 70 and percentage <=79:
    grade = "B"
elif percentage >= 60 and percentage <= 69:
    grade = "C"
elif percentage >= 50 and percentage <= 59:
    grade = "D"
else:
    grade = "U"

print("You have got ", percentage, "% ", "and your grade is ", grade, sep="")