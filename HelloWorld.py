print("Hello python interpreter")

print()
a='I told you my friend, "Phython is my favourite language".'
print(a)
b="The language 'python' is named after Monty Python, not the snake."
print(b) 
c="One of Python's strengths is its diverse and supportive community."
print(c)

print()
print("DataTypes")
print("type(13)",type(13))
print("type('17')",type('17'))
print("type(13.17)",type(13.17))

print()
name="shreyans jain"
print ("name = ",name)
print ("name.title() = ",name.title())
print ("name.upper() = ",name.upper())
print ("name.lower() = ",name.lower())

first_name="shreyans"
last_name="jain"
full_name=f"{first_name} {last_name}" #This strings are called f-strings(format strings)
print ("full_name = ",full_name)

print (f"Hello, {full_name}!!!")

message=f"Hello, {full_name.title()}!!!"
print (message)

print()
print ("Languages:\n\tC\n\tC++\n\tJAVA\n\tPYTHON\n\tHTML5\n\tCSS\n\tJAVASCRIPT\n\tNODE.JS")
favourite_language="                PyThOn              "
print ("favourite_language = ",favourite_language)
print ("favourite_language.rstrip() = ",favourite_language.rstrip())
print ("favourite_language.lstrip() = ",favourite_language.lstrip())
print ("favourite_language.strip() = ",favourite_language.strip())

print ()
x,y,z=1,2,3
print ("Multiple Assignment\n\tx,y,z=1,2,3")
print ("\tx = ",x)
print ("\ty = ",y)
print ("\tz = ",z)

universe_age=14_000_000_00 #underscore is used to group digits and not displayed
print ("universe_age = ",universe_age)

print ()
print ("Operators")
print ("Enter the two numbers")
x=int(input())
y=int(input())
print ("You entered ",x,y)

print ("\nArithmatic Operators")
print ("\t x + y = ",x+y)
print ("\t x - y = ",x-y)
print ("\t x * y = ",x*y)
print ("\t x / y = ",x/y)
print ("\t x // y = ",x//y)
print ("\t x % y = ",x%y)
print ("\t x ** y = ",x**y)

print ("\nAssignment Operators")
a,b=13,17
print ("\t a = ",a)
print ("\t b = ",b)
a+=7
print ("\t a+= ",a)
b-=7
print ("\t a-= ",b)
a*=b
print ("\t a*=b ",a)
b/=a
print ("\t b/=a ",b)

print()
print ("Comparison Operators")
print ("\t a>b = ",a>b)
print ("\t a<b = ",a<b)
print ("\t a>=b = ",a>=b)
print ("\t a<=b = ",a<=b)
print ("\t a==b = ",a==b)

print()
print ("Logical Operators")
i,j=0,1
print ("\t i = ",i)
print ("\t j = ",j)
print ("\t\tBoolean")
print ("\t\t i =",i,bool(i))
print ("\t\t i =",j,bool(j))
print ("\t i and j = ",i and j)
print ("\t i or j = ",i or j)
print ("\t not i = ",not i )
print("\t not j = ",not j )


print()
print ("Bitwise Operators")
m,n=10,4 #a=10=1010 #b=4=0100
print ("\t m = ",m)
print ("\t n = ",n)
print ("\t\tBitwise")
print ("\t\t m =",m,"= 1010")
print ("\t\t n =",n,"= 0100")
print ("\t m & n = ",m & n)
print ("\t m | n = ",m | n)
print ("\t ~m = ",~m )
print ("\t ~n = ",~n )

print()
print ("Membership Operators")
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
print ("\tlist1 = ",list1)
print ("\tlist2 = ",list2)
print ("\t5 in list1 = ",5 in list1)
print ("\t10 not in list2 = ",10 not in list2)

print()
print ("Identity Operators")
print("\ttype(13) is int = ",type(13) is int)
print("\ttype('17') is int = ",type('17') is int)
print("\ttype(13) is not int = ",type(13) is not int)
print("\ttype('17') is not int = ",type('17') is not int)
