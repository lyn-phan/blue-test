"""Check Inventory
You have just started working at a brand-new retail store. Unfortunately, it is difficult to remember which products
are in stock due to the store’s unique inventory system.
Write a function checkInventory(I,R) that will accept 2 arguments:
I – Inventory (nested object – see example below)
{
attribute_1: {
value_1: [array of integer product IDs],
value_2: [array of integer product IDs]
},
attribute_2: {
value_1: [array of integer product IDs],
value_2: [array of integer product IDs]
}
}
R – Request (object)
{
attribute_1: value_1,
attribute_2: value_2
}
Your function should return an array of product IDs that match all the attributes in the request. If there are no
matches, return an empty array. Note that there can be any number of attributes and values in the inventory
object. The request may also be a partial request (only contains some of the total attributes).
Example
I = {
color: {
blue: [123,456,789],
red: [234,567,890]
},
size: {
small: [123,234],
medium: [456,789],
large: [567,890]
}
}
R = {color: 'red ', size: 'small '} → Your function should return [234]
R = {color: 'red '} → Your function should return [234,567,890]
R = {color: 'green'} → Your function should return []"""