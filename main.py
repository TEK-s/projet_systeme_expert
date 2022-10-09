from mansion import *
from agent import *
text = "" 
i=2
while (text == ""):
    i=i+1
    grid=[["_" for j in range(i)] for k in range(i)]
    #print(grid)
    n=i
    grid[0][0]="R"
    if i==3:
        
        grid=generation_feu_chaleur(n,grid)
        grid=generation_decombre_poussiere(n,grid)
        grid=generation_personne(n,grid)
       
        
    if i>3:
        #grid=generation_personne(n,grid)
        options=[e for e in range(1,n-1)]
        position=random.choices(options,k=1)
        for e in range(0,position[0]) :
            generation_feu_chaleur(n,grid)
        options.remove(position[0])
        #generation_personne(n)
        position=random.choices(options,k=1)
        for e in range(0,position[0]) :
            generation_decombre_poussiere(n,grid)  
    #generation_personne(n) 
        generation_personne(n,grid) 
    
    #for k in range(i):
    #    for j in range(i):
    #        print(grid[k][j]," ", end="")
    #
    # print('\n')
        
    alternatives={}
    grid_parcouru=[['x' for i in range(n)] for j in range(n)]
    x=0
    y=0
    value='R'
    for k in range(n):
        for j in range(n):
            print(grid[k][j]," ", end="")
        print('\n')
    grid
    while value !='G' and value !='D' and x!=-1 and y!=-1:
        alternatives=capteur (y,x,n,alternatives,grid, grid_parcouru)
        y,x,value=inference(y,x,alternatives,n,grid, grid_parcouru)
    text = input("si vous souhaitez continuer appuyez entrer sinon appuyer sur une touche quelconque") 
    