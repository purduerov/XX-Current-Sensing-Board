#This code calculates the expected voltages gernerated
#from a voltage divider using a thermistor.  These vlaues
#change as the temperature changes


from math import exp


#Basic temperature conversions
def fToC(temp):
    return ((temp - 32) * (5 / 9))

def cToF(temp):
    return((temp * (9/5)) + 32)

def fToK(temp):
    return (fToC(temp) + 273.15)

def kToF(temp):
    return (cToF(temp - 273.15))

#Calculates the resistance of the thermistor based on the temperature (in Kelvin)
#temp - the temperature of the thermistor
def calculateResistance(temp, standRes=3300,B=4500, standTemp=298.15):

    #Formula given from the data sheet of the thermistor
    exponentialTerm = B * ((1 / temp) - (1 / standTemp))

    #Calculate the new resistance for the thermistor
    thermRes = standRes * exp(exponentialTerm)

    return thermRes

#Does voltage division to calculate the voltage between the two resistors
#resFirst - resistor closest to the voltage source
#resSecond - resistor closest to ground
def calculateVoltageOut(vIn, resFirst, resSecond):

    current = vIn / (resFirst + resSecond) # I = V / R
    vOut = current * resSecond #V = I * R
    return vOut


if __name__ == "__main__":

    fixedRes = 1000

    vIn = 5

    lowerTemp = 70.0

    upperTemp = 90.0

    tempStep = 0.1

    #range is stupid when it comes to stepping with float values
    for i in range(int(lowerTemp / tempStep), int(upperTemp / tempStep), int(tempStep / tempStep)):

        fTemp = round(i * tempStep, 2)
        kTemp = fToK(fTemp)
        thermRes = calculateResistance(kTemp, 1000)

        vOut = calculateVoltageOut(vIn, fixedRes, thermRes)

        print("Temp [F] = {0:3} : Temp [K] = {1:8f} : Resistance [ohms] = {2:8f} : Voltage Out [V] = {3:8f}".format(round(fTemp, 4), round(kTemp, 4), round(thermRes, 4), round(vOut, 4)))
