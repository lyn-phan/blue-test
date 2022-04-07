"""Check Inventory
You have just started working at a brand-new retail store. Unfortunately, it is difficult to remember which products
are in stock due to the store's unique inventory system.
Write a function checkInventory(I,R) that will accept 2 arguments:
        I - Inventory (nested object - see example below)
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
        R - Request (object)
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

# init an array to track found items
# loop through R (for request), check within I to see if that attribute for R exists, if not, return an empty list
# if the attribute exists, then look for the value of that attribute key, if it exists there are not more items in the request
# return the values of that key
# if there are further requests, continue to check the rest of the dictionary and return its values


def checkInventory(I, R):
    found_items = []
    nested_items = []

    for key, value in R.items():
        if I.get(key, []):
            found_items.append(value)

    for i in range(len(found_items)):
        item = found_items[i]
        res = [val[item] for k, val in I.items() if item in val]  # red, small
        nested_items.append(res)
        flat_list = [code for sublist in nested_items for code in sublist]
        if len(flat_list) == 1:
            return list(flat_list)
        else:
            seen = set()
            for i in range(len(flat_list)):
                element = flat_list[i]
                if isinstance(element, list):
                    for i in range(len(element)):
                        if element[i] in seen:
                            return element[i]
                        else:
                            seen.add(element[i])
                else:
                    if element in seen:
                        return element
                    else:
                        seen.add(element)


I = {"color": {
    "blue": [123, 456, 789],
    "red": [234, 567, 890]
},
    "size": {
        "small": [123, 234],
        "medium": [456, 789],
        "large": [567, 890]
}
}

# R = {"color": "red", "size": "small"}
# R = {"color": "red"}
R = {"color": "green"}
print(checkInventory(I, R))
