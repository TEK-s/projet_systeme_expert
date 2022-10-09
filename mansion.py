import random

#faits=["R","F","C","P","D","G"]
#for j in range (i):
 #   print("A "*i,"\n")
 
#while (text == ""):
#    text = input("si vous souhaitez continuer appuyez entrer") 
#    i+=1
#    for j in range (i):
#        print("A "*i,"\n")
        
#permet l'affichage de la grille
#def sudoku_grid(grid):
 #   for i in range(9):
 #       if (i%3==0 and i!=0):
 #           print("- "*15)
 #       for j in range(9):
 #           if(j%3==0 and j!=0):
 #               print("| ",end="")
 #               print(str(grid[i][j])," ", end="")
 #           else:
 #               print(str(grid[i][j])," ", end="")
 #       print('')
def generation_feu_chaleur(n,grid):
    x=random.randint(1,n-1)
    y=random.randint(1,n-1)
    grid[y][x]="F"
    if y+1<n and grid[y+1][x]!="F" and grid[y+1][x]!="G":
        grid[y+1][x]= "C"
    if y-1 > -1 and grid[y-1][x]!="F" and grid[y-1][x]!="G":
        grid[y-1][x]= "C"
    if x+1<n and  grid[y][x+1]!="F" and  grid[y][x+1]!="G":
        grid[y][x+1]= "C"
    if x-1 > -1 and grid[y][x-1]!="F" and grid[y][x-1]!="G":
        grid[y][x-1]= "C"
    return grid
    
     
def generation_personne(n,grid):
    grid_copy=[]
    for k in range(n):
        for j in range(n):
            if grid[k][j] in {"_"}:
                grid_copy.append([k,j])
    position=random.choices(grid_copy,k=1)
    y=position[0][0]
    x=position[0][1]
    grid[y][x]="G"
    return grid
    
def generation_decombre_poussiere(n,grid):
    grid_copy1=[]
    for k in range(n):
        for j in range(n):
            if grid[k][j] in {"_"}:
                grid_copy1.append([k,j])
    position=random.choices(grid_copy1,k=1)
    y=position[0][0]
    x=position[0][1]
    grid[y][x]="D"
    
    if y+1<n and grid[y+1][x]!="R":
        if grid[y+1][x]== "C":
            grid[y+1][x]= "PC"
        else :
            grid[y+1][x]= "P"
    if y-1 > -1 and grid[y-1][x]!="R":
        if grid[y-1][x]== "C":
            grid[y-1][x]= "PC"
        else :
            grid[y-1][x]= "P"
    if x+1<n and grid[y][x+1]!="R":
        if grid[y][x+1]== "C":
            grid[y][x+1]= "PC"
        else :
            grid[y][x+1]= "P"
    if x-1 > -1 and grid[y][x-1]!="R":
        if grid[y][x-1]== "C":
            grid[y][x-1]= "PC"
        else :
            grid[y][x-1]= "P"
    return grid
   

    
        
     
#grid=[["_" for j in range(i)] for k in range(i)]
#print(grid)
#n=i
#grid[0][0]="R"
#generation_feu_poussiere(n)
#for k in range(i):
#    for j in range(i):
#           print(grid[k][j]," ", end="")
#    print('\n')
        