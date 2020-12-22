# Stray killed!
execute store result score $Count ew_temp run data get storage ew:temp tag.kills.stray 1
scoreboard players operation $Count ew_temp += @s ew_stray
execute store result storage ew:temp tag.kills.stray int 1 run scoreboard players get $Count ew_temp
scoreboard players reset @s ew_stray
