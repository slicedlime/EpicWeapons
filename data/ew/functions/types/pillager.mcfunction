# Pillager killed!
execute store result score $Count ew_temp run data get storage ew:temp tag.kills.pillager 1
scoreboard players operation $Count ew_temp += @s ew_pillager
execute store result storage ew:temp tag.kills.pillager int 1 run scoreboard players get $Count ew_temp
scoreboard players reset @s ew_pillager
