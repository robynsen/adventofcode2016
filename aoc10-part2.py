import re

def add_value(my_bots, bot_i, val_n):
    if bot_i in my_bots:
        my_bots[bot_i].append(val_n)
    else:        
        my_bots[bot_i] = [val_n]

def transfer_chips(my_bots, bot_id):
    # note: does not cater to both high and low going to same bot that currently holds one chip
    for key, value in my_bot_instr[bot_id].items():
        # check if next bot has max chips
        if str(value)[:6] != 'OUTPUT' and has_max_chips(my_bots, value):
            transfer_chips(my_bots, value)
    # now the recipient bot will have < 2 chips
    tmp = 0
    for key, value in my_bot_instr[bot_id].items():
        if key == 'LOW':
            tmp = min(my_bots[bot_id])
        else:
            tmp = max(my_bots[bot_id])

        if str(value)[:6] != 'OUTPUT':
            # send to next bot
            add_value(my_bots, value, tmp)
        elif int(str(value)[6:]) < 3:
            # send to output
            output_chips[int(str(value)[6:])].append(tmp)
        my_bots[bot_id].remove(tmp)

def has_max_chips(my_bots, bot_id):
    return (bot_id in my_bots and (len(my_bots[bot_id]) > 1))

with open('aoc10-input.txt', 'r') as infile:
    # format: value 5 goes to bot 2
    add_regex = re.compile(r"value ([0-9]+) goes to bot ([0-9]+)")
    # format: bot 2 gives low to bot 1 and high to bot 0
    move_regex = re.compile(r"bot ([0-9]+) gives low to (bot|output) ([0-9]+) and high to (bot|output) ([0-9]+)")

    # x = for each both ID, a list of chip IDs it holds
    my_bots = {}
    # x = for each bot ID, a dict of key, value = LOW/HIGH, next bot ID
    my_bot_instr = {}
    output_chips = [[], [], []]

    for line in infile:
        add_result = add_regex.match(line)
        move_result = move_regex.match(line)
        
        if add_result:
            my_value = int(add_result.group(1))
            bot_target = int(add_result.group(2))
            add_value(my_bots, bot_target, my_value)
        elif move_result:
            bot_src = int(move_result.group(1))
            instr_low = move_result.group(2)
            bot_low = int(move_result.group(3))
            instr_high = move_result.group(4)
            bot_high = int(move_result.group(5))
            
            my_bot_instr[bot_src] = {}

            for i in ((instr_low, bot_low, 'LOW'), (instr_high, bot_high, 'HIGH')):                
                if i[0] == 'bot':
                    my_bot_instr.setdefault(bot_src,[]).update({i[2]: i[1]})
                elif i[0] == 'output':
                    my_bot_instr.setdefault(bot_src,[]).update({i[2]: 'OUTPUT' + str(i[1])})

    # bots 174 125 59 output to 0, 1, 2
    result = False
    while not result:
        # find bot with two chips and pass those on
        for key, value in my_bots.items():
            if len(value) > 1:
                transfer_chips(my_bots, key)
                break

        result = True
        for key, value in my_bots.items():
            if len(value) > 1:
                result = False     

    print('output_chips[0] * output_chips[1] * output_chips[2] =', 
        output_chips[0][0], '*', output_chips[1][0], '*', output_chips[2][0],
        '=',
        output_chips[0][0] * output_chips[1][0] * output_chips[2][0])