# A-Z = 65-90
# a-z = 97-122 Rd Sfrj NX Uwfrti

s = input("Enter CipherText : ")
print("------------ For Caeser Cipher key is 3 ------------")
ch = int(input("------------ IF YOU KNOWN THE KEY PRESS 1 OR ELSE PRESS 0 :  "))

def decrypt (k, l):
	for i in range(len(l)):
		u = ord(l[i])	
		
		if( u >= 97 and u <= 122 ):
			u = u - k
			if(u < 97):
				#print(u)
				d = 97 - u 
				u = 122 - (d - 1 )  				#d-1 is because when we move to 122 for k=1, 1 is already added by 
				#print(u)							# continuing to 97
		
		elif( u >= 65 and u <= 90):
			u = u - k
			#print(u)
			if(u < 65):	
				d = 65 - u
				u = 90 - ( d - 1 )
		
		l[i] = chr(u)
		
	l = ''.join(l)
	print("Plain Text for k = " + str(k) + " is : " + l)
	return

if(ch == 1):
	k = int(input("Enter the value of key :  "))
	decrypt(k, list(s))
	
	
else:
	for k in range(1,27):
		#l = list(s)
		decrypt(k, list(s))

		
print('\n' + '\u00a9 ' + '\u00a9 ' + '\u00a9 ' + '\u00a9 ' + '\u00a9 ' + '\u00a9 ' + '\u00a9 ' + '\u00a9 ' + '\u00a9 ' + '\u00a9 ' + '\u00a9 ')