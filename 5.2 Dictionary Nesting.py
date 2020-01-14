print ("Nesting in Dictionary")
print ("\tList of Dictionary")
alien_0={
    'color' : 'green',
    'points' : 5
}

alien_1={
    'color' : 'yellow',
    'points' : 10
}

alien_2={
    'color' : 'red',
    'points' : 15
}

aliens = [alien_0,alien_1,alien_2]

i=-1
for alien in aliens:
    print(f"\t\talien{(i:=i+1)} = {alien}")

del aliens

print()
print ("\tRandom aliens")
##Empty list for storing random aliens
aliens = []

for alien_number in range(13):
    new_alien = {
        'color' : 'green',
        'points' : 5,
        'speed' : 'slow',
    }
    aliens.append(new_alien)

for alien in aliens[0:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[0:10]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens:
    print (f"\t\taliens = {alien}")
print ("\t\t...")


print (f"\tTotal number of aliens created = {len(aliens)}")

print()
print ("\tList in a Dictionary")
pizza = {
    'crust' : 'thick',
    'toppings' : ['cheese crust', 'jalpeno', 'tomatino sauce']
}
print (f"\t\tYou ordered a {pizza['crust'].title()}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print (f"\t\t\t{topping}")

print ("\tDictionary in a Dictionary")
coders = {
    'Lead' : {
        'first' : 'shreyans',
        'last' : 'jain',
        'designation' : 'full stack web engineer',
    },
    'Member 1' : {
        'first' : 'suraj',
        'last' : 'singh',
        'designation' : 'cyber security engineer',
    },
    'Member 2' : {
        'first' : 'shivam',
        'last' : 'singh',
        'designation' : 'back end develoer',
    },
    'Member 3' : {
        'first' : 'Faique',
        'last' : 'Yusuf',
        'designation' : 'front end developer',
    },
}

for member,member_info in coders.items():
    print (f"\t\t{member}")
    full_name=f"{member_info['first']} {member_info['last']}"
    print (f"\t\t\t{full_name.title()}\n\t\t\t{member_info['designation'].title()} ")
