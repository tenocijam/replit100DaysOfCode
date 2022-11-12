# Day 20

print("List Generator")
print()

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
increment = int(input("Enter the increment between values: "))


for i in range(start, end+1, increment):
    print(i)
