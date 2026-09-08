#The formula for converting from degrees Celsius to degrees Fahrenheit is as follows:

#F = 1.8 * C + 32

degreeC= int(input("Please enter the degree Celcisus : "))

def calulate_Fahrenheit(str1):
    return (1.8 * str1+ 320) /10

print("The Fahrenheit equivalent of "+ str(degreeC) + " degrees Celsius is " + str(round(calulate_Fahrenheit(degreeC),2)))