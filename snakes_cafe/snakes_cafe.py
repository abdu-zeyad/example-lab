

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
listMenu = ["wings", "cookies", "spring rolls", "salmon", "steak", "meat tornado",
            "a literal garden", "ice cream", "cake", "pie", "coffee", "tea", "unicorn Tears"]


def orderfunction():
    order = []
    a = input(' ')
    while a != 'quit':

        if a in listMenu or a.lower() in listMenu:
            order.append(a.lower())
            print(
                f'* {order.count(a.lower())} order of {a.lower()} have been added to your meal *')
        else:
            print('please order one of the stuff on the menu!!')
        a = input(' ')


if __name__ == '__main__':
    orderfunction()
