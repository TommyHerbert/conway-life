def spiral(start_x, start_y):
	visited = [(start_x, start_y), (start_x, start_y - 1)]
	for cell in visited:
		yield cell
	while True:
		visited.append(next_cell(tuple(visited)))
		yield visited[-1]


def next_cell(visited):
	XXXX
