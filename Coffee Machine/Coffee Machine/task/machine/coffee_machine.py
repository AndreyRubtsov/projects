# water = int(input('Write how many ml of water the coffee machine has:\n'))
# milk = int(input('Write how many ml of milk the coffee machine has\n'))
# beans = int(input('Write how many grams of coffee beans the coffee machine has:\n'))
# cups = int(input('Write how many cups of coffee you will need:\n'))
# water_need = int(water / 200)
# milk_need = int(milk / 50)
# beans_need = int(beans / 15)
#
# num_cups = min(water_need, milk_need, beans_need)
#
# if num_cups == cups:
#     print('Yes, I can make that amount of coffee')
# elif num_cups > cups:
#     print('Yes, I can make that amount of coffee (and even ' + str(num_cups - cups) + ' more than that)')
# else:
#     print('No, I can make only ' + str(num_cups) + ' cups of coffee')

class CoffeMaschine():

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.disposable_cups = 9
        self.money = 550

    def print_machine(self):
        print(f'The coffee machine has:\n{self.water} of water\n{self.milk} of milk'
              f'\n{self.beans} of coffee beans\n{self.disposable_cups} of disposable cups\n'
              f'{self.money} of money\n')

    def buy_cofe(self, choice):
        if choice == '1':
            if self.water < 250 or self.beans < 6 or self.disposable_cups < 1:
                print('Sorry, not enough water!')
            else:
                self.water -= 250
                self.beans -= 16
                self.disposable_cups -= 1
                self.money += 4
                print('I have enough resources, making you a coffee!')
        elif choice == '2':
            if self.water < 350 or self.beans < 20 or self.milk < 75 or self.disposable_cups < 1:
                print('Sorry, not enough water!')
            else:
                self.water -= 350
                self.beans -= 20
                self.milk -= 75
                self.disposable_cups -= 1
                self.money += 7
                print('I have enough resources, making you a coffee!')
        elif choice == '3':
            if self.water < 200 or self.beans < 12 or self.milk < 100 or self.disposable_cups < 1:
                print('Sorry, not enough water!')
            else:
                self.water -= 200
                self.beans -= 12
                self.milk -= 100
                self.disposable_cups -= 1
                self.money += 6
                print('I have enough resources, making you a coffee!')
        else:
            print("Wrong choice!")

    def fill_cofe(self):
        add_some = input('Write how many ml of water do you want to add:')
        self.water += int(add_some)
        add_some = input('Write how many ml of milk do you want to add:')
        self.milk += int(add_some)
        add_some = input('Write how many grams of coffee beans do you want to add:')
        self.beans += int(add_some)
        add_some = input('Write how many disposable cups of coffee do you want to add:')
        self.disposable_cups += int(add_some)

    def take_money(self):
        print('I gave you $' + str(self.money))
        self.money = 0

    def coffee_action(self):
        while True:
            choice = input('Write action (buy, fill, take, remaining, exit):')
            if choice == 'buy':
                buy_choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
                self.buy_cofe(buy_choice)
            elif choice == 'fill':
                self.fill_cofe()
            elif choice == 'take':
                self.take_money()
            elif choice == 'remaining':
                self.print_machine()
            elif choice == 'exit':
                break
            else:
                print("Wrong choice")
machine=CoffeMaschine()
machine.coffee_action()

#
# def print_machine():
#     print(f'The coffee machine has:\n{water} of water\n{milk} of milk'
#           f'\n{beans} of coffee beans\n{disposable_cups} of disposable cups\n'
#           f'{money} of money\n')
#
#
# def buy_cofe(choice):
#     global water
#     global milk
#     global beans, disposable_cups, money
#     if choice == '1':
#         if water < 250 or beans < 6 or disposable_cups < 1:
#             print('Sorry, not enough water!')
#         else:
#             water -= 250
#             beans -= 16
#             disposable_cups -= 1
#             money += 4
#             print('I have enough resources, making you a coffee!')
#     elif choice == '2':
#         if water < 350 or beans < 20 or milk < 75 or disposable_cups < 1:
#             print('Sorry, not enough water!')
#         else:
#             water -= 350
#             beans -= 20
#             milk -= 75
#             disposable_cups -= 1
#             money += 7
#             print('I have enough resources, making you a coffee!')
#     elif choice == '3':
#         if water < 200 or beans < 12 or milk < 100 or disposable_cups < 1:
#             print('Sorry, not enough water!')
#         else:
#             water -= 200
#             beans -= 12
#             milk -= 100
#             disposable_cups -= 1
#             money += 6
#             print('I have enough resources, making you a coffee!')
#     else:
#         print("Wrong choice!")
#
#
# def fill_cofe():
#     global water, milk, beans, disposable_cups, money
#
#     add_some = input('Write how many ml of water do you want to add:')
#     water += int(add_some)
#
#     add_some = input('Write how many ml of milk do you want to add:')
#     milk += int(add_some)
#     add_some = input('Write how many grams of coffee beans do you want to add:')
#     beans += int(add_some)
#     add_some = input('Write how many disposable cups of coffee do you want to add:')
#     disposable_cups += int(add_some)
#
#
# def take_money():
#     global money
#     print('I gave you $' + str(money))
#     money = 0
#
#
# while True:
#     choice = input('Write action (buy, fill, take, remaining, exit):')
#     if choice == 'buy':
#         buy_choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
#         buy_cofe(buy_choice)
#     elif choice == 'fill':
#         fill_cofe()
#     elif choice == 'take':
#         take_money()
#     elif choice == 'remaining':
#         print_machine()
#     elif choice == 'exit':
#         break
#     else:
#         print("Wrong choice")
