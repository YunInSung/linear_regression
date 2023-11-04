import sys

if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()

if sys.argv[1].isdigit() == False :
	print("Wrong argument")
	sys.exit()
    

mileage = float(sys.argv[1])

file = open("./theta.txt", 'r')

theta0 = float(file.readline())
theta1 = float(file.readline())

print("estimatePrice :", theta1 * mileage + theta0)
