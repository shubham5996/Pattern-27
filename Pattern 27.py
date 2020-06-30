def make_matrix(number):
	global output, count
	side = 1 + (number-1)*2
	output = [[number]*side for x in range(side)]
	mid = side/2 + 1/2
	count = 0
	def do():
		global output, count
		new_list = []
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
		new_list += new_list[-2::-1]
		output = new_list
	
	for n in range(number):
		do()
		count+=1
	for x in output:
		print(' '.join([str(element) for element in x]))

make_matrix(7)

