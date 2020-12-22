# Wither Skeleton killed!
execute store result score $Count ew_temp run data get storage ew:temp tag.kills.wither_skeleton 1
scoreboard players operation $Count ew_temp += @s ew_wither_skele
execute store result storage ew:temp tag.kills.wither_skeleton int 1 run scoreboard players get $Count ew_temp
scoreboard players reset @s ew_wither_skele
