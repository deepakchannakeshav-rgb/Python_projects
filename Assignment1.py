# A customer of a grocery store is purchasing 6 items. The names and prices of the items are as follows:
#
# Penne 16 oz Pack of 12 - $16.68
#
# Arrabiata Pasta Sauce 24 oz - $6.98
#
# Bag of 20 Organic Garlic Cloves - $16.78
#
# Italian Seasoning 1.5 oz Bottle - $15.26
#
# Artisan Baguettes Twin Pack - $3.00
#
# 12 oz Bag of Meatballs - $4.39
#
# In a .py file, write a program which calculates the subtotal of all 6 of these items using an expression.  The subtotal is just the sum of all of their prices.
#
# Use print() to display the result of the expression.

penne= 16.68 *100
attabiata = 6.98 * 100
cloves = 16.78 * 100
bottle = 15.26 *100
twin_pack = 3.00 * 100
meetball = 4.39 * 100

subtotal = (penne+attabiata+cloves+bottle+twin_pack+meetball) / 100

print(subtotal)

penne= 16.68
attabiata = 6.98
cloves = 16.78
bottle = 15.26
twin_pack = 3.00
meetball = 4.39

print(round(penne+attabiata+cloves+bottle+twin_pack+meetball, 2))

# In a .py file, create a program and use input() three times to get answers to the following questions from a user.  Store each of the answers in a variable.
#
# What is your name?
#
# What is your quest?
#
# What is your favorite color?
#
# Then, concatenate everything into a string within a print() statement with the form "So your name is [name], your quest is [quest], and your favorite color is [color]."

name = input("what is your name?")
quest = input("what is your quest?")
color = input("what is your color?")

print ("So your name is "+name +", your quest is "+quest+", and your favorite color is "+color+ "." )