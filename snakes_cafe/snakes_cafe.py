

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
listMenu = ["Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Tornado",
            "A Literal Garden", "Ice Cream", "Cake", "Pie", "Coffee", "Tea", "Unicorn Tears"]


def lab():
    order = []
    a = input(' ')

    for i in range(8):
        if a in listMenu:
            order.append(a)
            print(
                f'** {order.count(a)} order of {a} have been added to your meal **')
        else:
            print('please order one of the stuff on the menu!!')
        a = input(' ')


if __name__ == '__main__':
    lab()
