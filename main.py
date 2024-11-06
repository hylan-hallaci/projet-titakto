

c1=" "                                              #chaques cases à une variable 
c2=" "
c3=" "
c4=" "
c5=" "
c6=" "
c7=" "
c8=" "
c9=" "

def turn_o():                                           #change la variable d'une case par la valeur 1 pour les O et a valeur 2 pour les X.
    global c1, c2, c3, c4, c5, c6, c7, c8, c9
    CA=int(input("quelle case voulez vous jouer ?"))
    if CA == 1 and c1 ==" ":
        c1= "O"
    elif CA == 2 and c2==" ":
        c2= "O"
    elif CA== 3 and c3 == " ":
        c3= "O"
    elif CA== 4 and c4 ==" ":
        c4= "O"
    elif CA==5 and c5==" ":
        c5= "O"
    elif CA==6 and c6==" ":
        c6= "O"
    elif CA==7 and c7==" ":
        c7= "O"
    elif CA==8 and c8==" ":
        c8="O"
    elif CA==9 and c9==" ":
        c9="O"
    else:
        print("choisissez une case vide svp")
        turn_o()
        
        
        
def turn_x():                                             #pour eviter des erreurs, répétition, KISS
    global c1, c2, c3, c4, c5, c6, c7, c8, c9
    CA=int(input("quelle case voulez vous jouer ?"))
    if CA == 1 and c1 ==" ":
        c1= "X"
    elif CA == 2 and c2==" ":
        c2= "X"
    elif CA== 3 and c3 == " ":
        c3="X"
    elif CA== 4 and c4 ==" ":
        c4="X"
    elif CA==5 and c5==" ":
        c5="X"
    elif CA==6 and c6==" ":
        c6="X"
    elif CA==7 and c7==" ":
        c7="X"
    elif CA==8 and c8==" ":
        c8="X"
    elif CA==9 and c9==" ":
        c9="X"
    else:
        print("choisissez une case vide svp")
        turn_x()
 
 
def case():                                               #grille avec support des variables dans le terminal
    global c1, c2, c3, c4, c5, c6, c7, c8, c9
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
        

def victory():                                      #Cnditions de victoire 
    global c1, c2, c3, c4, c5, c6, c7, c8, c9
    
    if (c1 == "O" and c2 == "O" and c3 == "O") or (c1 == "X" and c2 == "X" and c3 == "X"):
        print("Victoire GG")
        return False
    elif (c4 == "O" and c5 == "O" and c6 == "O") or (c4 == "X" and c5 == "X" and c6 == "X"):
        print("Victoire GG")
        return False
    elif (c7 == "O" and c8 == "O" and c9 == "O") or (c7 == "X" and c8 == "X" and c9 == "X"):
        print("Victoire GG")
        return False
    
    elif (c1 == "O" and c4 == "O" and c7 == "O") or (c1 == "X" and c4 == "X" and c7 == "X"):
        print("Victoire GG")
        return False
    elif (c2 == "O" and c5 == "O" and c8 == "O") or (c2 == "X" and c5 == "X" and c8 == "X"):
        print("Victoire GG")
        return False
    elif (c3 == "O" and c6 == "O" and c9 == "O") or (c3 == "X" and c6 == "X" and c9 == "X"):
        print("Victoire GG")
        return False
    
    elif (c1 == "O" and c5 == "O" and c9 == "O") or (c1 == "X" and c5 == "X" and c9 == "X"):
        print("Victoire GG")
        return False
    elif (c3 == "O" and c5 == "O" and c7 == "O") or (c3 == "X" and c5 == "X" and c7 == "X"):
        print("Victoire GG")
        return False

    elif c1 != " " and c2 != " " and c3 != " " and c4 != " " and c5 != " " and c6 != " " and c7 != " " and c8 != " " and c9 != " ":
        print("fin de partie, égalité")
        return False
    else:
        print("manche suivante")
        return True

def flow():                                     #avancement
    while victory() is True:
        
        print("Au tour du joueur O")
        victory()
        case()
        victory()
        turn_o()
        victory()       
        print("Au tour du joueur X") 
        case()
        victory()
        turn_x()
        victory()
        
        





def play():                                            #Le menu principal du jeu
    player=int(input("Solo ou deux joueurs"))
    if player==1:
        flow()        
    elif player==2:
        flow()
    else:
        print("1 ou 2 joueurs svp")
        play()
play()




        
        
    