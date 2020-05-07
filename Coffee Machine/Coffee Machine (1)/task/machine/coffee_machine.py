water = int(input('Write how many ml of water the coffee machine has:\n'))
milk = int(input('Write how many ml of milk the coffee machine has\n'))
beans = int(input('Write how many grams of coffee beans the coffee machine has:\n'))
cups = int(input('Write how many cups of coffee you will need:\n'))
water_need = int(water / 200)
milk_need = int(milk / 50)
beans_need = int(beans / 15)

num_cups = min(water_need, milk_need, beans_need)

if num_cups == cups:
    print('Yes, I can make that amount of coffee')
elif num_cups > cups:
    print('Yes, I can make that amount of coffee (and even ' + str(num_cups - cups) + ' more than that)')
else:
    print('No, I can make only ' + str(num_cups) + ' cups of coffee')
