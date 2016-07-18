menu_entry = ['burger','french fries','hot dog','nachos cheese','milk shake','cookies']
price_menu = ['4.95$','2$','4$','3.95$','5$','3$']

print('Hello !\nWelcome to Bristled\'s Diner')
print('Here are our choices !' + str(menu_entry))
print('Please, choose your order :')

order_choice = input()

if order_choice == 'burger':
    print('You chosed a burger for : ' + (price_menu[0]))
elif order_choice == 'french fries':
    print('Yummy ! I love me some french fries. That\'ll be :' + (price_menu[1]))
elif order_choice == 'hot dog':
    print('You love slappin\' the sausage aren\'t you?\n The sausage will be yours for :' + (price_menu[2]))
elif order_choice == 'nachos cheese':
    print('Mmmmhhh you got me meltin\' ! That\'ll be :' + (price_menu[3]))
elif order_choice == 'milk shake':
    print('All creamy, no chunky ! GIVE ME MY MONEY !' 'That\'ll be :' + (price_menu[4]))
elif order_choice == 'cookies':
    print('All chunky. Only chocolate. ' + (price_menu[5]))
