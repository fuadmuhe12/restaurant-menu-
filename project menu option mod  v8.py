from guess import *
from lot import *

meal = {
    'SHERO': 50,
    'FERFER': 45,
    'PASTA': 50,
    'DORO WOT': 350,
    'MICIRA': 300,
    'TEBSE': 200,
    'KITFO': 355.9,
    "TIBS FIRFIR": 237.2,
    "QUANTA FIRFIR": 237.2,
    "CHECHEBSA": 134.4,
    "FASTING FIRFIR": 134.4,

}

hot_beverage = {
    "SPECIAL TEA": 71.2,
    "COFFEE": 31.7,
    "TEA WITH COFFEE": 31.7,
    "PEANUT TEA": 39.6,
    "MILK": 39.6,
    "MILK WITH COFFEE": 39.6,
    "TRADITIONAL COFFEE": 31.7,
}

cold_beverage = {
    "HEINEKEN BEER BOTTLE": 97.1,
    "BEER": 63.3,
    "BEER 500ML": 97.1,
    "SOFT DRINK": 39.6,
    "AMBO MINERAL WATER": 39.6,
    "SMALL BOTTLED WATER": 31.7,
    "MEDIUM BOTTLED WATER": 47.5,
    "BIG BOTTLED WATER": 55.4,
    "ROYAL TONIC": 63.3,
}

pizza = {
    "SPECIAL PIZZA": 474.3,
    "PIZZA MARINARA": 434.7,
    "PIZZA MARGARITA": 434.7,
    "PIZZA VEGETABLE": 395.25,
    "PIZZA BEEF": 434.7,
    "PIZZA CHICKEN": 434.7,
    "PIZZA TUNA": 434.7,

}

soup = {
    "CHICKEN CREAM SOUP": 174,
    "FISH MAN SOUP": 150.2,
    "VEGETABLE SOUP": 142.3,
    "FRENCH ONION SOUP": 150.2,
    "ETHIOPIAN PEPPER SOUP": 150.2,
    "TOMATO CREAM SOUP": 150.2,
}

dessert = {
    "BANANA FRITTER": 142.3,
    "CREEP SUZETT": 142.3,
    "FRUIT SALAD": 118.6,
    "FRUIT PUNCH": 118.6,
}

fresh_juice = {
    "SPECIAL DELIGHT": 79.1,
    "SEASONAL JUICE": 71.4,
}

meal_orders = {

}

hot_beverage_orders = {

}

cold_beverage_orders = {

}

pizza_orders = {

}

soup_orders = {

}

dessert_orders = {

}

fresh_juice_orders = {

}

close_text = ('''

                            THANK YOU FOR USING OUR PRODUCT 

                                  have a great day!

                                   Menu is Closed.

                ''')
completed = ''' successfully completed 
'''
menu_type = ('''
       [1] NATIONAL Dish Menu
       [2] Hot Beverage Menu
       [3] Cold Beverage Menu
       [4] Pizza Menu
       [5] Soup Menu
       [6] Dessert Menu
       [7] Fresh Juice Menu
       [8] Go Back
       ''')


def update_opt_print(name_of_update):
    print(
        f'........Which Part Do You Wanna Update........''\n'
        
        f'           [1] Name of {name_of_update}''\n'
        f'           [2] Price of {name_of_update}''\n'
        f'           [3] Both''\n'
        f'           [4] Go Back')


def check_parameter(x, menu_type):
    if x in menu_type:
        return 'true'


