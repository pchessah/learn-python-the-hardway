#DEFINING A FUNCTION CHEESE AND CRACKERS THAT TAKES TWO ARGUMENTS
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print(f"Man that is enough for a party")
    print("Get a blanket. \n")

print("We can just give the function numbers directly")
#CALLING THE FUNCTION WITH PARAMETERS DIRECTLY
cheese_and_crackers(20,30)

print("OR, we can use variables from our script: ")
#ASSIGNING VALUES TO VARIABLES
amount_of_cheese = 10
amount_of_crackers = 50

#CALLING THE FUNCTION WITH THE VARIABLES
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too!")
#DOING MATH IN THE ARGUMENTS WHEN CALLLING THE function
cheese_and_crackers(10+29, 56+67)


print("AND we can combine the two and use variables and math: ")
#COMBINING VARIABLES AND VALUES WHEN CALLING THE FUNCTION
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

