money = int(input())
d = {23: "chicken", 678: "goat", 1296: "pig", 3848: "cow", 6769: "sheep"}
low_animal = "None"
price = 0
for key in d.keys():
    if money >= key:
        low_animal = d[key]
        price = key
if low_animal != "None":
    res = money // price
    print(res, low_animal if res == 1 or low_animal == "sheep" else low_animal + "s")
else:
    print("None")
