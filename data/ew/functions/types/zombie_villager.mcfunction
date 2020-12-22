# Zombie Villager killed!
execute store result score $Count ew_temp run data get storage ew:temp tag.kills.zombie_villager 1
scoreboard players operation $Count ew_temp += @s ew_zombie_villa
execute store result storage ew:temp tag.kills.zombie_villager int 1 run scoreboard players get $Count ew_temp
scoreboard players reset @s ew_zombie_villa
