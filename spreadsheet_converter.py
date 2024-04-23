import csv

# push day data pasted straight from my notes app, warts and all
bench_data = """
4/18/2024
Bench: 135x13, 135x7, 135x7
Dips: 15, 10, 10
Tricep pull-down: 110x11, 110x60


4/14/2024
Bench: 135x13, 135x10, 135x8
Incline dumbbell press:  45x11, 42.5x15, 42.5x13
Chest flys: 100x7, 85x7, 70x9
Tricep pull-down: 110x16, 110x13, 110x9
Dips: 8, 8, 6
Single arm Tricep pull-down: 20x20, 30x6, 20x



4/9/2024
Bench:135x12, 135x9, 135x8
Incline dumbbell press: 42.5x17, 42.5x13, 42.5x8
Machine press: 6thx14, 6thx10, 6thx14
Tricep pull-down: 100x14, 100x10, 100x10
Dips: 8, 5
Single arm pull downs: 30x10, 20x14, 20x9



4/6/2024
Bench: 135x12, 135x10, 135x8
Dips: 10, 8, 8
Incline dumbbell press: 40x17, 40x13, 40x12
Tricep pull-down: 110x14, 110x11, 110x7
Tricep concentration: 45x17, 45x13, 45x


 
4/3/2024
Bench: 135x11, 135x10, 135x6
Incline dumbbell press: 42.5x16, 42.5x10, 42.5x


3/30/2024
Bench: 135x11, 135x10, 135x6
Incline dumbbell press: 

3/24/2024
Bench: 135x12, 135x10, 135x7
Incline dumbbell press: 42.5x15, 42.5x11, 42.5x10
Machine press: 


3/21/2024
Bench: 135x12, 135x10, 135x6
Incline dumbbell press: 42.5x14, 42.5x11, 42.5x8
Machine press: 6thx13, 6thx



3/16/2024
Bench: 135x12, 135x9, 135x6
Incline dumbbell press: 42.5x14, 42.5x11, 42.5x8
Machine press: 6thx13, 6thx


3/13/2024
Bench: 135x9, 135x8, 125x11
Incline dumbbell press: 42.5x14, 42.5x13, 42.5x11
Machine press: 105x11, 105xa lot, 125x a lot
Tricep pull-down: 110x7, 100x14, 100x12
Tricep concentration: 45x16, 45x12, 45x






3/10/2024
Bench: 135x10, 135x7, 125x9
Incline dumbbell press: 42.5x14, 42.5x12, 42.5x?
Cable flys: 17x?, x3
Tricep pull-down: 110x14, 110x9, 100x7
Assisted dips: 45lbsx14, 30lbsx12, 30lbsx9
Tricep concentration: 42.5x14, 42.5x13, 42.5x


3/7/2024
Bench: 135x10, 135x6, 115x14
Incline dumbbell press: 40x15, 40x12, 40x10
Machine press: 7thx12, 6thx12, 6thx11
Tricep pull-down: 120x8, 110x12, 100x14
Tricep concentration: 45x15, 45x11, 45x12
Assisted dip: 3?(0)x11, 3?(0)x12, 3?(0)x8



3/4/2024
Bench: 125x13, 125x11, 125x8
Incline dumbbell press: 40x15, 40x10, 40x10
Machine press: 7thx11, 6thx16(?), 6thx10
Tricep concentration: 45x20, 45x12, 45x13
Tricep pull-down: 110x10, 100x12, 100x11
Assisted pull-up: 3?(0)x12, 3?(0)x10, 3?(0)x8





3/1/2024
Bench: 125x12, 125x8, 115x12
Incline dumbbell press: 40x13.5, 40x9, 40x10
Machine press: 6thx15, 6thx10, 6thx10
Tricep concentration: 45x?, 45x12, 45x11
Tricep pull-down: 120x5, 100x12, 100x8
Assisted dips: 3?(1)x12, 3?(1)x10, 3?(2)x11



2/27/2024
Bench:125x10, 115x13, 115x11
Incline dumbbell press: 40x12, 40x10, 40x10
Machine press: 5thx15, 5thx12, 5thx12
Tricep pull-down: 110x8, 100x16, 100x10
Tricep concentration: 40x17, 40x14, 40x17
Assisted dip: 3?(2)x12, 3?(2)x11, 3?(2)x10




2/24/2024
Bench: 125x12, 115x12, 115x10
Incline dumbbell press: 40x13, 40x10, 40x


2/19/2024
Bench: 125x12, 115x13, 115x9
Incline dumbell press: 40x12, 40x8, 37.5x10
Dips: 7, 6, 6
Tricep pulldown: 110x10, 100x13, 100x8



2/15/2024
Bench: 115x12, 115x12, 115x9
Incline dumbell press: 40x12, 40x10, 
Machine press: burnout low weightx3
Tricep pulldown: 120x7, 110x8, 100x14
Assisted dips: 2?(2)x12, 2?(2)x12, 2?(2)x12


2/12/2024
Bench: 115x12, 115x11, 115x8
Incline dumbbell press: 37.5x12, 37.5x11, 37.5x10
Machine press: 95x6, 80x6, burnout set
Tricep pull-down: 115x12, 105x11, 100x10
Assisted dips: 3?(1)x12, 3?(1)x12, 3?(1)x 12


2/5/2024
Bench: 115x12, 115x10, 115x7
Incline dumbbell press: 37.5x12, 37.5x10, 37.5x6.5
Machine press: 95x8, 95x6, 80x10
Tricep concentration: 50x11, 45x13, 45x11
Tricep pull-down: 100x11, 100x8, 90x8
Assisted dip: 3?(1)x12, 3?(1)x12, 3?(1)x


2/2/2024
Bench: 135x5, 115x9, 115x7
Machine press: 95x9, 95x6, 95x6
Incline dumbbell press: 35x8, 35x8, 35x8
Tricep concentration: 50x11, 50x6, 45x11
Tricep pull-down: 100x11, 100x7, 90x8
Assisted dips:3?(1)x12, 3?(1)x8, 3?(2)x



1/29/2024
Lateral raise: 12.5x16, 12.5x16, 12.5x16
Bench: 135x4, 115x9, 115x6
Machine press: 95x8, 95x7, 95x8
Incline dumbell press: 32.5x12, 32.5x11.5, 32.5x
Tricep concentration: 50x11, 50x10, 45x14
Tricep pull-down: 100x8, 90x10, 90x10
Assisted dip: 3?(2)x15, 3?(1)x8, a


1/26/2024
Bench: 115x11, 115x9, 115x5
Incline dumbell press: 35x12, 35x9, 35x10
Machine press: 90x8, 90x9, 90x7
Tricep concentration: 50x13, 50x9, 50x6, 50x3 right after
Tricep pull-down: 100x8, 90x9, 90x9
Assisted dip: 3?(2)x9, 3?(2)x11, 3?(2)x8


1/22/2024
Bench: 115x11, 115x8, 115x4
Incline dumbbell press: 35x12, 35x9, 35x7
Machine chest press:5thx12, 105x5, 90x8
Tricep pulldowns: 100x12, 110x4, 100x6
Machine dips: 150x12, 165x12, 165x8


1/19/2024 ️ 
Bench: 115x10, 115x6, 105x8
Incline dumbbell press: 32.5x12, 32.5x10, 
Tricep concentration: 45x12, 45x11, 45x7


1/16/2024
Bench: 110x12, 110x10, 110x6
Incline dumbbell press: 32.5x12, 32.5x9, 
Machine press: idk the weights
Tricep concentration: 45x8, 42.5x10, 42.5x6
Machine dips: 105x14, 135x9, 135x10
Hard pulldowns: 40x7, 30x12, 30x12


1/12/2024
Bench: 105x12, 105x9, 100x9
Incline dumbbell press: 27.5x12, 27.5x10, 
Machine press: 95x8, 80x10, 80x8
Tricep concentration: 40x12, 45x7, 40x12
Tricep pull-down (good grip): 80x13, 90x8, 80x8
Machine dip: 105x14, 135x14, 165x7

1/9/2024:
Bench: 100x12, 100x11, 100x8
Incline dumbbell press: 25x12, 25x10, 25x12
Horizontal iso press: 15x8, 15x9, 15x9
Tricep concentration: 35x12, 40x11, 40x7
Tricep pull-down (good grip): 80x12, 80x10, 70x8
Machine dips: 85x15, 105x8, 105x8 


"""

