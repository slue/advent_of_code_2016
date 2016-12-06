import copy

input = "R4, R3, L3, L2, L1, R1, L1, R2, R3, L5, L5, R4, L4, R2, R4, L3, R3, L3, R3, R4, R2, L1, R2, L3, L2, L1, R3, R5, L1, L4, R2, L4, R3, R1, R2, L5, R2, L189, R5, L5, R52, R3, L1, R4, R5, R1, R4, L1, L3, R2, L2, L3, R4, R3, L2, L5, R4, R5, L2, R2, L1, L3, R3, L4, R4, R5, L1, L1, R3, L5, L2, R76, R2, R2, L1, L3, R189, L3, L4, L1, L3, R5, R4, L1, R1, L1, L1, R2, L4, R2, L5, L5, L5, R2, L4, L5, R4, R4, R5, L5, R3, L1, L3, L1, L1, L3, L4, R5, L3, R5, R3, R3, L5, L5, R3, R4, L3, R3, R1, R3, R2, R2, L1, R1, L3, L3, L3, L1, R2, L1, R4, R4, L1, L1, R3, R3, R4, R1, L5, L2, R2, R3, R2, L3, R4, L5, R1, R4, R5, R4, L4, R1, L3, R1, R3, L2, L3, R1, L2, R3, L3, L1, L3, R4, L4, L5, R3, R5, R4, R1, L2, R3, R5, L5, L4, L1, L1"

# the overall distances driven in each direction
distance = {
    "north": 0,
    "east": 0,
    "south": 0,
    "west": 0
}

# the locations visited after each step
location_history = [{"x":0,"y":0}]

turnarounds = {
    "north": {
        "R": 'east',
        "L": 'west'
    },
    "east": {
        "R": 'south',
        "L": 'north'
    },
    "south": {
        "R": 'west',
        "L": 'east'
    },
    "west": {
        "R": 'north',
        "L": 'south'
    },
}

def check_for_visited_location(new_location):
    for location in location_history:
        if cmp(location, new_location) == 0:
            print '----location visited twice: (x: ' + str(location['x']) + ', y: '+ str(location['y'])+') / distance: ' + str(calc_taxi_metric_distance(distance))
            print_taxi_metric(distance)
            exit()

def drive_block(facing):
    distance[facing] += 1

    current_location = copy.copy(location_history[-1])
    if facing is 'north':
        current_location['x'] += 1
    elif facing is 'south':
        current_location['x'] -= 1
    elif facing is 'east':
        current_location['y'] += 1
    elif facing is 'west':
        current_location['y'] -= 1
    check_for_visited_location(current_location)
    location_history.append(current_location)
    print '    goto (x: '+str(current_location['x']) +' / y: '+str(current_location['y']) +')'

def drive_distance(direction, blocks):
    print 'Facing ' + facing + ' driving ' + str(blocks) + ' blocks to ' + direction
    new_facing = turnarounds[facing][direction]
    for i in range(0,blocks):
        drive_block(new_facing)
    return new_facing

def calc_taxi_metric_distance(calc_distance):
    return abs(calc_distance['north'] - calc_distance['south']) + abs(calc_distance['east'] - calc_distance['west'])

def print_taxi_metric(calc_distance):
    north_south_distance = calc_distance['north'] - calc_distance['south']
    east_west_distance = calc_distance['east'] - calc_distance['west']

    ret_string = 'the taxi metric is: '
    ret_string = ret_string + str(abs(north_south_distance))
    if north_south_distance >= 0:
        ret_string = ret_string + ' north, '
    else:
        ret_string = ret_string + ' south, '
    ret_string = ret_string + str(abs(east_west_distance))
    if east_west_distance >= 0:
        ret_string = ret_string + ' east'
    else:
        ret_string = ret_string + ' west'

    print ret_string

facing = 'north'

directions = input.split(", ")
for direction_entry in directions:
    # get direction and blocks driven
    direction = direction_entry[0]
    blocks = int(direction_entry[1:])
    facing = drive_distance(direction, blocks)

print 'Driven:'
print '  ' + str(distance['north']) + ' blocks north'
print '  ' + str(distance['east']) + ' blocks east'
print '  ' + str(distance['south']) + ' blocks south'
print '  ' + str(distance['west']) + ' blocks west'

print ''
print_taxi_metric(distance)
print 'the total taxi metric distance is: ' + str(calc_taxi_metric_distance(distance))
