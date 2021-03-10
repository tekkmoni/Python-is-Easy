#Homework #6 Advanced Loops

def board(rows, columns):
    rows = int(rows)
    columns = int(columns)
    columns = 3
    rows = 21
    if columns < 3 or rows > 21:
        return False
    
    else: 
        for row in range(rows):
            if row % 2 == 0:
                for col in range(1,columns):
                    if col % 2 == 1:
                        if col != columns -1:
                            print (" ", end="")
                    else:
                        print("|", end="")
            else: 
                print("-" * columns)
                
        	return True   