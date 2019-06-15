import math

def pRoot(q):
	ctain = [None]*(q-1)
#we only find minimum primitve root after that we work co-prime to decrease time complexity
	
	for i in range(2,q):
		ch = 0
		for j in range(1,q):
			ctain[j-1] = (i**j)%q
			
		#print(ctain)
		for j in range(1,q):
			if(j in ctain):
				ch = ch + 1
				
		#print(ch,"",q-1)
		if(ch == q-1):
			print("1 Smallest Primitve Root for",q,"is :",i)
			break;
	print()		
	print("Findind Other Primitve Root via Relative Prime Number to ",q-1)
	j = 1
	for k in range(i+1,q):
		ch = math.gcd(k,q-1)
		if(ch == 1):
			j += 1
			print(j,"Primitve Root for",q,"is :",(i**k)%q)
	
	return

def inverseCal(K,q):
	for i in range(0,q):
		if((K*i)%q == 1):
			print("Possible inverse for K can be :",i)
	return

print("<---------------------------------------- Note Note Note ------------------------------------------------------>")
print("Note : This Program is made for Elgamal Algo to Encypt and Decrypt Message formed by Alphabet, So Please Kindly ")	
print("do use a prime number greater than 127 because that the last ascii value in Decimal Ascii Table.")	
print("<---------------------------------------- Note Note Note ------------------------------------------------------>")
print()
q = int(input("Enter the prime Number(q) :"))
pRoot(q)
print()
afa = int(input("Choose the value for Alfa :"))
print("<-------------------------------- Public and Private Key Pairs-------------------------------------->")

xa = int(input("Enter the value for Private key X(A) < "+ str(q-1) + " :"))
ya = (afa**xa)%q
print("Private and Public {q,alfa,Y(A)} key Pairs are :(",xa,",(",q,",",afa,",",ya,")")

m = list(input("Enter the PlainText :"))
k = int(input("Enter the Random integer k < "+ str(q-1) + " :"))
K = (ya**k)%q
c1 = (afa**K)%q

print("<-------------------------------- Calculation Done - Encrypting Text -------------------------------------->")
ctain = [None]*len(m)
for i in range(0,len(m)):
	#print(m[i],ord(m[i]),K)
	ctain[i] = (K*ord(m[i]))%q
print("<-------------------------------------------- Encryption Done --------------------------------------------->")

print("Cipher Key (C1,C2) :",c1,ctain)
inverseCal(K,q)
Ki = int(input("Choose a value for Inverse :"))

dc = [None]*len(m)
print("<-------------------------------- Calculation Done - Decrypting Text -------------------------------------->")
for i in range(0,len(m)):
	#print(ctain[i],Ki)
	dc[i] = chr((ctain[i]*Ki)%q)
print("<-------------------------------------------- Decryption Done --------------------------------------------->")

dc = "".join(dc);
print("Plain Text : ",dc)
