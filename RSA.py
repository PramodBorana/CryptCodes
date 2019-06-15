#c = m^e mod n
#m = c^d mod n

import math

p = int(input("Enter the First Prime number P : "))
q = int(input("Enter the First Prime number Q : "))

n = p*q
fin = (p-1) * (q-1)

print("<---------------------------- Possible values for e --------------------->")
print("GCD(fi(n) x) : gcd(fi(n),i)")
for i in range(1,fin):
	ch = math.gcd(fin,i)
	if(ch == 1):
		print("GCD(",fin,i,") :",ch)
	
print("<------------------------------------------------------------------------>")
e = int(input("Select Value of E :"))
print("<---------------------------- Possible values for d --------------------->")
for i in range(1,fin):
	ch = (i*e)%fin
	if(ch == 1):
		print("Possible value for d :",i)
print("<------------------------------------------------------------------------>")
d = int(input("Select Value of D :"))
print()
print("your public key pair  : e =",e,"n =",n)
print("your private key pair : d =",d,"n =",n)

print("<------------------------------------------------------------------------>")
sl = list(input("Enter your full name :"))
#print(sl)
cl =  ""
for i in sl:
	#print(i)
	c = (ord(i)**e)%n
	cl = cl + str(c) + " "
	
print("Cipher Text :",cl)
cl = list(map(int,cl.split()))
#print(cl)	

vl = ""
for i in cl:
	c  = (i**d)%n
	vl = vl + chr(c)

print("Message Text :",vl)


