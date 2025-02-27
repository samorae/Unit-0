province = {
    'A': 'Newfoundland',
    'B': 'Nova Scotia',
    'C': 'Prince Edward Island',
    'E': 'New Brunswick',
    'G': 'Quebec','H': 'Quebec','J':'Quebec',
    'K':'Ontario','L': 'Ontario', 'M':'Ontario','N':'Ontario','P':'Ontario',
    'R': 'Manitoba',
    'S': 'Saskatchewan',
    'T': 'Alberta',
    'V': 'British Columbia',
    'X': 'Nunavut/Northwest Territories',
    'Y': 'Yukon' }

while True:
    user_code = input('Type your poastal code in the following format(*** ***): ').upper()
    if len(user_code) != 7:
        print("Invalid postal code format.")
        continue
   
    else:
        first = user_code[0]
        second = user_code[1]

        if first in province:
            location_type = second
            if location_type == '0':
                location_type = 'Rural'
            else:
                location_type = 'Urban'
            print(f'You typed {user_code.upper()}')
            print(f'The poastal code is a(n) {location_type} location, in {province[first]}')
            break
        else:
            print('There is no place with that poastal code')
            break