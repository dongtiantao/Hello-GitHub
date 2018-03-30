def make_pizza(*toppings):
    '''打印顾客点的所有配料'''
    for topping in toppings:
        print('--'+topping)


make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')