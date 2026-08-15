"""
Grocery List:

Implement a program that prompts the user for items, one per line,
until the user inputs control-d (which is a common way of ending one’s input to a program).

Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item.

No need to pluralize the items. Treat the user’s input case-insensitively.
"""

item_dict = {}

while True:
    try:
        item = input().upper()
        if item in item_dict:
            item_dict[item] += 1
        else:
            item_dict[item] = 1
    except EOFError:
        # catch CTRL+D from keyboard
        break

sorted_items = sorted(item_dict)

for key in sorted_items:
    print(item_dict[key], key)
