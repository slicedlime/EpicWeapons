# Ravager killed!
execute store result score $Count ew_temp run data get storage ew:temp tag.kills.ravager 1
scoreboard players operation $Count ew_temp += @s ew_ravager
execute store result storage ew:temp tag.kills.ravager int 1 run scoreboard players get $Count ew_temp
scoreboard players reset @s ew_ravager
