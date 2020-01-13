print ("Operators\n")
universe_age=14_000_000_00 #underscore is used to group digits and not displayed
print (f"universe_age = {universe_age}\n")
x,y,z=1,2,3
print ("\tMultiple Assignment Operators\n\tx,y,z=1,2,3")
print ("\t\tx = ",x)
print ("\t\ty = ",y)
print ("\t\tz = ",z)

print ("\tEnter the two numbers")
x=int(input("\t"))
y=int(input("\t"))
print ("\tYou entered ",x,y)

print ("\n\tArithmatic Operators")
print ("\t\t x + y = ",x+y)
print ("\t\t x - y = ",x-y)
print ("\t\t x * y = ",x*y)
print ("\t\t x / y = ",x/y)
print ("\t\t x // y = ",x//y)
print ("\t\t x % y = ",x%y)
print ("\t\t x ** y = ",x**y)

print ("\n\tAssignment Operators")
a,b=13,17
print ("\t\t a = ",a)
print ("\t\t b = ",b)
a+=7
print ("\t\t a+= ",a)
b-=7
print ("\t\t a-= ",b)
a*=b
print ("\t\t a*=b ",a)
b/=a
print ("\t\t b/=a ",b)

print()
print ("\tComparison Operators")
print ("\t a>b = ",a>b)
print ("\t a<b = ",a<b)
print ("\t a>=b = ",a>=b)
print ("\t a<=b = ",a<=b)
print ("\t a==b = ",a==b)

print()
print ("\tLogical Operators")
i,j=0,1
print ("\t\t i = ",i)
print ("\t\t j = ",j)
print ("\t\t\tBoolean")
print ("\t\t\t i =",i,bool(i))
print ("\t\t\t i =",j,bool(j))
print ("\t\t i and j = ",i and j)
print ("\t\t i or j = ",i or j)
print ("\t\t not i = ",not i )
print("\t\t not j = ",not j )


print()
print ("\tBitwise Operators")
m,n=10,4 #a=10=1010 #b=4=0100
print ("\t\t m = ",m)
print ("\t\t n = ",n)
print ("\t\t\tBitwise")
print ("\t\t\t m =",m,"= 1010")
print ("\t\t\t n =",n,"= 0100")
print ("\t\t m & n = ",m & n)
print ("\t\t m | n = ",m | n)
print ("\t\t ~m = ",~m )
print ("\t\t ~n = ",~n )

print()
print ("\tMembership Operators")
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
print ("\t\tlist1 = ",list1)
print ("\t\tlist2 = ",list2)
print ("\t\t5 in list1 = ",5 in list1)
print ("\t\t10 not in list2 = ",10 not in list2)

print()
print ("\tIdentity Operators")
print ("\t\ttype(13) is int = ",type(13) is int)
print ("\t\ttype('17') is int = ",type('17') is int)
print ("\t\ttype(13) is not int = ",type(13) is not int)
print ("\t\ttype('17') is not int = ",type('17') is not int)

print()
print ("\tSpecial assignment operator")
print ("\t\tused to assign value in between different epressions")
print (f"\t\tlist1 = {list1}")
if (n:=len(list1)) > 0:
	print(f"\tWalrus operater used {n}")

if n:=len(list1) > 3:
	print(f"\tWalrus operater used {n}")
	
