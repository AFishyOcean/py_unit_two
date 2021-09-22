name = input('Hi whats your name?')
print('Well hello', name)

fav_number = float(input('What is your favorite number?'))
as_big = (fav_number / 42)
print('Oh cool that is', as_big, 'times as big as my favorite number which is 42')

car = input('What would you say your dream car is?')
print('Sounds like a cool car')
car_price = float(input('How much do you think it would cost?'))
print('Well that\'s not exactly cheap is it')
mortgage_time = int(input('How many years do you think it would take you to pay off a loan for it?'))
percent_int = float(input('What do you think the annual interest would be? (In decimals please)'))
monthly_int = (percent_int / 12)
monthly_payment = ((car_price * monthly_int) / (1 - (1 + monthly_int) ** -mortgage_time))
total_payment = (monthly_payment * 12 * mortgage_time)

print('If you get this car with your predicted loan you would have to pay $', monthly_payment, 'each month.')
print('That will total $', total_payment)