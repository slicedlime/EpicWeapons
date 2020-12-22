# Cave Spider killed!
execute store result score $Count ew_temp run data get storage ew:temp tag.kills.cave_spider 1
scoreboard players operation $Count ew_temp += @s ew_cave_spider
execute store result storage ew:temp tag.kills.cave_spider int 1 run scoreboard players get $Count ew_temp
scoreboard players reset @s ew_cave_spider