# pull day data
pull_data = """
4/13/2024
Barbell curls: 55x16, 55x12, 55x12
Hammer curls: 27.5x12, 27.5x12, 27.5x12
Outside grip curls: 17.5x16, 17.5x16, 17.5x12



4/7/2024
Assisted pull-ups: 2?(1)x8, 2?(1)x9, 2?(1)x7
Low cable rows: 115x10, 100x15, 100x12
Lat pulldowns: 115x6, 100x9, 85x12
Barbell curls: 55x12, 55x12, 55x12
Hammer curls: 25x13, 25x12, 25x13
Outside grip curl: 20x9, 20x7, 20x





4/5/2024
Barbell curl: 60x16, 60x10, 55x12
Hammer curl: 27.5x12, 27.5x12, 27.5x13
Outside grip curl: 17.5x13, 17.5x12, 17.5x16
Dips: 14, 14, 10
Tricep pull-down: 100x18, 110x14, 110x12, 110x9

 

4/1/2024
Lat pull-down: 115x12, 115x8, 100x13
Low cable row: 115x10, 100x12, 100x10
Barbell curls: 55x16, 55x12, 55x9
Hammer curls: 30x12, 27.5x12, 27.5x12
Outside grip curls: 20x8, 17.5x12, 17.5x8



3/22/2024
21s x3
Outside grip ez bar curl: 45x30
Hammer curl: 30x13, 30x9, 27.5x17
Outside grip curl: 17.5x17, 17.5x17, 17.5x


3/17/2024
Lat pull-down: 115x9, 100x13, 100x9
Low cable rows: 115x10, 100x12, 100x
Assisted pull-ups : 2 sets
21s x2
Bar curls: 45x10, 
Hammer curls: 27.5x12, 27.5x13, 27.5x9
Outside grip curl: 17.5x16, 17.5x10, 17.5x



3/14/2024
Lat pull-down: 115x9, 100x14, 100x11
T bar rows: 55x12, 55x12, 55x16
Low cable rows: 85x14, 85x20, 85x13
7x7x7 x2
Hammer curls: 25x20, 30x10, 25x14
Outside grip curl: 17.5x13, 17.5x9, 17.5x




3/8/2024
Lat pull-down: 115x12, 100x12, 100x11
Low cable row: 115x14, 115x8, 100x14, 100x12, 100x140
Preacher curl: 65x12, 60x12, 60x12
Hammer curl: 30x14, 30x10, 25x12
Outside grip curl: 20x12, 20x12, 20x11


3/5/2024
Lat pull-down: 115x12, 100x12, 100x11
Low cable rows: 100x12, 100x19, 100x14, 115x8, 100x14
Preacher curl: 65x11, 60x9, 60x14
Hammer curl: 30x13, 30x10, 25x12
Outside grip curl: 20x11, 20x12, 20x10


3/2/2024
Lat pull-down: 100x19, 100x13, 100x9
Low cable row: 115x8, 100x9, 85x13, 85x19, 85x13
Preacher curl: 65x10, 60x12, 60x13
Hammer curl: 27.5x15, 27.5x13, 27.5x10
Outside grip curl: 20x10(?), 20x9, 






2/28/2024
Assisted pull-ups: 3?(1)x12, 3?(1)x12, 3?(1)x9
Lat pull downs: 100x9, 85x13, 85x9
Low cable row: 100x12, 85x14, 85x13
Preacher curls: 60x13, 60x12, 60x12
Hammer curls: 27.5x12, 27.5x10, 25x14
Outside grip curls: 20x11, 20x10, 20x10




2/25/2024
Lat pull-down: 115x8, 100x12, 85x14
Assisted pull-ups: 3?(2)x8, 4?x8, 4?x10
Low cable rows: 85x20, 100x10, 85x16
Preacher curls: 55x16, 60x13, 60x12
Hammer curls: 27.5x12, 25x13, 25x13
Outside grip curl (good all the way down reps): 20x8, 20x10, 



2/20/2024
Lat pull-down mid grip: 115x10, 100x11, 85x14
Low cable rows: 100x14, 110x11, 85x12
Assisted pull-ups: 4?x8, 4?x8
Preacher curls: 55x16, 60x13, 60x12
Hammer curls: 25x16, 25x12, 25x11
Outside grip curl: 25x5, 20x10, 20x a lot


2/17/2024
Assisted pull-ups: 3?(1)x12, 3?(1)x9, 3?(2)x9
Lat pulldowns (narrow grip): 85x12, 85x11, 85x10
Low cable row: 85x13, 85x12, 85x11
Preacher curls: 55x12, 55x9, 55x12
Hammer curls: 25x10, 20x14, 20x12
Outside grip curls: 20x7.5, 17.5x8, 17.5x7



2/13/2024
Lat-pull-down: 100x12, 100x12, 100x9
Low cable rows: 85x14, 100x8, 100x8
Assisted pull-up: 3?(2)x9, 3?(2)x8, 4?x9
Preacher curl: 55x12, 55x14, 55x12
Hammer curl: 25x12, 25x12, 25x8
Outside grip curl: 22.5x6, 20x9, 


2/7/2024
Assisted pull-up: 3?(1)x12, 3?(1)x12, 3(1)x9
Preacher curl: 55x20, 65x10, 65x8
Hammer curl: 25x12, 25x11, 22.5x12
Outside grip curl: 22.5x8, 20x8, 20x10
Tricep concentration: 50x7, 45x19, 45x23, 45x17
Assisted dip: 3?(1)x12, one below that 2x x12



2/4/2024
Assisted pull-up: 3?(1)x12, 3?(1)x8, 3?(1)x6
Low cable row: 85x15, 85x12, 85x12
Lat pulldown: 85x12, 85x11, slow reps 85x6
Preacher curl: 65x8, 55x14, 55x11
Hammer curls: 22.5x16, 22.5x12, 22.5x9
Outside grip curls: 22.5x8, 20x12, 20x8





1/31/2024
Assisted pull-up: 3?(2)x12, 3?(1)x9, 3?(1)x6
Low cable row: 70x14, 70x14, 70x14
Lat pull-down: 85x12, 85x10, 85x9
Preacher curls: 70x6, 65x8.5, 55x13
Hammer curls: 25x9, 25x8, 25x7
Outside grip curl: 22.5x7, 20x10, 20x



1/28/2024
Assisted pull-up: 4?x13, 4?x11, 3?(2)x8
Low cable row (leaning forward): 60x12, 60x10, 70x8
Hi to lo cable row: fuck… that was good
Preacher curl: 65x12, 70x7, 65x8
Hammer curls: 25x9, 25x8, 25x7
Outside grip curls: 22.5x6, 20x9, 20x7
Lateral raise: 12.5x16, 12.5x16, 12.5x16



1/24/2024
Lat pull-down: 85x12, 85x10, 85x12, 85x6
Low cable row: 70x8, 70x12, 85x10
 Assisted pull-ups idk
Preacher curls: 65x6, 65x5, 55x14, 55x11
Hammer curls: 25x8.5, 22.5x9, 22.5x8
Outside grip curls: 20x7, 20x6, 




1/21/2024
Assisted pull-ups: 3?(2)x12, 3?(2)x8, 4?x6(slow reps), 
Hammer high rows: 45x?, 45x9, 45x8
Low cable rows: fuck idk, 70x10, 70x12, 
Barbell curl: 55x12, 55x8, 55x6
Hammer curl: 25x8, 22.5x8, 22.5x8
Outside grip curl: 22.5x6, 20x8.5, 20x7



1/18/2024
Back pain… went easy on the back shit
Preacher curls: 50x12, 55x12
Standing barbell curl: 65x5
Hammer curl: 25x12, 25x10, 22.5x10
Outside grip curl: 22.5x8, 17.5x12, 



1/14/2024
Assisted pull-ups: 4?x12, 3?(2)x9, 3?(2)x8, 4?x6
Low cable rows: 85x8, 70x8, 70x13, 
Hammer high row: 40x12, 50x6, 40x10
Curl: 27.5x9, 27.5x6, 22.5x11
Hammer curl: 22.5x11, 22.5x7, 20x12
Outside grip curl: 20x7, 17.5x10, 



1/11/2024
Assisted pull-up: 4?x12, 4?x10, 4?x10
Low cable row: 70x12, 70x10, 70x10
Lat pull-down: 70x12, 85x10, 85x10
Curl: 22.5x12, 22.5x9, 22.5x9
Hammer curl: 22.5x8, 20x12, 20x11
Outside grip curl: 20x8, 17.5x9, 17.5x7


 

1/8/2024:
Assisted pull-up: 70x12, 55x12, 55x8
Low cable row: 70x10, 60x10, 60x14
T-bar row: 35x12, 35x12, 35x12
Preacher curls: 10x12, 15x8, 12.5x10
Hammer curls: 17.5x12, 17.5x12, 17.5x12
Outside grip curls: 17.5x8, 15x10, 

"""

