c1=1
c2=2
c3=3
c4=4
c5=5
c6=6
c7=7
c8=8
c9=9

def turn_o():                                           #change la variable d'une case par la valeur 1 pour les O et a valeur 2 pour les X.
    CA=input("quelle case voulez vous jouer ?")
    if CA == 1 and c1 ==0:
        c1= 1
    elif CA == 2 and c2==0:
        c2= 1
    elif CA== 3 and c3 == 0:
        c3=1
    elif CA== 4 and c4 ==0:
        c4=1
    elif CA==5 and c5==0:
        c5=1
    elif CA==6 and c6==0:
        c6=1
    elif CA==7 and c7==0:
        c7=1
    elif CA==8 and c8==0:
        c8=1
    elif CA==9 and c9==0:
        c9=1
    else:
        print("choisissez une case vide svp")
        turn_o()
def turn_x():                                             #pour eviter des erreurs, répétition, KISS
    CA=input("quelle case voulez vous jouer ?")
    if CA == 1 and c1 ==0:
        c1= 2
    elif CA == 2 and c2==0:
        c2= 2
    elif CA== 3 and c3 == 0:
        c3=2
    elif CA== 4 and c4 ==0:
        c4=2
    elif CA==5 and c5==0:
        c5=2
    elif CA==6 and c6==0:
        c6=2
    elif CA==7 and c7==0:
        c7=2
    elif CA==8 and c8==0:
        c8=2
    elif CA==9 and c9==0:
        c9=2
    else:
        print("choisissez une case vide svp")
        turn_x()
 
def case():
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









































def victory():
    if c1==1 and c2==1 and c3==1:
        return 
    elif c4==1 and c5==1 and c6==1:
        return
    elif c7==1 and c8==1 and c9==1:
        return
    elif c1==1 and c4==1 and c7==1:
        return
    elif c2==1 and c5==1 and c8==1:
        return
    elif c3==1 and c6==1 and c9==1:
        return
    elif c1==1 and c5==1 and c9==1:
        return
    elif c3==1 and c5==1 and c7==1:
        return
    else:
        print("manche suivante")
        
    if c1==2 and c2==2 and c3==2:
        return 
    elif c4==2 and c5==2 and c6==2:
        return
    elif c7==2 and c8==2 and c9==2:
        return
    elif c1==2 and c4==2 and c7==2:
        return
    elif c2==2 and c5==2 and c8==2:
        return
    elif c3==2 and c6==2 and c9==2:
        return
    elif c1==2 and c5==2 and c9==2:
        return
    elif c3==2 and c5==2 and c7==2:
        return
    else:
        print("manche suivante")

    if c1 != 0 and c2 !=0 and c3 !=0 and c4 !=0 and c5 !=0 and c6 !=0 and c7 !=0 and c8 !=0 and c9 !=0:
        print("fin de partie, égalité")
        
    