def bill():
    meal_bill = dict()
    for key in set(meal.keys()) and set(meal_orders.keys()):
        meal_bill[key] = meal_orders[key] * meal[key]
    print("YOUR BILL IS:")
    for food in meal_bill:
        print(f'{food} : {meal_bill[food]}')
    hot_beverage_bill = dict()
    if len(hot_beverage_orders)!=0:
        print("************")
    for key in set(hot_beverage.keys()) and set(hot_beverage_orders.keys()):
        hot_beverage_bill[key] = hot_beverage_orders[key] * hot_beverage[key]
    for drink in hot_beverage_bill:
        print(f'{drink} : {hot_beverage_bill[drink]}')
    cold_beverage_bill = dict()
    if len(cold_beverage_orders)!=0:
        print("************")
    for key in set(cold_beverage.keys()) and set(cold_beverage_orders.keys()):
        cold_beverage_bill[key] = cold_beverage_orders[key] * cold_beverage[key]
    for drink in cold_beverage_bill:
        print(f'{drink} : {cold_beverage_bill[drink]}')
    pizza_bill = dict()
    if len(pizza_orders)!=0:
        print("************")
    for key in set(pizza.keys()) and set(pizza_orders.keys()):
        pizza_bill[key] = pizza_orders[key] * pizza[key]
    for pizzas in pizza_bill:
        print(f'{pizzas} : {pizza_bill[pizzas]}')
    soup_bill = dict()
    if len(soup_orders)!=0:
        print("************")
    for key in set(soup.keys()) and set(soup_orders.keys()):
        soup_bill[key] = soup_orders[key] * soup[key]
    for soups in soup_bill:
        print(f'{soups} : {soup_bill[soups]}')
    dessert_bill = dict()
    if len(dessert_orders)!=0:
        print("************")
    for key in set(dessert.keys()) and set(dessert_orders.keys()):
        dessert_bill[key] = dessert_orders[key] * dessert[key]
    for desserts in dessert_bill:
        print(f'{desserts} : {dessert_bill[desserts]}')
    fresh_juice_bill = dict()
    if len(fresh_juice_orders)!=0:
        print("************")
    for key in set(fresh_juice.keys()) and set(fresh_juice_orders.keys()):
        fresh_juice_bill[key] = fresh_juice_orders[key] * fresh_juice[key]
    for juices in fresh_juice_bill:
        print(f'{juices} : {fresh_juice_bill[juices]}')
    print("************")
    total_meal_bill = 0
    total_hot_beverage_bill = 0
    total_cold_beverage_bill = 0
    total_pizza_bill = 0
    total_soup_bill = 0
    total_dessert_bill = 0
    total_fresh_juice_bill = 0
    meal_bill_list = meal_bill.values()
    hot_beverage_bill_list = hot_beverage_bill.values()
    cold_beverage_bill_list = cold_beverage_bill.values()
    pizza_bill_list = pizza_bill.values()
    soup_bill_list = soup_bill.values()
    dessert_bill_list = dessert_bill.values()
    fresh_juice_bill_list = fresh_juice_bill.values()
    for item1 in meal_bill_list:
        total_meal_bill += item1
    for item2 in hot_beverage_bill_list:
        total_hot_beverage_bill += item2
    for item3 in cold_beverage_bill_list:
        total_cold_beverage_bill += item3
    for item4 in pizza_bill_list:
        total_pizza_bill += item4
    for item5 in soup_bill_list:
        total_soup_bill += item5
    for item6 in dessert_bill_list:
        total_dessert_bill += item6
    for item7 in fresh_juice_bill_list:
        total_fresh_juice_bill += item7
    total = total_hot_beverage_bill + total_meal_bill + total_cold_beverage_bill + total_pizza_bill + total_soup_bill + total_dessert_bill + total_fresh_juice_bill
    print(f'TOTAL :  {total}')


def add_new():
    print(''' .......What Do You Want To Add.......
    ''', menu_type)
    while True:
        choice = input('Enter your choice: ').upper()
        if choice == "1":
            food = input('enter food: ').upper()
            price = (input('enter price:'))
            if check_parameter(food, meal) == 'true':
                print('The meal already exist.')
            else:
                try:
                    price = eval(price)
                    meal[food] = price
                    print(completed)
                except:
                    print("invalid input. please enter numbers only for price.")
        elif choice == "2":
            hot_drink = input('enter a hot drink: ').upper()
            price = (input('enter price: '))
            if check_parameter(hot_drink, hot_beverage) == 'true':
                print(' The drink already exist ')
            else:
                try:
                    price = eval(price)
                    hot_beverage[hot_drink] = price
                    print(completed)
                except:
                    print("invalid input. please enter numbers only for price.")
        elif choice == "3":
            cold_drink = input('enter a cold drink: ').upper()
            price = (input('enter price: '))
            if check_parameter(cold_drink, cold_beverage) == 'true':
                print(' The drink already exist ')
            else:
                try:
                    price = eval(price)
                    cold_beverage[cold_drink] = price
                    print(completed)
                except:
                    print("invalid input. please enter numbers only for price.")
        elif choice == "4":
            pizzaa = input('enter a pizza: ').upper()
            price = (input('enter price: '))
            if check_parameter(pizzaa, pizza) == 'true':
                print(' The pizza already exist ')
            else:
                try:
                    price = eval(price)
                    hot_beverage[pizza] = price
                    print(completed)
                except:
                    print("invalid input. please enter numbers only for price.")
        elif choice == "5":
            soupr = input('enter a soup: ').upper()
            price = (input('enter price: '))
            if check_parameter(soupr, soup) == 'true':
                print(' The soup already exist ')
            else:
                try:
                    price = eval(price)
                    soup[soupr] = price
                    print(completed)
                except:
                    print("invalid input. please enter numbers only for price.")
        elif choice == "6":
            dessertt = input('enter a dessert: ').upper()
            price = (input('enter price: '))
            if check_parameter(dessertt, dessert) == 'true':
                print(' The dessert already exist ')
            else:
                try:
                    price = eval(price)
                    dessert[dessertt] = price
                    print(completed)
                except:
                    print(' The dessert already exist ')
        elif choice == "7":
            juicee = input('enter a fresh juice: ').upper()
            price = (input('enter price: '))
            if check_parameter(juicee, fresh_juice) == 'true':
                print(' The drink already exist ')
            else:
                try:
                    price = eval(price)
                    fresh_juice[juicee] = price
                    print(completed)
                except:
                    print("invalid input. please enter numbers only for price.")
        elif choice == '8':
            break
        else:
            print('invalid input.')
        print('''.........Do you Wanna Add Another........
        ''', '\n', menu_type)


