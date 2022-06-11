listnomor = [1,3,6,8,11]
listgenap=[]
listganjil=[]


for bilangan in range(len(listnomor)):  
	if(listnomor[bilangan]%2==0):
		listgenap.append(listnomor[bilangan])
		
	else:
		listganjil.append(listnomor[bilangan])

	
print("bilangan ganjil dalam list ada 3 buah, yaitu", listganjil[0],",",listganjil[1],",",listganjil[2])
print("bilangan ganjil dalam list ada 3 buah, yaitu", listganjil[0],",",listganjil[1], "dan" ,listganjil[2])
		