the_count = [1,2,3,4,5]
fruits = ["fruits", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

#This first kind of for_loop goes through a list
for number in the_count:
    print(f"This is the count {number}")

#same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#Also we can go through mixed lists too
#Notice we have to use {} since we do not know what's in it
for i in change:
    print(f"I got {i}")

#We can also build from empty lists
elements = []
for i in range(0,6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")
