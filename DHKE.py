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

q = int(input("Enter the prime Number(q) :"))
pRoot(q)
print()
afa = int(input("Choose the value for Alfa :"))
print("<-------------------------------- Public and Private Key Pairs-------------------------------------->")
xa = int(input("Select Private key for User A such that X(A)<q :"))
ya = (afa**xa)%q
print("Private and Public Key Pair for User A :(",xa,",",ya,")")
print()

xb = int(input("Select Private key for User B such that X(B)<q :"))
yb = (afa**xb)%q
print("Private and Public Key Pair for User B :(",xb,",",yb,")")
print()

ska = (yb**xa)%q
skb = (ya**xb)%q

print("Secret Key A & B :",ska,skb)






