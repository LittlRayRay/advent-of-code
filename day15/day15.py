def main():

	file = open("input.txt", "r").read().splitlines()
	print(file)

	mapping = {}

	for x, char in enumerate(file[0]):
		for y, line in enumerate(file):
			
			toappend = []

			if x - 1 > 0:
				toappend.append([x - 1, y])
			if x + 1 < len(file[y]) - 1:
				toappend.append([x + 1, y])
			if y - 1 > 0:
				toappend.append([x, y -1 ])
			if y + 1 < len(file) - 1:
				toappend.append([x, y + 1])

			mapping[x, y] = toappend

	print(mapping)


if __name__ == "__main__":
	main()