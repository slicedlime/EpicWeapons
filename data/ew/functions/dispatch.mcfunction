# Update stats based on kill type

# Copy item kills to storage
data remove storage ew:temp tag
execute if entity @s[tag=ew_mainhand] run data modify storage ew:temp tag.kills merge from entity @s SelectedItem.tag.kills
execute if entity @s[tag=ew_offhand] run data modify storage ew:temp tag.kills merge from entity @s Inventory[{Slot:-106b}].tag.kills

scoreboard players set $Count ew_temp 0

# Do type-specific digging
function ew:dispatch_types

# Copy data back to item
execute if entity @s[tag=ew_mainhand] run item entity @s weapon.mainhand modify ew:copy_tag
execute if entity @s[tag=ew_offhand] run item entity @s weapon.offhand modify ew:copy_tag

# Make the lore
execute if entity @s[tag=ew_mainhand] run function ew:create_lore
execute if entity @s[tag=ew_offhand] run function ew:create_lore

tag @s remove ew_mainhand
tag @s remove ew_offhand
