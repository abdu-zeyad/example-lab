

menu = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""
print(menu)
list_food = []

for i in range(7):

    order = input()
    if order in list_food:
        print(f"{len(list_food)} order of {order} have been added to your meal")
        list_food['order'].append(order)
        print(len(list_food[order]))
    else:
        list_food.append(order)
        print(f"1 order of {order} have been added to your meal")
        print(list_food)
print(list_food)
