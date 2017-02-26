def isFactorial(n, i = 1):
	# base case
	if n == i:
		return i
	# recursive case
	elif n % i == 0:
		return isFactorial(n/i, i + 1)
	else:
		return -1

print(isFactorial(1124000727777607680000))