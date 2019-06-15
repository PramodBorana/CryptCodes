#key=ISYVKJRUXEDZQMCTPLOFNBWGAH
# A-Z = 65-90
# a-z = 97-122
s = input("Enter Cipher Text : ")
s = s.upper()
#print(s)
sl = list(s)
k = input("Enter the Cipher Key : ")
kl = list(k)
ab = {}           #is type of list with index as A,B,C,D which are mapped to I S Y V
ci = list(s)

spa = '$'
sp = input("Do you have used special character for space other then $ then press Y else N : ")
if(sp == 'Y'):
 spa = input("Enter the special character for Spaces : ")

for i in range(0,26):
	ab[kl[i]] = chr(65 + i)
	#print( kl[i] + " = " + ab[kl[i]] )						#ab[I] = A, ab[S] = B like this reverse of Encrypt
	
for i in range(len(sl)):
	if(sl[i] == '$'):
		ci[i] = ' '
	else:	
		ci[i] = ab[sl[i]]
	

	
	
ci = ''.join(ci)
print("Cipher Text : " + ci )