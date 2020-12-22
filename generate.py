import json

scoreboard_types = {}
scoreboard_seen = []
scoreboard_counter = 0

def get_id(type):
    return type.lower().replace(' ', '_')

def get_scoreboard_id(type_name):
    type = get_id(type_name)
    if type in scoreboard_types.keys():
        return scoreboard_types[type]

    short = type[0:12]
    if short in scoreboard_seen:
        short = type[0:10] + str(scoreboard_counter)
        scoreboard_counter += 1
    scoreboard_seen.append(short)
    scoreboard_types[type] = short
    return short

def write_predicate(mob_type):
    data = {
        'condition': 'value_check',
        'value': {
            'type': 'score',
            'score': 'ew_temp',
            'target': {
                'type': 'fixed',
                'name': '$' + get_id(mob_type)
            }
        },
        'range': {
            'min': {
                'type': 'score',
                'score': 'ew_temp',
                'target': {
                    'type': 'fixed',
                    'name': '$Max'
                }
            }
        }
    }

    with open('data/ew/predicates/types/' + get_id(mob_type) + '.json', 'w') as file:
        json.dump(data, file, indent=4)

def write_function(type):
    with open('data/ew/functions/types/' + get_id(type) + '.mcfunction', 'w') as file:
        file.write('# ' + type + ' killed!\n')
        file.write('execute store result score $Count ew_temp run data get storage ew:temp tag.kills.' + get_id(type) + ' 1\n')
        file.write('scoreboard players operation $Count ew_temp += @s ew_' + get_scoreboard_id(type) + '\n')
        file.write('execute store result storage ew:temp tag.kills.' + get_id(type) + ' int 1 run scoreboard players get $Count ew_temp\n')
        file.write('scoreboard players reset @s ew_' + get_scoreboard_id(type) + '\n')

def get_copy_score_line(type):
    return 'execute store result score $' + get_id(type) + ' ew_temp run data get storage ew:temp tag.kills.' + get_id(type) + ' 1'

def get_dispatch_line(type): 
    return 'execute if score @s ew_' + get_scoreboard_id(type) + ' matches 1.. run function ew:types/' + get_id(type)

def get_scoreboard_line(type):
    return 'scoreboard objectives add ew_' + get_scoreboard_id(type) + ' minecraft.killed:minecraft.' + get_id(type) + ' "' + type + ' Killed"'

def get_lore_table(type):
    lore = []
    for i in range(5):
        lore.append({
            'function': 'set_lore',
            'entity': 'this',
            'conditions': [
                {
                    'condition': 'reference',
                    'name': 'ew:types/' + get_id(type)
                },
                {
                    'condition': 'reference',
                    'name': 'ew:level' + str(i + 1)
                }
            ],
            'lore': [
                {
                    'nbt': get_id(type) + '[' + str(i) + ']',
                    'storage': 'ew:lore',
                    'color': 'white'
                }
            ],
            'replace': True
        })
    return lore

types = [
    'Blaze',
    'Cave Spider',
    'Creeper',
    'Drowned',
    'Enderman',
    'Endermite',
    'Evoker',
    'Ghast',
    'Guardian',
    'Hoglin',
    'Husk',
    'Magma Cube',
    'Phantom',
    'Piglin',
    'Piglin Brute',
    'Pillager',
    'Ravager',
    'Shulker',
    'Silverfish',
    'Skeleton',
    'Slime',
    'Spider',
    'Stray',
    'Vex',
    'Vindicator',
    'Witch',
    'Wither Skeleton',
    'Zoglin',
    'Zombie',
    'Zombie Villager',
    'Zombified Piglin'
]

set_lore = []
with open('data/ew/functions/copy_kill_scores.mcfunction', 'w') as kill_file,\
     open('data/ew/functions/dispatch_types.mcfunction', 'w') as dispatch_file,\
     open('data/ew/functions/create_type_scoreboards.mcfunction', 'w') as scoreboard_file:
    for type in types:
        write_predicate(type)
        write_function(type)
        kill_file.write(get_copy_score_line(type) + '\n')
        dispatch_file.write(get_dispatch_line(type) + '\n')
        scoreboard_file.write(get_scoreboard_line(type) + '\n')
        set_lore.extend(get_lore_table(type))

with open('data/ew/item_modifiers/set_lore.json', 'w') as lore_file:
    json.dump(set_lore, lore_file, indent=4)
