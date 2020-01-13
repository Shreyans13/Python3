print("Dictionary")
print()
alien={
    'color' : 'green',
    'points' : 5,
    'speed' : 'fast'
    }
print (f"\talien before")
print (f"\talien = {alien}")
print (f"\talien['color'] = {alien['color']}")
print (f"\talien['points'] = {alien['points']}")

print()
alien['position'] = 0
print (f"\talien after adding new key value pair ")
print (f"\talien = {alien}")

print()
alien['color'] = 'yellow'
alien['points'] = 13
print (f"\talien after changing old values")
print (f"\talien = {alien}")
print()
print (f"\tOriginal position of alien = {alien['position']}")

if alien['speed'] == 'fast':
    inc=5
else:
    inc=1
alien['position'] += inc

print (f"\tNew Position = {alien['position']}")

print()
print (f"\talien before \n\talien  = {alien}")
print (f"\talien after deletings its position")
del alien['position']
print (f"\talien = {alien}")

print()
favourite_Languages = {
    'suraj' : 'python',
    'vijay' : 'c',
    'anshu' : 'c++',
}

print (f"\tSuraj's favourite language is {favourite_Languages['Suraj'.lower()].title()}")
print (f"\tSHreyans's favourite lanugage is {favourite_Languages.get('Shreyans','[No value named Shreyans]').title()}")

print()
print ("\tLooping through a Dictionary")
user = {
    'username' : 'KingMaker',
    'first' : 'Shreyans',
    'last' : 'Jain',
}
print (f"\t\tuser = {user}")
for key, value in user.items():
    print (f"\n\t\tKey : {key}\n\t\tValue : {value}")

print (f"\t\tfavourite_Languages = {favourite_Languages}")
for name,language in favourite_Languages.items():
    print (f"\t\t{name.title()} : {language.upper()}")
print()
print ("\tLooping through keys only")
for name in favourite_Languages.keys():
    print (f"\t\t{name}")

print ("\tLooping through keys in particular order")
for name in sorted(favourite_Languages.keys()):
    print (f"\t\t{name.title()}")

skills = {
    'Shreyans Jain' : 'full stack web developer',
    'Suraj Singh' : 'full stack web developer',
    'Shivam Singh' : 'UI/UX designer',
    'Faique Yusuf' : 'UI/UX designer',
    'Vijay Dhakar' : 'cyber security researcher',
    'Anshu Singh' : 'cyber security researcher',
}
print (f"\tskills = {skills}")
print ("\tLooping through values only")
for skill in skills.values():
    print (f"\t\t{skill}")
print ("\tLooping through values uniquely only")
for skill in sorted(set(skills.values())):
    print (f"\t\t{skill.upper()}")
