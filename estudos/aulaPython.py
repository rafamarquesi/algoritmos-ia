# Comeco de um script
fruits = ['apple', 'banana', 'pear', 'orange']
for fruit in fruits:
    print(fruit + ' for sale')

fruiPrices = {'apple':2.0, 'orange':3.0, 'banana':5.0}
for fruit, price in fruiPrices.items():
    if price > 2:
        print('It is very expensive!')
    print('%s cost %.2f a kilogram!' % (fruit, price))

# for i in range(0, len(fruiPrices)):
#     print('%s cost %.2f a kilogram!' % fruiPrices.items()[i])