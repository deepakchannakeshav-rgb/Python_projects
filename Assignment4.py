# For this exercise, you will create a program that approximates the number of miles per gallon that a car gets.

from random import randint



def miles_per_gallon(gallons,miles):
    print("miles per gallon", miles // gallons)

fuel= randint(10,25)
miles= randint(200,400)

print("no_of_gallons : "+ str(fuel)+ ", no_of_miles " + str(miles))

miles_per_gallon(fuel,miles)


# calculates and displays the MPG of the car assuming car manufacturers overestimates in their claims
print("The car can travel " + str(miles // fuel) + " miles per gallon.")
# displays the number of gallons of fuel that the car's fuel tank can hold
print("The car's fuel tank can hold " + str(fuel) + " gallons.")
# displays the number of miles that the car can travel on a full tank
print("The car can travel " + str(miles) + " miles on a full tank.")