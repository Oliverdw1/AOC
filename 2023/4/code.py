total_score = 0
matches = {}
def calculate_score(ls):
    score = 0
    for element in ls:
        if score == 0:
            score += 1
        else:
            score *= 2
    return score


with open('puzzle_input.txt') as f:
    puzzle_input = f.readlines()
    for line in puzzle_input:
        winners = []
        first_numbers = []
        second_numbers = []
        line = line.strip("Card ")
        line = line.split(':')
        index, numbers = line[0], line[1]
        numbers = numbers.split('|')
        winning_numbers, played_numbers = numbers[0], numbers[1]
        played_numbers = played_numbers.strip(" \n")
        winning_numbers = winning_numbers.strip(" ")
        first_numbers.extend(map(int, winning_numbers.split()))
        second_numbers.extend(map(int, played_numbers.split()))
        for number in second_numbers:
            if number in first_numbers:
                winners.append(number)

        matches[index] = winners


for key in matches:
    print(f"{key}: {matches[key]}")