# Husk killed!
execute store result score $Count ew_temp run data get storage ew:temp tag.kills.husk 1
scoreboard players operation $Count ew_temp += @s ew_husk
execute store result storage ew:temp tag.kills.husk int 1 run scoreboard players get $Count ew_temp
scoreboard players reset @s ew_husk
