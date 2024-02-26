colors = ['red', 'green', 'blue']
powers = []
def minimum_cubes(data):
    reds = []
    greens = []
    blues = []
    data = data.split(";")
    for game in data:
        game = game.split(",")
        for cube in game:
            if "red" in cube:
                cube = cube.strip("red")
                cube = cube.strip(" ")
                reds.append(int(cube))
            if "green" in cube:
                cube = cube.strip("green")
                cube = cube.strip(" ")
                greens.append(int(cube))
            if "blue" in cube:
                cube = cube.strip("blue")
                cube = cube.strip(" ")
                blues.append(int(cube))

    return max(reds), max(greens), max(blues)



def main():
    with open("puzzle_input.txt") as f:
        games = f.readlines()
        for game in games:
            game = game.replace("\n","")
            game = game.split(":")
            data = game[1]
            min_red, min_green, min_blue = minimum_cubes(data)
            powers.append(min_red*min_green*min_blue)
        print(sum(powers))

main()