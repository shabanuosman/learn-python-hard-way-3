def cheese_and_cracker(cheesecount ,box_of_crackers):
   print(f"you have {cheesecount} cheeses")
   print(f"you have {box_of_crackers} cracker")


print("we give just function number directly:")
cheese_and_cracker(20,50)

print("OR We can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_cracker(amount_of_cheese,amount_of_crackers)

print("we can do math too")
cheese_and_cracker(10+40, 56+98)

print("we can do variable and math")
cheese_and_cracker( amount_of_cheese+10,amount_of_crackers+50)
