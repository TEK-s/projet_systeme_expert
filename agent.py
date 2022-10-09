import random
"""def capteur(grid,x,y,n):
    grid_parcouru=[[]]
    direction={}
    for i in {[y-1,x],[y+1,x],[y,x+1],[y,x-1]}:
        if grid[i[0]][i[1]]=="_" and grid[i[0]][i[1]] not in grid_parcouru :
            y=i[0]
            x=i[1]
            action="robot ava"
            return(x,y,action)
        elif grid[i[0]][i[1]]=="F" and grid[i[0]][i[1]] not in grid_parcouru :
            y=i[0]
            x=i[1]
            action="robot eteind le feu"
            return(x,y,action)
        elif grid[i[0]][i[1]]=="D" and grid[i[0]][i[1]] not in grid_parcouru :
            y=i[0]
            x=i[1]
            action="robot coincé"
            return(x,y,action)
        elif grid[i[0]][i[1]]=="P" and grid[i[0]][i[1]] not in grid_parcouru :
            y=i[0]
            x=i[1]
            action="robot coincé"
            return(x,y,action)
        elif grid[i[0]][i[1]]=="P" and grid[i[0]][i[1]] not in grid_parcouru :
            y=i[0]
            x=i[1]
            action="robot coincé"
            return(x,y,action)
    
    grid_parcouru[y][x]=grid[y][x]
    grid_parcouru[y+1][x]=grid[y+1][x]
    grid_parcouru[y][x+1]=grid[y][x+1]
    grid_parcouru[y-1][x]=grid[y-1][x]
    grid_parcouru[y][x-1]=grid[y][x-1]
    
    
grid=[['R','P','_'],['P','F','P'],['_','P','_']]"""

def capteur (y,x,n,alternatives,grid, grid_parcouru):
    
    if y+1<n and grid[y+1][x] != grid_parcouru[y+1][x]:
      grid_parcouru[y+1][x]=grid[y+1][x]
      alternatives["S"]=grid[y+1][x]
    else:
        alternatives["S"]=""
    if y-1>-1 and grid[y-1][x] != grid_parcouru[y-1][x]:
        grid_parcouru[y-1][x]=grid[y-1][x]
        alternatives["N"]=grid[y-1][x]
    else:
        alternatives["N"]=""
    if x+1<n and grid[y][x+1] != grid_parcouru[y][x+1]:
        grid_parcouru[y][x+1]=grid[y][x+1]
        alternatives["E"]=grid[y][x+1]
    else:
        alternatives["E"]=""
    if x-1 >-1 and grid[y][x-1] != grid_parcouru[y][x-1]:
       grid_parcouru[y][x-1]=grid[y][x-1]
       alternatives["O"]=grid[y][x-1]
    else:
        alternatives["O"]=""
    grid_parcouru[y][x]=grid[y][x]
    return alternatives


def return_direction(alternatives,value):
    return_direction = [k for k, v in alternatives.items() if v == value]
    return return_direction

def Action (direction,y,x,n):
    if direction=='S':
        y+=1
        if y>=n :
            y-=1
        action="le robot descend"
        #print(' x :' ,x,' y :', y,' direction :',direction )
        return y,x,action
    if direction=='N':
        y-=1
        if y<=-1:
            y+=1
        action="le robot monte"
        #print(' x :' ,x,' y :', y,' direction :',direction )
        return y,x,action
    if direction=='E':
        x+=1
        if x>=n:
            x-=1
        action="le robot va à droite"
        #print(' x :' ,x,' y :', y,' direction :',direction )
        return y,x,action
    if direction=='O':
        x-=1
        if x<=-1:
            x+=1
        action="le robot va à gauche"
        #print(' x :' ,x,' y :', y,' direction :',direction )
        return y,x,action
    
    
                
