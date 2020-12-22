# Piglin killed!
execute store result score $Count ew_temp run data get storage ew:temp tag.kills.piglin 1
scoreboard players operation $Count ew_temp += @s ew_piglin
execute store result storage ew:temp tag.kills.piglin int 1 run scoreboard players get $Count ew_temp
scoreboard players reset @s ew_piglin
