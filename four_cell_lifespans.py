def solve():
    # try all patterns that fit in a 4x4 bounding box and have 4 live cells
    # could optimise for space here
    record = 0
    pattern_count = 0
    patterns = get_patterns(4, 4, 4)
    for pattern in patterns:
        lifespan = get_lifespan(pattern)
        pattern_count += 1
        if lifespan > record:
            print(f'new record: this pattern lasts for {lifespan} generations:')
            pretty_print(pattern)
            print(f'({pattern_count} pattern(s) checked so far)')
            record = lifespan
    print(f'done - {pattern_count} patterns checked')
    return record


def get_patterns(rows, columns, live_cells):
    dead_cells = rows * columns - live_cells
    for permutation in permutations(live_cells, dead_cells):
        pattern = []
        for i in range(rows):
            pattern.append(tuple(permutation[i * columns : i * columns + columns]))
        yield tuple(pattern)


def permutations(live_cells, dead_cells):
    if live_cells == 0:
        yield tuple([0] * dead_cells)
    elif dead_cells == 0:
        yield tuple([1] * live_cells)
    else:
        for i in range(dead_cells + 1):
            first_part = [0] * i + [1]
            for second_part in permutations(live_cells - 1, dead_cells - i):
                yield tuple(first_part + list(second_part))


def get_lifespan(pattern):
    if empty_pattern(pattern):
        return 0
    current_pattern = pattern
    trimmed_pattern = trim(current_pattern)
    previous_patterns = []
    while trimmed_pattern not in previous_patterns:
        previous_patterns.append(trimmed_pattern)
        current_pattern = successor(current_pattern)
        if empty_pattern(current_pattern):
            return len(previous_patterns)
        trimmed_pattern = trim(current_pattern)
    return previous_patterns.index(trimmed_pattern)


def empty_pattern(pattern):
    return not any([1 in row for row in pattern])


def trim(pattern):
    trimmed_pattern = pattern
    for row_index in [0, -1]:
        while 1 not in trimmed_pattern[row_index]:
            trimmed_pattern = remove_row(trimmed_pattern, row_index)
    for column_index in [0, -1]:
        while 1 not in [row[column_index] for row in trimmed_pattern]:
            trimmed_pattern = remove_column(trimmed_pattern, column_index)
    return trimmed_pattern


def remove_row(pattern, row):
    pattern_list = list(pattern)
    del pattern_list[row]
    return tuple(pattern_list)


def remove_column(pattern, column):
    new_pattern = []
    for row in pattern:
        row_list = list(row)
        del row_list[column]
        new_pattern.append(tuple(row_list))
    return tuple(new_pattern)


def successor(pattern):
    if reaches_edge(pattern):
        pattern = expand(pattern)
    new_pattern = []
    for y in range(len(pattern)):
        new_row = []
        for x in range(len(pattern[y])):
            live_neighbours = count_neighbours(pattern, x, y)
            new_row.append(1 if lives(pattern[y][x], live_neighbours) else 0)
        new_pattern.append(tuple(new_row))
    return tuple(new_pattern)


def reaches_edge(pattern):
    if 1 in pattern[0] or 1 in pattern[-1]:
        return True
    return 1 in [row[0] for row in pattern] or 1 in [row[-1] for row in pattern]


def expand(pattern):
    width = len(pattern[0]) + 2
    new_pattern = [tuple([0] * width)]
    for row in pattern:
        new_pattern.append(tuple([0] + list(row) + [0]))
    new_pattern.append(tuple([0] * width))
    return tuple(new_pattern)


def count_neighbours(pattern, x, y):
    neighbour_sum = 0
    for vector in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
        neighbour_x, neighbour_y = add_vector((x, y), vector)
        if exists(neighbour_x, neighbour_y, pattern):
            neighbour_sum += pattern[neighbour_y][neighbour_x]
    return neighbour_sum


def add_vector(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return x1 + x2, y1 + y2


def exists(x, y, pattern):
    if x < 0 or y < 0:
        return False
    return y < len(pattern) and x < len(pattern[0])


def lives(state, neighbours):
    if neighbours == 3: # birth/survival
        return True
    if neighbours == 2 and state == 1: # survival
        return True
    return False


def pretty_print(pattern):
    for row in pattern:
        for cell in row:
            print('⬜' if cell == 1 else '⬛', end='')
        print('\n')

if __name__ == '__main__':
    solve()