def inference(y,x,alternatives,n,grid, grid_parcouru):
    if 'G' in alternatives.values():
        value='G'
        direction=return_direction(alternatives,value)
        y,x,action=Action(direction[0],y,x,n)
        print(action)
        print("la personne est sauvée")
        return y,x,value
    elif '_' in alternatives.values():
        value='_'
        direction=return_direction(alternatives,value)
        direction=random.choices(direction,k=1)
        y,x,action=Action(direction[0],y,x,n)
        print(action)
        return y,x,value
    elif 'P' in alternatives.values() and 'C' in alternatives.values():
        value=random.choices(['P','C'],weights=[1,1],k=1)
        direction=return_direction(alternatives,value[0])
        direction=random.choices(direction,weights=[1 for i in range(len(direction))],k=1)
        y,x,action=Action(direction[0],y,x,n)   
        print(action)
        return y,x,value[0]
    elif 'C' in alternatives.values() and 'PC' in alternatives.values():
        value=random.choices(['C','PC'],weights=[1,1],k=1)
        direction=return_direction(alternatives,value[0])
        direction=random.choices(direction,weights=[1 for i in range(len(direction))],k=1)
        y,x,action=Action(direction[0],y,x,n)   
        print(action)
        return y,x,value[0]
    elif 'P' in alternatives.values() and 'PC' in alternatives.values():
        value=random.choices(['P','PC'],weights=[1,1],k=1)
        direction=return_direction(alternatives,value[0])
        direction=random.choices(direction,weights=[1 for i in range(len(direction))],k=1)
        y,x,action=Action(direction[0],y,x,n)   
        print(action)
        return y,x,value[0]
    elif 'F' in alternatives.values() and 'D' in alternatives.values():
        value=random.choices(['F','D'],weights=[1,1],k=1)
        direction=return_direction(alternatives,value[0])
        direction=random.choices(direction,weights=[1 for i in range(len(direction))],k=1)
        y,x,action=Action(direction[0],y,x,n)
        if value[0]=='F':
            grid[y][x]='_'
            grid_parcouru[y][x]='_'
            print("le robot a éteind le feu")
            print(action)
            return y,x,value[0]
        if value[0]=='D':
            x=-1
            y=-1
            print("le robot est coincé dans les décombres")
            print(" la partie est terminée")
            print(x,y)
            return y,x,value[0]
    elif 'C' in alternatives.values():
        value='C'
        direction=return_direction(alternatives,value)
        direction=random.choices(direction,k=1)
        y,x,action=Action(direction[0],y,x,n)   
        print(action)
        return y,x,value
    elif 'P' in alternatives.values():
        value='P'
        direction=return_direction(alternatives,value)
        direction=random.choices(direction,k=1)
        y,x,action=Action(direction[0],y,x,n)  
        print(action) 
        return y,x,value
    elif 'PC' in alternatives.values():
        value='PC'
        direction=return_direction(alternatives,value)
        direction=random.choices(direction,k=1)
        y,x,action=Action(direction[0],y,x,n)  
        print(action) 
        return y,x,value
    elif 'F' in alternatives.values():
        value='F'
        direction=return_direction(alternatives,value)
        y,x,action=Action(direction[0],y,x,n)
        grid[y][x]='_'
        grid_parcouru[y][x]='_'
        print("le robot a éteind le feu")
        print(action)
        return y,x,value
    elif 'D' in alternatives.values():
        value='D'
        direction=return_direction(alternatives,value)
        y,x,action=Action(direction[0],y,x,n)
        x=-1
        y=-1
        print(action)
        print("le robot est coincé dans les décombres")
        print(" la partie est terminée")
        return y,x,value
    else:
        if y+1<n :
            alternatives["S"]=grid[y+1][x]
        else:
            alternatives["S"]=""
        if y-1>-1 :
            alternatives["N"]=grid_parcouru[y-1][x]
        else:
            alternatives["N"]=""
        if x+1<n :
            alternatives["E"]=grid_parcouru[y][x+1]
        else:
            alternatives["E"]=""
        if x-1 >-1:
            alternatives["O"]=grid_parcouru[y][x-1]
        else:
            alternatives["O"]=""
        a=[i for i in alternatives.values()]
        value=random.choices(a,weights=[1 for i in range(len(a))],k=1)
        direction=return_direction(alternatives,value[0])
        y,x,action=Action(direction[0],y,x,n)
        print(action)
        return y,x,value
        
"""n=4  
alternatives={}
grid_parcouru=[['x' for i in range(n)] for j in range(n)]
grid=[['R','_','_','P'],['_','P','P','D'],['P','D','P','PC'],['G','P','C','F']]
x=0
y=0
value='R'
for k in range(n):
    for j in range(n):
        print(grid[k][j]," ", end="")
    print('\n')
while value !='G' and value !='D' and x!=-1 and y!=-1:
    alternatives=capteur (y,x,n,alternatives,grid, grid_parcouru)
    y,x,value=inference(y,x,alternatives,n,grid, grid_parcouru)
    alternatives={}"""


    

    

#print("originale",grid)
#print("alternatives",alternatives.values('_'))
