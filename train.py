import matplotlib.pyplot as plt
import numpy as np

file = open("./data.csv", 'r')

kmList = []
priceList = []

while True:
	line = file.readline()
	if not line: break
	lineList = line.split(',')
	if not (lineList[0].isdigit() or lineList[1].isdigit()) : 
		continue
	kmList.append(float(lineList[0]))
	priceList.append(float(lineList[1]))

length = len(kmList)

# # first case
# psi = 0
# alpha = 0
# beta = 0
# for i in range(0, length) :
# 	psi += kmList[i] ** 2
# 	alpha += kmList[i]
# 	beta += kmList[i] * priceList[i]
# psi *= (2 / length)
# alpha *= (2 / length)
# beta *= (2 / length)

# sigma = 0
# tau = 0

# for i in range(0, length) :
# 	sigma += (1 - (alpha / psi) * kmList[i]) ** 2
# 	tau += ((beta / psi) * kmList[i] - priceList[i]) * (1 - (alpha / psi) * kmList[i])

# sigma *= (2 / length)
# tau *= (2 / length)

# bias = -(tau / sigma)
# weight = (beta - alpha * bias) / psi
# # second case
# m = 0
# n = 0
# for i in range(0, length) :
# 	m += kmList[i]
# 	n += priceList[i]

# m *= (2 / length)
# n *= (2 / length)

# sigma = 0
# tau = 0

# for i in range(0, length) :
# 	sigma += (kmList[i] - (m / 2)) ** 2
# 	tau += ((n / 2) - priceList[i]) * (kmList[i] - (m / 2))

# sigma *= (2 / length)
# tau *= (2 / length)

# weight = -tau / sigma
# bias = (n - m * weight) / 2

# third case
psi = 0
alpha = 0
beta = 0
for i in range(0, length) :
	psi += kmList[i] ** 2
	alpha += kmList[i]
	beta += kmList[i] * priceList[i]
psi *= (2 / length)
alpha *= (2 / length)
beta *= (2 / length)

m = 0
n = 0
for i in range(0, length) :
	m += kmList[i]
	n += priceList[i]

m *= (2 / length)
n *= (2 / length)

sigma = 0
tau = 0

mat = np.array([[psi, alpha], [m, 2]])
inv = np.linalg.inv(mat)

weight = inv[0][0] * beta + inv[0][1] * n
bias = inv[1][0] * beta + inv[1][1] * n




text_file_path = './theta.txt'
new_text_content = ''
with open(text_file_path,'r') as f:
	lines = f.readlines()
	for i, l in enumerate(lines):
		if i == 0:
			new_string = str(bias)
		elif i == 1:
			new_string = str(weight)
		else:
			new_string = l.strip()
		
		if new_string:
			new_text_content += new_string + '\n'
		else:
			new_text_content += '\n'
				
with open(text_file_path,'w') as f:
	f.write(new_text_content)

print(np.polyfit(kmList, priceList, 1))

n1 = np.array(kmList)

t = np.arange(0., np.max(n1), 1)
plt.plot(kmList, priceList, 'ro')
plt.plot(t, weight * t + bias)
plt.ylabel('estimatePrice($)')
plt.xlabel('mileage(km)')
plt.show()
