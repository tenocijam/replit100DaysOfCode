# Day 21

print("Multiplication game")
print("I will ask you the multiplication table for the number you choose")

print()
num = int(input("Enter the number for which you want the multiplication table: "))

points = 0
for i in range(1, 11):
    print()
    ans = int(input(f"{num} x {i} = "))
    if ans == num*i:
        points += 1
        print("\033[32mThat's a correct answer!\033[0m")
    else:
        print("\033[31mOops, you got it wrong\033[0m")
        print("The correct answer is", num*i)
print()
print("You got", points, "out of 10.")
