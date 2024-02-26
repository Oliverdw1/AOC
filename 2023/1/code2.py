values = []

words = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}


with open('puzzle_input.txt', 'r') as f:
    l = f.readlines()
    for line in l:
        for word in words:
            line = line.replace(word, str(words[word]))
        numbers = []
        for char in line:
            if char.isnumeric():
                char = int(char)
                numbers.append(char)
        if len(numbers) == 1:
            values.append(11 * numbers[0])
        if len(numbers) >= 2:
            values.append(10 * numbers[0] + numbers[-1])
        print(line.strip("\n") , values[-1])


    print(values)
    print(sum(values))