def remove():
    print(''' .......What Do You Want To Remove.......
    ''', menu_type)
    while True:
        choice = input('Enter your choice: ').upper()
        if choice == "1":
            food = input('enter food: ').upper()
            if check_parameter(food, meal) == 'true':
                del (meal[food])
                print(completed)
            else:
                print("This meal does not exist.")
        elif choice == '2':
            hot_drink = input('enter a hot drink: ').upper()
            if check_parameter(hot_drink, hot_beverage) == 'true':
                del (hot_beverage[hot_drink])
                print(completed)
            else:
                print("This hot beverage does not exist.")
        elif choice == "3":
            cold_drink = input('enter a cold drink: ').upper()
            if check_parameter(cold_drink, cold_beverage) == 'true':
                del (cold_beverage[cold_drink])
                print(completed)
            else:
                print("This cold beverage does not exist.")
        elif choice == "4":
            pizzaa = input('enter a pizza: ').upper()
            if check_parameter(pizzaa, pizza) == 'true':
                del (pizza[pizzaa])
                print(completed)
            else:
                print("This pizza does not exist.")
        elif choice == "5":
            soupp = input('enter a soup: ').upper()
            if check_parameter(soupp, soup) == 'true':
                del (soup[soupp])
                print(completed)
            else:
                print("This soup does not exist.")
        elif choice == "6":
            dessertt = input('enter a dessert: ').upper()
            if check_parameter(dessertt, dessert) == 'true':
                del (dessert[dessertt])
                print(completed)
            else:
                print("This dessert does not exist.")
        elif choice == "7":
            juicee = input('enter a hot drink: ').upper()
            if check_parameter(juicee, fresh_juice) == 'true':
                del (fresh_juice[juicee])
                print(completed)
            else:
                print("This juice does not exist.")
        elif choice == '8':
            break
        else:
            print('invalid')
        print('''.........Do you Wanna Remove Another........
                ''', '\n', menu_type)


