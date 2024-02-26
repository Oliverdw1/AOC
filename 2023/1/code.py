values = []

with open('puzzle_input.txt', 'r') as f:
    l = f.readlines()
    for line in l:
        numbers = []
        for char in line:
            if char.isnumeric():
                char = int(char)
                numbers.append(char)
        if len (numbers) == 1:
            values.append(11*numbers[0])
        if len (numbers) >= 2:
            values.append(10*numbers[0] + numbers[-1])
    print(values)
    print(sum(values))