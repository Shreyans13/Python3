print ("\tWhile Loops")
i = 0
while i < 5:
    print(f"\t{i}")
    i += 1

print ("\tExiting a loop")
unconfirmed_users = []
confirmed_users = []
print (f"\tConfirmed Users = {confirmed_users}")
print ("\tEnter the users press QUIT to exit")
#user controlled exit
user = ""
while user.lower() != 'quit':
    user = input("\t")
    if user.lower() != 'quit':
        unconfirmed_users.append(user)
print (f"\tUnconfirmed users = {unconfirmed_users}")
while unconfirmed_users:
    user = unconfirmed_users.pop()
    print(f"\tVerifying users {user}")
    confirmed_users.append(user.title())
print (f"\tConfirmed Users = {confirmed_users}")

print ("\tEnter the user to be removed")
illegal_user = input("\t").title()
while illegal_user in confirmed_users:
    confirmed_users.remove(illegal_user)

print (f"\tConfirmed Users = {confirmed_users}")
shreyanssh
print ("\tFilling a Dictionary with user input")
database = {}

poll = True

while poll:
    print ("\tPolling")
    name = input("\tEnter your name ").title()
    uid = input("\tEnter your uid ").upper()
    database[uid] = name
    entries = input("\tAny more entries (Y/N) ")
    if entries.upper() == 'N':
        poll = False
print ("\tDatabase complete")
print (f"\t{database}")