def update():
    print(''' .......What Do You Want To Update.......
    ''', menu_type)
    while True:
        choice = input('Enter your choice:').upper()
        if choice == '1':
            while True:
                update_opt_print('Meal')
                opt = input("Enter your choice: ")
                if opt == "1":
                    old_meal_name = (input("Enter Name of the meal you want to Update: ")).upper()
                    new_meal_name = (input("Enter The New Name : ")).upper()
                    if check_parameter(old_meal_name, meal) == "true":
                        meal[new_meal_name] = meal.pop(old_meal_name)
                        print(completed)
                    else:
                        print("This is Meal does not exist")
                elif opt == "2":
                    old_meal_name = (input("Enter Name of the meal you want to Update: ")).upper()
                    new_meal_price = (input("Enter The updated price : "))
                    if check_parameter(old_meal_name, meal) == "true":
                        try:
                            new_meal_price = eval(new_meal_price)
                            meal[old_meal_name] = new_meal_price
                            print(completed)
                        except:
                            print("invalid input. please enter numbers only for price.")

                    else:
                        print("This is Meal does not exist .")

                elif opt == "3":
                    keys = input("Enter name of the food you want to update: ").upper()
                    food_name = (input("Enter the new food name: ")).upper()
                    food_price = (input("Enter the new price: "))
                    if check_parameter(keys, meal) == 'true':
                        del meal[keys]
                        try:
                            del meal[keys]
                            food_price = eval(food_price)
                            meal[food_name] = food_price
                            print(completed)
                        except:
                            print("invalid input. please enter numbers only for price.")
                    else:
                        print("This is Meal does not exist .")

                elif opt == "4":
                    break
                else:
                    print("Invalid Input"
                          "")

        elif choice == '2':
            while True:
                update_opt_print('hot drink')
                opt = input("Enter your choice: ")
                if opt == "1":
                    old_hot_drink_name = (input("Enter Name of the hot drink you want to Update: ")).upper()
                    new_hot_drink_name = (input("Enter The New Name : ")).upper()
                    if check_parameter(old_hot_drink_name, hot_beverage) == "true":
                        hot_beverage[new_hot_drink_name] = hot_beverage.pop(old_hot_drink_name)
                        print(completed)
                    else:
                        print("This Hot Drink does not exist")
                elif opt == "2":
                    old_hot_drink_name = (input("Enter Name of the hot drink you want to Update: ")).upper()
                    new_hot_drink_price = (input("Enter The updated price : "))
                    if check_parameter(old_hot_drink_name, hot_beverage) == "true":
                        try:
                            new_hot_drink_price = eval(new_hot_drink_price)
                            meal[old_hot_drink_name] = new_hot_drink_price
                            print(completed)
                        except:
                            print("invalid input. please enter numbers only for price.")

                    else:
                        print("This is hot drink does not exist .")

                elif opt == "3":
                    keys = input("Enter name of the hot drink you want to update: ").upper()
                    hot_drink_name = (input("Enter the new hot drink name: ")).upper()
                    hot_drink_price = (input("Enter the new price: "))
                    if check_parameter(keys, hot_beverage) == 'true':
                        try:
                            del hot_beverage[keys]
                            hot_drink_price = eval(hot_drink_price)
                            hot_beverage[hot_drink_name] = hot_drink_price
                            print(completed)
                        except:
                            print("invalid input. please enter numbers only for price.")
                    else:
                        print("This hot drink does not exist .")

                elif opt == "4":
                    break
                else:
                    print("Invalid Input"
                          "")
        elif choice == '3':
            while True:
                update_opt_print('cold drink')
                opt = input("Enter your choice: ")
                if opt == "1":
                    old_cold_drink_name = (input("Enter Name of the cold drink you want to Update: ")).upper()
                    new_cold_drink_name = (input("Enter The New Name : ")).upper()
                    if check_parameter(old_cold_drink_name, cold_beverage) == "true":
                        cold_beverage[new_cold_drink_name] = cold_beverage.pop(old_cold_drink_name)
                        print(completed)
                    else:
                        print("This Cold Drink does not exist")
                elif opt == "2":
                    old_cold_drink_name = (input("Enter Name of the cold drink you want to Update: ")).upper()
                    new_cold_drink_price = (input("Enter The updated price : "))
                    if check_parameter(old_cold_drink_name, cold_beverage) == "true":
                        try:
                            new_cold_drink_price = eval(new_cold_drink_price)
                            meal[old_cold_drink_name] = new_cold_drink_price
                            print(completed)
                        except:
                            print("invalid input. please enter numbers only for price.")

                    else:
                        print("This cold drink does not exist .")

                elif opt == "3":
                    keys = input("Enter name of the cold drink you want to update: ").upper()
                    cold_drink_name = (input("Enter the new cold drink name: ")).upper()
                    cold_drink_price = (input("Enter the new price: "))
                    if check_parameter(keys, cold_beverage) == 'true':
                        try:
                            del cold_beverage[keys]
                            cold_drink_price = eval(cold_drink_price)
                            cold_beverage[cold_drink_name] = cold_drink_price
                            print(completed)
                        except:
                            print("invalid input. please enter numbers only for price.")
                    else:
                        print("This cold drink does not exist .")

                elif opt == "4":
                    break
                else:
                    print("Invalid Input"
                          "")
        elif choice == '4':
            while True:
                update_opt_print('pizza')
                opt = input("Enter your choice: ")
                if opt == "1":
                    old_pizza_name = (input("Enter Name of the pizza you want to Update: ")).upper()
                    new_pizza_name = (input("Enter The New Name : ")).upper()
                    if check_parameter(old_pizza_name, pizza) == "true":
                        pizza[new_pizza_name] = pizza.pop(old_pizza_name)
                        print(completed)
                    else:
                        print("This is Pizza does not exist")
                elif opt == "2":
                    old_pizza_name = (input("Enter Name of the pizza you want to Update: ")).upper()
                    new_pizza_price = (input("Enter The updated price : "))
                    if check_parameter(old_pizza_name, pizza) == "true":
                        try:
                            new_pizza_price = eval(new_pizza_price)
                            dessert[old_pizza_name] = new_pizza_price
                            print(completed)
                        except:
                            print("invalid input. please enter numbers only for price.")

                    else:
                        print("This is Pizza does not exist .")

                elif opt == "3":
                    keys = input("Enter name of the pizza you want to update: ").upper()
                    pizza_name = (input("Enter the new pizza name: ")).upper()
                    pizza_price = (input("Enter the new price: "))
                    if check_parameter(keys, pizza) == 'true':
                        del pizza[keys]
                        try:
                            del pizza[keys]
                            pizza_price = eval(pizza_price)
                            pizza[pizza_name] = pizza_price
                            print(completed)
                        except:
                            print("invalid input. please enter numbers only for price.")
                    else:
                        print("This is Pizza does not exist .")

                elif opt == "4":
                    break
                else:
                    print("Invalid Input"
                          "")

        elif choice == '5':
            while True:
                update_opt_print('soup')
                opt = input("Enter your choice: ")
                if opt == "1":
                    old_soup_name = (input("Enter Name of the soup you want to Update: ")).upper()
                    new_soup_name = (input("Enter The New Name : ")).upper()
                    if check_parameter(old_soup_name, pizza) == "true":
                        soup[old_soup_name] = pizza.pop(new_soup_name)
                        print(completed)
                    else:
                        print("This is Soup does not exist")
                elif opt == "2":
                    old_soup_name = (input("Enter Name of the soup you want to Update: ")).upper()
                    new_soup_price = (input("Enter The updated price : "))
                    if check_parameter(old_soup_name, soup) == "true":
                        try:
                            new_soup_price = eval(new_soup_price)
                            meal[old_soup_name] = new_soup_price
                            print(completed)
                        except:
                            print("invalid input. please enter numbers only for price.")

                    else:
                        print("This is soup does not exist .")

                elif opt == "3":
                    keys = input("Enter name of the soup you want to update: ").upper()
                    soup_name = (input("Enter the new soup name: ")).upper()
                    soup_price = (input("Enter the new price: "))
                    if check_parameter(keys, soup) == 'true':
                        try:
                            del soup[keys]
                            soup_price = eval(soup_price)
                            soup[soup_name] = soup_price
                            print(completed)
                        except:
                            print("invalid input. please enter numbers only for price.")
                    else:
                        print("This is Soup does not exist .")

                elif opt == "4":
                    break
                else:
                    print("Invalid Input"
                          "")
        elif choice == '6':
            while True:
                update_opt_print('Dessert')
                opt = input("Enter your choice: ")
                if opt == "1":
                    old_dessert_name = (input("Enter Name of the Dessert you want to Update: ")).upper()
                    new_dessert_name = (input("Enter The New Name : ")).upper()
                    if check_parameter(old_dessert_name, dessert) == "true":
                        dessert[new_dessert_name] = dessert.pop(old_dessert_name)
                        print(completed)
                    else:
                        print("This Dessert does not exist")
                elif opt == "2":
                    old_dessert_name = (input("Enter Name of the pizza you want to Update: ")).upper()
                    new_dessert_price = (input("Enter The updated price : "))
                    if check_parameter(old_dessert_name, dessert) == "true":
                        try:
                            new_dessert_price = eval(new_dessert_price)
                            dessert[old_dessert_name] = new_dessert_price
                            print(completed)
                        except:
                            print("invalid input. please enter numbers only for price.")

                    else:
                        print("This is Dessert does not exist .")

                elif opt == "3":
                    keys = input("Enter name of the dessert you want to update: ").upper()
                    dessert_name = (input("Enter the new dessert name: ")).upper()
                    dessert_price = (input("Enter the new price: "))
                    if check_parameter(keys, dessert) == 'true':
                        del dessert[keys]
                        try:
                            del dessert[keys]
                            dessert_price = eval(dessert_price)
                            dessert[dessert_name] = dessert_price
                            print(completed)
                        except:
                            print("invalid input. please enter numbers only for price.")
                    else:
                        print("This is Dessert does not exist .")

                elif opt == "4":
                    break
                else:
                    print("Invalid Input"
                          "")

        elif choice == '7':
            while True:
                update_opt_print('fresh juice')
                opt = input("Enter your choice: ")
                if opt == "1":
                    old_fresh_juice_name = (input("Enter Name of the fresh juice you want to Update: ")).upper()
                    new_fresh_juice_name = (input("Enter The New Name : ")).upper()
                    if check_parameter(old_fresh_juice_name, fresh_juice) == "true":
                        fresh_juice[new_fresh_juice_name] = fresh_juice.pop(old_fresh_juice_name)
                        print(completed)
                    else:
                        print("This Fresh Juice does not exist")
                elif opt == "2":
                    old_fresh_juice_name = (input("Enter Name of the fresh juice you want to Update: ")).upper()
                    new_fresh_juice_price = (input("Enter The updated price : "))
                    if check_parameter(old_fresh_juice_name, fresh_juice) == "true":
                        try:
                            new_fresh_juice_price = eval(new_fresh_juice_price)
                            fresh_juice[old_fresh_juice_name] = new_fresh_juice_price
                            print(completed)
                        except:
                            print("invalid input. please enter numbers only for price.")

                    else:
                        print("This is hot drink does not exist .")

                elif opt == "3":
                    keys = input("Enter name of the fresh juice you want to update: ").upper()
                    fresh_juice_name = (input("Enter the new fresh juice name: ")).upper()
                    fresh_juice_price = (input("Enter the new price: "))
                    if check_parameter(keys, hot_beverage) == 'true':
                        try:
                            del fresh_juice[keys]
                            fresh_juice_price = eval(fresh_juice_price)
                            fresh_juice[fresh_juice_name] = fresh_juice_price
                            print(completed)
                        except:
                            print("invalid input. please enter numbers only for price.")
                    else:
                        print("This fresh juice does not exist .")

                elif opt == "4":
                    break
                else:
                    print("Invalid Input"
                          "")

        elif choice == '8':
            break
        else:
            print("invalid input!")
        print('''.........Do you Want Update Another........
                ''', '\n', menu_type)


