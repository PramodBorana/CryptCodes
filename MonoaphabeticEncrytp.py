#key=ISYVKJRUXEDZQMCTPLOFNBWGAH
s = input("Enter Plain Text : ")
s = s.upper()
#print(s)
sl = list(s)
k = input("Enter the Cipher Key : ")
kl = list(k)
ab = {}           #is type of list with index as A,B,C,D which are mapped to I S Y V
ci = list(s)

spa = '$'
sp = input("Want to give some special character for space or It is $  Y/N : ")
if(sp == 'Y'):
 spa = input("Enter the special character for Spaces : ")

for i in range(0,26):
	ab[chr(65 + i)] = kl[i]
	#print( chr(97 + i) + " = " + ab[chr(97 + i)] )				#ab[A] = I, ab[B] = S like this
	
for i in range(len(sl)):
	if(sl[i] == ' '):
		ci[i] = spa
	else:	
		ci[i] = ab[sl[i]]
	

	
	
ci = ''.join(ci)
print("Cipher Text : " + ci )