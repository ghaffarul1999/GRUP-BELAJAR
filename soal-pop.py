# soal: remove/hapus semua bilangan genap pada list

# input --> [10,5,6,6]

# output --> [5]

# SOLUSI 1: ---------------------------------------------------------------------------------------------------------------------

def removeEvenNum(data): 
    i=0

    for x in data:
        if x%2 == 0:
            
            data.pop(i)
            getOddNum( data )
            
        else:
            i+=1

    return data

x = removeEvenNum( [10,5,6,6] )

print(x)


# SOLUSI 2: (menggunakan flag True dan False) --------------------------------------------------------------------------------------------

def removeEvenNum(data):
    i=0
    stat = False

    for x in data:
        if x%2 == 0:
            stat = True
            break
            
        else:
            i+=1

    if stat == True:
        data.pop(i)
        removeEvenNum( data )

    return data

x = removeEvenNum([10,5,6,6])

print( x )


