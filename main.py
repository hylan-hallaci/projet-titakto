c1="X"                                               #chaques cases à une variable 
c2="X"
c3="X"
c4=0
c5=0
c6=0
c7=0
c8=0
c9=0

def flow():
    while True:  
        case()   
        turn_o() 
        if victory(): 
            break
        case()   
        turn_x() 
        if victory():  
            break
flow()

def play():                                            #Le menu principal du jeu
    player=input("Solo ou deux joueurs")
    if player==1:
        flow()
    if player==2:
        flow()
    else:
        print("1 ou 2 joueurs svp")
        play()












def turn_o():                                           #change la variable d'une case par la valeur 1 pour les O et a valeur 2 pour les X.
    CA=input("quelle case voulez vous jouer ?")
    if CA == 1 and c1 ==0:
        c1= "O"
    elif CA == 2 and c2==0:
        c2= "O"
    elif CA== 3 and c3 == 0:
        c3= "O"
    elif CA== 4 and c4 ==0:
        c4= "O"
    elif CA==5 and c5==0:
        c5= "O"
    elif CA==6 and c6==0:
        c6= "O"
    elif CA==7 and c7==0:
        c7= "O"
    elif CA==8 and c8==0:
        c8="O"
    elif CA==9 and c9==0:
        c9="O"
    else:
        print("choisissez une case vide svp")
        turn_o()
def turn_x():                                             #pour eviter des erreurs, répétition, KISS
    CA=input("quelle case voulez vous jouer ?")
    if CA == 1 and c1 ==0:
        c1= "X"
    elif CA == 2 and c2==0:
        c2= "X"
    elif CA== 3 and c3 == 0:
        c3="X"
    elif CA== 4 and c4 ==0:
        c4="X"
    elif CA==5 and c5==0:
        c5="X"
    elif CA==6 and c6==0:
        c6="X"
    elif CA==7 and c7==0:
        c7="X"
    elif CA==8 and c8==0:
        c8="X"
    elif CA==9 and c9==0:
        c9="X"
    else:
        print("choisissez une case vide svp")
        turn_x()
 
def case():                                               #grille avec support des variables dans le terminal
    long = 1
    larg = 1
    n=0
    grille = [c1,c2,c3,c4,c5,c6,c7,c8,c9]

    print("+" + ("-" * long + "+") * 4)

    for i in range(3):
        
        for k in range(3):
            print(( f"|{grille[n]}|"),end='')
            n+=1
        print (end="\n") 

    print("+" + ("-" * long + "+")*4)
        
case()









































def victory():                                           #Victory c'est toutes les possibilités de victoires plus l'égalité
    if c1=="O" and c2=="O" and c3=="O" or c1=="X" and c2=="X" and c3=="X":
        return True     
    elif c4=="O" and c5=="O" and c6=="O" or c4=="X" and c5=="X" and c6=="X":
        return True
    elif c7=="O" and c8=="O" and c9=="O" or c7=="X" and c8=="X" and c9=="X":
        return True
    elif c1=="O" and c4=="O" and c7=="O" or c1=="X" and c4=="X" and c7=="X":
        return True
    elif c2=="O" and c5=="O" and c8=="O" or c2=="X" and c5=="X" and c8=="X":
        return True
    elif c3=="O" and c6=="O" and c9=="O" or c3=="X" and c6=="X" and c9=="X":
        return True
    elif c1=="O" and c5=="O" and c9=="O" or c1=="X" and c5=="X" and c9=="X":
        return True
    elif c3=="O" and c5=="O" and c7=="O" or c3=="X" and c5=="X" and c7=="X":
        return True
    elif c1 != 0 and c2 !=0 and c3 !=0 and c4 !=0 and c5 !=0 and c6 !=0 and c7 !=0 and c8 !=0 and c9 !=0:
        print("fin de partie, égalité")
        return True
    else:
        print("manche suivante")
        return False
    


#def game(player1 = turn_x(),player2=turn_o()):
#    while victory(False):
#        player1
#        case()
#        player1
#        case()
#print(game())


        
        






























#grille =  ["_","_","_","_","_","_","_","_","_"]
    
#def displaygame(grille):
#    print(grille[0], '|',grille[1],'|',grille[2])
#    print("__"+"__"+"__"+"__"+"__")
#    print(grille[3], '|',grille[4],'|',grille[5])
#    print("__"+"__"+"__"+"__"+"__")
#    print(grille[5], '|',grille[6],'|',grille[7])
#    print("___"+"__"+"__"+"__"+"__")
#displaygame(grille)

#def jouer(joueur,grille):
#    print("Le joueur")



























import tkinter

root = tkinter.Tk()



def draw_grid():
    button = tkinter.Button(root,height=5,width=20)
    button.place(x=100,y=200)
    button = tkinter.Button(root,height=5,width=20)
    button.place(x=300,y=200)
    button = tkinter.Button(root,height=5,width=20)
    button.place(x=500,y=200)
    button = tkinter.Button(root,height=5,width=20)
    button.place(x=100,y=400)
    button = tkinter.Button(root,height=5,width=20)
    button.place(x=300,y=400)
    button = tkinter.Button(root,height=5,width=20)
    button.place(x=500,y=400)
    button = tkinter.Button(root,height=5,width=20)
    button.place(x=100,y=600)
    button = tkinter.Button(root,height=5,width=20)
    button.place(x=300,y=600)
    button = tkinter.Button(root,height=5,width=20)
    button.place(x=500,y=600)
    

root.title("tictac")
root.minsize(700,700)
draw_grid()
root.mainloop()