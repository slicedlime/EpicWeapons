import json

def write_predicate(mob_type):
    data = {
        'condition': 'value_check',
        'value': {
            'type': 'score',
            'score': 'ew_temp',
            'target': {
                'type': 'fixed',
                'name': '$' + mob_type
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

    with open('data/ew/predicates/types/' + mob_type.lower() + '.json', 'w') as file:
        json.dump(data, file, indent=4)

def write_function(type):
    with open('data/ew/functions/types/' + type.lower() + '.mcfunction', 'w') as file:
        file.write('# ' + type + ' killed!\n')
        file.write('execute store result score $Count ew_temp run data get storage ew:temp tag.kills.' + type.lower() + ' 1\n')
        file.write('scoreboard players operation $Count ew_temp += @s ew_' + type.lower() + '\n')
        file.write('execute store result storage ew:temp tag.kills.' + type.lower() + ' int 1 run scoreboard players get $Count ew_temp\n')
        file.write('scoreboard players reset @s ew_' + type.lower() + '\n')

def get_copy_score_line(type):
    return 'execute store result score $' + type + ' ew_temp run data get storage ew:temp tag.kills.' + type.lower() + ' 1'

def get_dispatch_line(type): 
    return 'execute if score @s ew_' + type.lower() + ' matches 1.. run function ew:types/' + type.lower()

def get_scoreboard_line(type):
    return 'scoreboard objectives add ew_' + type.lower() + ' minecraft.killed:minecraft.' + type.lower().replace(' ', '_') + ' "' + type + ' Killed"'

types = [
    'Skeleton',
    'Spider'
]

with open('data/ew/functions/copy_kill_scores.mcfunction', 'w') as kill_file,\
     open('data/ew/functions/dispatch_types.mcfunction', 'w') as dispatch_file,\
     open('data/ew/functions/create_type_scoreboards.mcfunction', 'w') as scoreboard_file:
    for type in types:
        write_predicate(type)
        write_function(type)
        kill_file.write(get_copy_score_line(type) + '\n')
        dispatch_file.write(get_dispatch_line(type) + '\n')
        scoreboard_file.write(get_scoreboard_line(type) + '\n')
