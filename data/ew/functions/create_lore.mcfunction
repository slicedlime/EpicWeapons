# Find the highest kill score, create a lore message based on that

scoreboard players reset * ew_temp

# Copy all the kill counts to a scoreboard
execute store result score $Spiders ew_temp run data get storage ew:temp tag.kills.spiders 1

# Find the maximum
scoreboard players set $Max ew_temp 0
scoreboard players operation $Max ew_temp > * ew_temp

# Figure out which was the maximum
execute if entity @s[tag=ew_mainhand] run item entity @s weapon.mainhand modify ew:set_lore
execute if entity @s[tag=ew_offhand] run item entity @s weapon.offhand modify ew:set_lore
