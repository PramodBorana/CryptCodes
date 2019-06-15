# A-Z = 65-90
# a-z = 97-122

s = input("Enter PlainText : ")
l = list(s)
print("------------ For Caeser Cipher key is 3 ------------")
k = int(input("Enter the value of key :  "))

for i in range(len(l)):
	u = ord(l[i])	
	
	if( u >= 97 and u <= 122 ):
		u = u + k
		if(u > 122):
			#print(u)
			d = u - 122
			u = 97 + (d - 1 )  				#d-1 is because when we move to 97 for k=1, 1 is already added by 
			#print(u)						# continuing to 97
	
	elif( u >= 65 and u <= 90):
		u = u + k
		#print(u)
		if(u > 90):	
			d = u - 90
			u = 65 + ( d - 1 )
	
	l[i] = chr(u)
	
l = ''.join(l)
print("Cipher Text :" + l)
	
	

