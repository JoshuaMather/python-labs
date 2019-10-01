def printState():
    print ("Red Light is " + str(redLight))
    print ("Yellow Light is " + str(yellowLight))
    print ("Green Light is " + str(greenLight))
    print(int(3)+5)
redLight = True
yellowLight = False
greenLight = False

printState()
print(type(redLight))

x = 10
y = 20.0
z = 1j

print(type(x), type(y), type(z))

day = "Beautiful"
print(day[1])
print(day[0:5])
print(day[-3])
print(day[-3:])
print(day[-5:3])
print(day[-5:-3])

#day == "Beautiful"
#print("Today is " + day)
#print(str(day == "Beautiful") + ": Today is " + day)
operand1 = input("Input a number: ")
print("You entered " + operand1)
