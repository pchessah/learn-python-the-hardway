formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter.format("cows", "cows", "cows", "cows",), formatter.format(
    "cows", "cows", "cows", "cows",), formatter.format("cows", "cows", "cows", "cows",), formatter.format("cows","cows","cows","cows",)))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