def list_food():
    print('    meal menu'.upper())
    for food in meal:
        print(f'  {food} : {meal[food]} birr')
    print('*' * 36)
    print('*' * 36)
    print('  cold beverage menu'.upper())
    for cold_drink in cold_beverage:
        print(f'  {cold_drink} : {cold_beverage[cold_drink]} birr')
    print('*'*36)
    print('*' * 36)
    print('  hot beverage menu'.upper())
    for hot_drink in hot_beverage:
        print(f'  {hot_drink} : {hot_beverage[hot_drink]} birr')
    print('*'*36)
    print('*' * 36)
    print('  pizza menu'.upper())
    for pizzaa in pizza:
        print(f'  {pizzaa} : {pizza[pizzaa]} birr')
    print('*'*36)
    print('*' * 36)
    print('  soup menu'.upper())
    for soupp in soup:
        print(f'  {soupp} : {soup[soupp]} birr')
    print('*'*36)
    print('*' * 36)
    print('  dessert menu'.upper())
    for dessertt in dessert:
        print(f'  {dessertt} : {dessert[dessertt]} birr')
    print('*'*36)
    print('*' * 36)
    print('  fresh juice menu'.upper())
    for juicee in fresh_juice:
        print(f'  {juicee} : {fresh_juice[juicee]} birr')


