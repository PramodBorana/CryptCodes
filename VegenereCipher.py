# A-Z = 65-90
# a-z = 97-122 Rd Sfrj NX Uwfrti
#SIWECYIPSUQRTTQV

ab = [0] * 26
a  = [[0] * 26 for i in range(26)]
for i in range(len(ab)):
	ab[i] = chr(65 + i)
#print(ab);

for i in range(len(a)):
	id = 65 + i 								#to increase the first character as much as row
	#print(id)
	for j in range(len(a[i])):
		if id > 90 :
			id = 65
		a[i][j] = chr(id)
		id = id + 1

#for row in a:
#    print(' '.join([str(elem) for elem in row]))
		
		

pt = input("Enter the PlainText : ")
pt = pt.upper()
ct = input("Enter the key : ")
ct = ct.upper()
ci = list(pt)

ptl = list(pt)
ctl = list(ct)

#print(a[25][25])

#key can be smaller then the plain text so once it completed we have to start it from ctl[0]
j = 0
print(len(ctl))
for i in range(len(ptl)):
	if j > (len(ctl) - 1):					#if j has reached the last index of key 0 to n-1
		j = 0
		print(ctl[j])
	
	ci[i] = a[ ord(ptl[i]) - 65 ] [ord(ctl[j]) - 65]
	j += 1
	
ci = ''.join(ci)
print("Cipher Text : " + ci)

