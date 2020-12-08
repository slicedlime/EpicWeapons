# React to a ranged kill
tag @s remove ew_mainhand
tag @s remove ew_offhand

# Check main hand
execute if entity @s[nbt={SelectedItem:{id:"minecraft:bow"}}] run tag @s add ew_mainhand
execute if entity @s[nbt={SelectedItem:{id:"minecraft:crossbow"}}] run tag @s add ew_mainhand

# Check off hand
execute unless entity @s[tag=ew_mainhand] if entity @s[nbt={Inventory:[{Slot:-106b,id:"minecraft:bow"}]}] run tag @s add ew_offhand
execute unless entity @s[tag=ew_mainhand] if entity @s[nbt={Inventory:[{Slot:-106b,id:"minecraft:crossbow"}]}] run tag @s add ew_offhand

advancement revoke @s only ew:hidden/ranged