def order_list():
    if len(meal_orders) != 0:
        print('meal order'.upper())
        print('order : amount ')
    for food in meal_orders:
        print(food, ":", meal_orders[food])
    if len(cold_beverage_orders) != 0:
        print('*'*36)
        print('*' * 36)
        print('cold beverage order'.upper())
        print('order : amount ')
    for cold_drink in cold_beverage_orders:
        print(cold_drink, ":", cold_beverage_orders[cold_drink])
    if len(hot_beverage_orders) != 0:
        print('*'*36)
        print('*' * 36)
        print('hot beverage order'.upper())
        print('order : amount ')
    for hot_drink in hot_beverage_orders:
        print(hot_drink, ":", hot_beverage_orders[hot_drink])
    if len(pizza_orders) != 0:
        print('*' * 36)
        print('*' * 36)
        print('pizza order'.upper())
        print('order : amount ')
    for pizzaa in pizza_orders:
        print(pizzaa, ":", pizza_orders[pizzaa])
    if len(soup_orders) != 0:
        print('*' * 36)
        print('*' * 36)
        print('soup order'.upper())
        print('order : amount ')
    for soupp in soup_orders:
        print(soupp, ":", soup_orders[soupp])
    if len(dessert_orders) != 0:
        print('*'*36)
        print('*' * 36)
        print('dessert order'.upper())
        print('order : amount ')
    for dessertt in dessert_orders:
        print(dessertt, ":", dessert_orders[dessertt])
    if len(fresh_juice_orders) != 0:
        print('*' * 36)
        print('*' * 36)
        print('fresh juice order'.upper())
        print('order : amount ')
    for juicee in fresh_juice_orders:
        print(juicee, ":", fresh_juice_orders[juicee])


