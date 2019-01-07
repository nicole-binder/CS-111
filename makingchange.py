price_string =  input('Price? ')
rendered_string = input('Amount Tendered? ')

price = float(price_string)
rendered = float(rendered_string)

cents = price*100
rendered_cents = rendered*100
change = rendered_cents - cents
money = change/100

ones = int(change/100)
quarters = int((change - 100*ones)/25)
dimes = int((change - ones*100 - quarters*25)/10)
nickels = int((change - ones*100 - quarters*25 - dimes*10)/5)
pennies = int((change - ones*100 - quarters*25 - dimes*10 - nickels*5))

if money < 10:
    message_to_print = '${0:.2}'.format(money)
    print('Change: ', message_to_print,)
if money > 100:
    message_to_print = '${0:.4}'.format(money)
    print('Change: ', message_to_print,)
else:
    message_to_print = '${0:.3}'.format(money)
    print('Change: ', message_to_print,)


if ones == 1:
    print( ones, 'one-dollar bill')
else:
    print( ones, 'one-dollar bills')
if quarters == 1:
    print( quarters, 'quarter')
else:
    print( quarters, 'quarters')
if dimes == 1:
    print( dimes, 'dime')
else:
    print( dimes, 'dimes')
if nickels == 1:
    print( nickels, 'nickel')
else:
    print( nickels, 'nickels')
if pennies == 1:
    print( pennies, 'penny')
else:
    print( pennies, 'pennies')
