with open("puzzle_input.txt", "r") as f:
    puzzle = f.read()
    special_chars = set()
    for char in puzzle:
        if not char.isnumeric():
            special_chars.add(char)
    special_chars.remove(".")
    # special_chars is now a set containing every special character in the field



def check_neigbours(x_start, x_end, y):
    pass