def order():
    opts = ('''
       What do you want to order.

          [1] for meal menu
          [2] for hot beverage menu
          [3] for cold beverage menu
          [4] for pizza menu
          [5] for soup menu
          [6] for dessert menu
          [7] for fresh juice menu
          [8] to go back
          ''')
    print(opts)
    print('''
          For customers who order at least 3 orders at once, we have a special prize!
    ''')
    meal_orders_count = 0
    hot_beverage_orders_count = 0
    cold_beverage_orders_count = 0
    pizza_orders_count = 0
    soup_orders_count = 0
    dessert_orders_count = 0
    fresh_juice_orders_count = 0
    total_count = 0
    while True:
        choice = input('Enter your choice :').upper()
        if choice == '1':
            while True:
                order = input('Enter food: ').upper()
                if order in meal:
                    meal_orders[order] = meal_orders.get(order, 0) + 1
                    meal_orders_count += 1
                else:
                    print(f'{" sorry, we do not have that food, please order again ":.^20} ')

                print(''' DO YOU WANT ORDER A MEAL AGAIN 

                        [1] YES
                        [2] NO, Go Back
                ''')
                opt = input("Enter your preference: ")
                while True:
                    if opt == '1':
                        break
                    elif opt == '2':
                        break
                    else:

                        print("invalid input.")
                        opt = input("Enter your preference again: ")
                if opt == '2':
                    break

        elif choice == '2':
            while True:
                order = input('enter a hot drink: ').upper()
                if order in hot_beverage:
                    hot_beverage_orders[order] = hot_beverage_orders.get(order, 0) + 1
                    hot_beverage_orders_count += 1
                else:
                    print('we do not have that drink, please order again ')
                print('''

                    DO YOU WANT ORDER A HOT DRINK AGAIN 

                             [1] YES
                             [2] NO, Go Back
                                ''')
                opt = input("Enter your preference:")
                while True:
                    if opt == '1':
                        break
                    elif opt == '2':
                        break
                    else:

                        print("invalid input.")
                        opt = input("Enter your preference again: ")
                if opt == '2':
                    break
        elif choice == '3':
            while True:
                order = input('enter a cold drink: ').upper()
                if order in cold_beverage:
                    cold_beverage_orders[order] = cold_beverage_orders.get(order, 0) + 1
                    cold_beverage_orders_count += 1
                else:
                    print('we do not have that drink, please order again ')
                print('''

                                DO YOU WANT ORDER A COLD DRINK AGAIN 

                                         [1] YES
                                         [2] NO, Go Back
                                            ''')
                opt = input("Enter your preference:")
                while True:
                    if opt == '1':
                        break
                    elif opt == '2':
                        break
                    else:

                        print("invalid input.")
                        opt = input("Enter your preference again: ")
                if opt == '2':
                    break
        elif choice == '4':
            while True:
                order = input('enter a pizza: ').upper()
                if order in pizza:
                    pizza_orders[order] = pizza_orders.get(order, 0) + 1
                    pizza_orders_count += 1
                else:
                    print('we do not have that drink, please order again ')
                print('''

                                DO YOU WANT ORDER A PIZZA AGAIN 

                                         [1] YES
                                         [2] NO, Go Back
                                            ''')
                opt = input("Enter your preference:")
                while True:
                    if opt == '1':
                        break
                    elif opt == '2':
                        break
                    else:

                        print("invalid input.")
                        opt = input("Enter your preference again: ")
                if opt == '2':
                    break
        elif choice == '5':
            while True:
                order = input('enter a soup: ').upper()
                if order in soup:
                    soup_orders[order] = soup_orders.get(order, 0) + 1
                    soup_orders_count += 1
                else:
                    print('we do not have that soup, please order again ')
                print('''

                                DO YOU WANT ORDER A HOT DRINK AGAIN 

                                         [1] YES
                                         [2] NO, Go Back
                                            ''')
                opt = input("Enter your preference:")
                while True:
                    if opt == '1':
                        break
                    elif opt == '2':
                        break
                    else:

                        print("invalid input.")
                        opt = input("Enter your preference again: ")
                if opt == '2':
                    break
        elif choice == '6':
            while True:
                order = input('enter a dessert: ').upper()
                if order in dessert:
                    dessert_orders[order] = dessert_orders.get(order, 0) + 1
                    dessert_orders_count += 1
                else:
                    print('we do not have that dessert, please order again ')
                print('''

                                DO YOU WANT ORDER A DESSERT AGAIN 

                                         [1] YES
                                         [2] NO, Go Back
                                            ''')
                opt = input("Enter your preference:")
                while True:
                    if opt == '1':
                        break
                    elif opt == '2':
                        break
                    else:

                        print("invalid input.")
                        opt = input("Enter your preference again: ")
                if opt == '2':
                    break
        elif choice == '7':
            while True:
                order = input('enter a fresh juice: ').upper()
                if order in fresh_juice:
                    fresh_juice_orders[order] = fresh_juice_orders.get(order, 0) + 1
                    fresh_juice_orders_count += 1
                else:
                    print('we do not have that juice, please order again ')
                print('''

                                DO YOU WANT ORDER A FRESH JUICE AGAIN 

                                         [1] YES
                                         [2] NO, Go Back
                                            ''')
                opt = input("Enter your preference:")
                while True:
                    if opt == '1':
                        break
                    elif opt == '2':
                        break
                    else:

                        print("invalid input.")
                        opt = input("Enter your preference again: ")
                if opt == '2':
                    break
        elif choice == '8':
            break
        else:
            print('invalid input')
        print(opts)
    total_count = meal_orders_count + hot_beverage_orders_count + cold_beverage_orders_count + pizza_orders_count + soup_orders_count + dessert_orders_count + fresh_juice_orders_count
    if total_count >= 3:
        print('''
                your order is taken.
                guess a number to win a prize
                ''')
        lottery()
        bill()
    elif total_count == 1 or total_count == 2:
        print('''
               your order is taken.
               Thank you for using our service.
        ''')
        bill()
    else:
        print("                You DID NOT ORDER ANYTHING")


