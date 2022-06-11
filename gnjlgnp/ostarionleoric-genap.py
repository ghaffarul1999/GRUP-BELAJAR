listnomor = [1,3,6,8,11]
listgenap=[]
dan = "dan"

for bilangan in range(len(listnomor)):  
	if(listnomor[bilangan]%2==0):
		listgenap.append(listnomor[bilangan])        
        	
print("bilangan genap dalam list ada 2 buah, yaitu", *listgenap, sep=',') 
print("bilangan genap dalam list ada 2 buah, yaitu", listgenap[0],"dan",listgenap[1])
