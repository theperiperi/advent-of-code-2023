def parse_game_strings(game_strs):
    games = []

    for game_str_list in game_strs:
        game = []

        for game_str in game_str_list:
            sets = game_str.split(';')
            cube_dict_list = []

            for set_str in sets:
                cubes = set_str.strip().split(',')
                cube_dict = {}

                for cube in cubes:
                    parts = cube.strip().split()
                    color = parts[1].lower() if len(parts) > 1 else parts[0].lower()
                    count = int(parts[0]) if len(parts) > 1 else 1

                    cube_dict[color] = count

                cube_dict_list.append(cube_dict)

            game.append(cube_dict_list)

        games.append(game)

    return games

def is_game_possible(game, red, green, blue):
    for set_of_cubes in game:
        red_count = green_count = blue_count = 0

        for cube_dict in set_of_cubes:
            for color, count in cube_dict.items():
                if color == 'red':
                    red_count += count
                elif color == 'green':
                    green_count += count
                elif color == 'blue':
                    blue_count += count

            if red_count > red or green_count > green or blue_count > blue:
                return False

    return True

def possible_games_sum(red, green, blue, *games):
    possible_games = [i + 1 for i, game in enumerate(games) if is_game_possible(game, red, green, blue)]

    return possible_games

red_cubes = 12
green_cubes = 13
blue_cubes = 14

games_list=[]
for i in range(100):
    game=input()
    if i<8:
        game=game[8:]
    else:
        game=game[9:]
    game=game.split("; ")
    games_list.append(game)

games = parse_game_strings(games_list)
result = possible_games_sum(red_cubes, green_cubes, blue_cubes, *games)
print(f"The possible games are: {result}")
print(f"The sum of their IDs is: {sum(result)}")
