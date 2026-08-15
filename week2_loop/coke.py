"""
Coke Machine.
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and
only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

Implement a program that prompts the user to insert a coin,
one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
Assume that the user will only input integers, and
ignore any integer that isn’t an accepted denomination.

"""
coke_price = amount_due = 50
inserted_coins = 0

while inserted_coins < coke_price:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        amount_due -= coin
        inserted_coins += coin
    else:
        continue

print(f"Change Owed: {inserted_coins - coke_price}")