weight_data = """
12/9/23
133
12/16/23
136.5
12/22/23
140
12/30/23
142
1/6/24
142.6
1/13/24
143.5
1/20/24
143.6
1/28/24
144.5
2/3/24
145
2/7/24
145
2/13/24
147
2/24/24
146
3/2/24
147
3/8/24
149
3/13/24
150
3/24/24
153
4/14/24
151

"""


def parse_weight_data(data):
    lines = data.strip().split('\n')
    date = None
    weight_data = []

    for line in lines:
        if line.count('/') == 2:  # Date line
            date = line.strip()
        else:
            weight = line.strip()
            weight_data.append((date, weight))  # holds a series of tuples

    return weight_data


def parse_exercise_data(data, exercise):
    lines = data.strip().split('\n')
    date = None
    exercise_data = []

    for line in lines:
        if line.count('/') == 2:  # Date line
            date = line.strip()
        elif exercise in line:
            sets = line.split(':')[1].split(',')
            sets = [s.strip() for s in sets if 'x' in s and s.split('x')[1].isdigit()]  # Ensure all sets are valid

            # If there are less than 3 sets, estimate the missing sets (assuming valid input here)
            while len(sets) < 3:
                if len(sets) == 2:
                    weight, reps = sets[-1].split('x')
                    reps = str(int(reps) - 2)  # Assuming reps can safely decrease by 2
                    sets.append(f"{weight}x{reps}")

            exercise_data.append((date, sets[0], sets[1], sets[2]))

    return exercise_data


def write_to_csv_exercise(filename, exercise_data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Set 1', 'Set 2', 'Set 3'])
        for entry in exercise_data:
            writer.writerow(entry)


def write_to_csv_weight(filename, weight_data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Weight'])
        for entry in weight_data:
            writer.writerow(entry)


# bench_name = "Bench"
# bench_data = parse_data(bench_data, bench_name)
# write_to_csv('bench_data.csv', bench_data)

# curl_name = "Hammer curl"
# pull_data = parse_data(pull_data, curl_name)
# write_to_csv('curl_data.csv', pull_data)

# lat_name = "Lat "
# pull_data = parse_exercise_data(pull_data, lat_name)
# write_to_csv_exercise('pulldown_data.csv', pull_data)

# weight_data = parse_weight_data(weight_data)
# write_to_csv_weight("weight_data.csv", weight_data)
