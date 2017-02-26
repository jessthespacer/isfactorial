from time import sleep

def isFactorial(n, i = 1):
	# base case
	if n == i:
		return i
	# recursive case
	elif n % i == 0:
		return isFactorial(n/i, i + 1)
	else:
		return -1

product = 1
i = 1
while True:
	print(product)
	#sleep(0.5)
	i += 1
	product *= i