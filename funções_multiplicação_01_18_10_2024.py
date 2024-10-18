

def multiplica(x, y, *resto):
    total = 0
    for i in resto:
        if(total == 0):
            total = total + i
        else:
            total = total * i
    
    print(total)
   
    
multiplica(1 ,2 ,3 ,4 ,5 ,6 ,50 ,10)

