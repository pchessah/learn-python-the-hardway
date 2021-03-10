people = 30
cars = 20
trucks = 195

if cars > people:
    print("We should take cars")
elif cars <people:
    print("We should not take cars")
else:
    print("Ww cant decide")

if trucks > cars:
    print("That's too many trucks")
elif trucks < cars:
    print("Take the trucks")
else:
    print("We cant decide")

if people > trucks:
    print("Alright, let's take the trucks")
    
else:
    print("Let's stay home")