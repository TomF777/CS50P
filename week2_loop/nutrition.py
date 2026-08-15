"""
Implement a program that prompts consumers users to input a fruit (case-insensitively)
and then outputs the number of calories in one portion of that fruit.

Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry).
Ignore any input that isn’t a fruit.
"""

fruit_calories = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydew Melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Tangerine": 50,
    "Watermelon": 80
}

item = input("Item: ").title()
if item in fruit_calories:
    calories = fruit_calories[item]
    print(f"Calories: {calories}")
