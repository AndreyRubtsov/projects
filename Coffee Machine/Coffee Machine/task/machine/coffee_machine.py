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
