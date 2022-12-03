# Day 41

print()

websites = {"name": None, "url": None, "desc": None, "rating": None}

for key in websites:
    websites[key] = input(f"{key.capitalize()}: ")

print()
print("-------------------------------------")
print()

for key, value in websites.items():
    print(f"{key}: {value}")