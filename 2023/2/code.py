red_cubes = 12
green_cubes = 13
blue_cubes = 14
indeces = []


def cube_count(data):
    data = data.split(";")
    for game in data:
        game = game.split(",")
        for cube in game:
            if "red" in cube and int(cube.strip("red")) > red_cubes:
                return False
            if "blue" in cube and int(cube.strip("blue")) > blue_cubes:
                return False
            if "green" in cube and int(cube.strip("green")) > green_cubes:
                return False
    return True


def main():
    with open("puzzle_input.txt") as f:
        games = f.readlines()
        for game in games:
            game = game.replace("\n","")
            game = game.strip("Game ")
            game = game.split(":")
            index = int(game[0])
            data = game[1]
            if cube_count(data):
                indeces.append(index)
        print(indeces)
        print(sum(indeces))

main()