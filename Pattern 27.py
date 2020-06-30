# The function which makes and prints the matrix
def make_matrix(number):
	global output, count
	# Determining number of sides
	side = 1 + (number-1)*2
	# Creating a skeleton matrix with the given number as every element
	output = [[number]*side for x in range(side)]
	# Determining where to stop after building half the matrix
	mid = side/2 + 1/2
	count = 0
	def do():
		global output, count
		new_list = []
		# alters the skeletal matrix to assign values as needed
		for a,row in enumerate(output, 0):
			rows = []
			if a == (side/2 + 1/2):
				break
			for b,element in enumerate(row, 0):
				if a < count or b < count or b > len(row)-(count+1):
					rows.append(element)
				elif b == count or a == count or b == len(row)-(count+1):
					rows.append(number-count)
				else:
					rows.append(number)
			new_list.append(rows)
		# makes a final matrix by adding half the list to itself
		new_list += new_list[-2::-1]
		output = new_list
	# increases count to change values as you move towards center
	for n in range(number):
		do()
		count+=1
	# prints matrix in a readable format
	for x in output:
		print(' '.join([str(element) for element in x]))

make_matrix(7)

