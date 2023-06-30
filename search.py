def spiral(start_x, start_y):
    visited = [(start_x, start_y), (start_x, start_y - 1)]
    for cell in visited:
        yield cell
    while True:
        visited.append(next_cell(tuple(visited)))
        yield visited[-1]


def next_cell(visited):
    current = visited[-1]
    vectors = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    north, east, south, west = [add_vector(current, v) for v in vectors]
    if south in visited:
        if east in visited:
            
