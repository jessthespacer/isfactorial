with open("hugenumber.txt", "r+") as f:
	content = f.readlines()
	content = "".join(content)
	print(len(content))