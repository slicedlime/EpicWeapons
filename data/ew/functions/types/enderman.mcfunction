# Enderman killed!
execute store result score $Count ew_temp run data get storage ew:temp tag.kills.enderman 1
scoreboard players operation $Count ew_temp += @s ew_enderman
execute store result storage ew:temp tag.kills.enderman int 1 run scoreboard players get $Count ew_temp
scoreboard players reset @s ew_enderman