def admin():
    print(
        '''
                 OPTIONS

                [1] Add
                [2] Remove
                [3] Update
                [4] list
                [5] interface
                [6] orders
                [0] Exit

        ''')
    option = input("Select an option: ")

    opt = '''

                 OPTIONS

                [1] Add
                [2] Remove
                [3] Update
                [4] list
                [5] Interface
                [6] orders
                [0] Exit

        '''
    while option != "0":
        if option == "1":
            add_new()
            print(opt)
        elif option == "2":
            remove()
            print(opt)
        elif option == "3":
            update()
            print(opt)
        elif option == "4":
            list_food()
            print(opt)
        elif option == "5":
            digital_menu()
        elif option == "6":
            order_list()
            print(opt)

        else:
            print("Invalid option.")

        option = input("Select an option: ")

    if option == "0":
        print(close_text)
        exit()


def costumer():
    print('''
     welcome to our digital menu!!

        Menu Option 

        1: View food list
        2: Order food
        3: Interface
        0: exit

    ''')
    opts = ('''
        Menu Option 

        1: View food list
        2: Order food
        3: Interface
        0: exit

    ''')
    options = input("Select an option: ")
    while options != "0":
        if options == "1":
            list_food()
            print('''
            ''')
            print(opts)
        elif options == "2":
            order()
            print('''
            ''')
            print(opts)
        elif options == "3":
            digital_menu()
        else:
            print("Invalid Option. Try again!")
            print('''
            ''')
            print(opts)
        options = input("Select an option: ")
    if options == "0":
        print(close_text)
        exit()


def digital_menu():
    print('''
    WELCOME TO OUR DIGITAL RESTAURANT MENU

            INTERFACES

        [1] Admin
        [2] Costumer
        [0] exit

    '''

          )
    inter = input("Select an interface: ")
    while inter != "0":
        if inter == "1":
            i = 0
            for i in range(3):

                password = input("Enter the password: ")
                if password == "1234":
                    admin()
                else:
                    print("Incorrect  Password. Try again!", 2 - i, " trials left")
                i += 1
            if i >= 3:
                return digital_menu()

        elif inter == "2":
            costumer()
        else:
            print("Invalid option. Try again! ")
            print('''

                    INTERFACES

                    [1] Admin
                    [2] Costumer
                    [0] exit
                    ''')
            inter = input("Select an interface: ")
    print(close_text)


digital_menu()
