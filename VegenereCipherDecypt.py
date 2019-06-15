# A-Z = 65-90
# a-z = 97-122 Rd Sfrj NX Uwfrti
#SIWECYIPSUQRTTQV
#Decryption is performed by going to the row in the table corresponding to the key, finding the position of the ciphertext letter in this row,
#and then using the column’s label as the plaintext.For example, in row A (from AYUSH), the ciphertext G appears in column G,which is the first
#plaintext letter.Next we go to row Y (from AYUSH), locate the ciphertext C which is found in column E, thus E is the second plaintext letter.

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
		
		

pt = input("Enter the CiphereText : ")
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
	
	for k in range(26):
		if a[0][k] == ctl[j]:				
			for l in range(26):
				if a[k][l] == ptl[i]:
					ci[i] = a[0][l]
	j += 1
	
ci = ''.join(ci)
print("Plain Text : " + ci)

