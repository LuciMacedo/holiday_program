cd


#user input destination and validations for the inputs
while True:
    city_flight = str(input('''
        [1] Rio de Janeiro - £518.00
        [2] Miami - £432.00
        [3] Greece - £155.00
        [4] Spain - £73.00
        Enter the city: '''))
    if city_flight in '1234':
        break
    else:
        print('=' * 60)
        print('Enter a valid option!')
        print('=' * 60)

#user input hotel and validations for the inputs
while True:
    try:
        num_nights = int(input('Enter the number of night: '))
    except ValueError:
        print('=' * 60)
        print('Enter a valid number!')
        print('=' * 60)
    else:
        break

#user input rental car and validations for the inputs
while True:
    try:
        rental_days = int(input('Enter the number of days for renting: '))
    except ValueError:
        print('=' * 60)
        print('Enter a valid number!')
        print('=' * 60)
    else:
        break

# prices for the hotel and rental car
hotel_price = int(90.00)
rental_price = float(45.00)

# function to calculate the hotel cost
def hotel_cost(num_nights):
    return num_nights * hotel_price

# function to calculate teh rental car
def car_rental(rental_days):
    return rental_days * rental_price

# function to calculate the flight
def plane_cost(city_flight):
    match city_flight:
        case '1':
            return 518
        case '2':
            return 432
        case '3':
            return 155
        case '4':
            return 73


# function to calculate total cost of the holiday
def holiday_cost(flight, rental, nights):
    total_holiday_cost = flight + rental + nights
    return f'The total amount for the HOLIDAY is {total_holiday_cost:.2f}'

# store in variables
hotel = (hotel_cost(num_nights))
car = (car_rental(rental_days))
plane = (plane_cost(city_flight))
print('=' * 60)
# printing the amount for the costs
print(f'The cost of the TICKET is {plane:.2f}')
print(f'The cost of the HOTEL is {hotel:.2f}')
print(f'The cost of the RENTAL CAR is {car:.2f}')
print(holiday_cost(hotel, car, plane))
print('=' * 60)
