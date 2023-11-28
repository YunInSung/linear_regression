import sys
if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()

partition = sys.argv[1].partition(".")
if not (sys.argv[1].isdigit() or ((partition[0].isdigit() and partition[1] == "." and partition[2].isdigit())
        or (partition[0] == "" and partition[1] == "." and partition[2].isdigit())
        or (partition[0].isdigit() and partition[1] == "." and partition[2] == ""))):
	print("Wrong argument")
	sys.exit()

mileage = float(sys.argv[1])

file = open("./theta.txt", 'r')

theta0 = float(file.readline())
theta1 = float(file.readline())

print("estimatePrice :", theta1 * mileage + theta0)
