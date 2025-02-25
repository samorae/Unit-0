province = {
    'A':'Newfoundland', 
    'B': 'Nova Scotia', 
    'C': 'Prince Edward Island',
    'E': 'New Brunswick',
    'Quebec': 'G' or 'H' or 'J',
    'Ontario':'K'or'L'or'M'or'N'or'P',
    'R': 'Manitoba',
    'S': 'Saskatchewan',
    'T': 'Alberta',
    'V': 'British Columbia',
    'X': 'Nunavut'or'Northwest Territories', 
    'Y': 'Yukon' } 
user_code = input('What is your poastal code?: ').upper()

if user_code[0] == 'A':
    print(f'Your poastal code is {province["A"]}')
elif user_code[0] == 'B':
    print(f'Your poastal code is {province["B"]}')
elif user_code[0] == 'C':
    print(f'Your poastal code is {province["C"]}')
elif user_code[0] == 'E':
    print(f'Your poastal code is {province["E"]}')
elif user_code[0] == 'G' or 'H' or 'J':
    province = 'Quebec'
    print(f'Your poastal code is {province}')
elif user_code[0] == 'K' or 'L' or 'M' or 'N' or 'P':
    province = "Ontario"
    print(f'Your poastal code is {province}')
elif user_code[0] == 'R':
    print(f'Your poastal code is {province["R"]}')
elif user_code[0] == 'S':
    print(f'Your poastal code is {province["S"]}')
elif user_code[0] == 'T':
    print(f'Your poastal code is {province["T"]}')
elif user_code[0] == 'V':
    print(f'Your poastal code is {province["V"]}')
elif user_code[0] == 'X':
    print(f'Your poastal code is {province["X"]}')
elif user_code[0] == 'Y':
    print(f'Your poastal code is {province["Y"]}')
else: 
    print('Invalid poastal code')
