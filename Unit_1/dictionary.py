alien_0 = {'color': 'green' }

alien_0['x-pos'] = 0
alien_0['y-pos'] = 0 
alien_0['speed'] = 'fast' 

if alien_0['speed'] == "fast":
    alien_0['x-pos'] += 3
    print(alien_0)
elif alien_0['speed'] == 'medium':
    alien_0['x-pos'] += 2
    print(alien_0)
elif alien_0['speed'] == 'slow':
    alien_0['x-pos'] += 1
    print(alien_0)
else:
    print(0)

print(f"New position: {alien_0['x-pos']}, {alien_0['y-pos']}")

alien_0['home planet'] = 'Neptune'
print(alien_0)

del alien_0['home planet']
print(alien_0)


alien_1 = {
    'color': 'blue', 
    'points': 10 ,
    'x-pos': 50 ,
    'y-pos': 30 , 
    'speed': 'fast'}

print(alien_1)