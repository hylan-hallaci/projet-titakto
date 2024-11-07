grille=[" "," "," "," "," "," "," "," "," "]

def case():                                               #grille avec support des variables dans le terminal
 
    long = 1
    larg = 1
    n=0
    global grille

    print("+" + ("-" * long + "+") * 4)

    for i in range(3):
        
        for k in range(3):
            print(( f"|{grille[n]}|"),end='')
            n+=1
        print (end="\n") 

    print("+" + ("-" * long + "+")*4)
def turn(verif):
    if verif == True:
        symbol="X"
    else:
        symbol = "O" 
        
def victory(grille):
    if grille(1) !=" " and grille (2) !=" " and grille (3) !=" " and grille (4) !=" " and grille (5) !=" " and grille (6) !=" " and grille(7)!=" " and grille (8) !=" " and grille (9) !=" ":
        print("fin de partie, égalité")
        return
        

#Note de cours, qand on merge on fait Origin/Lucas, quand probleme résoudre en 

def turn(symbol):
    
    