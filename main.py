grille =  ["_","_","_","_","_","_","_","_","_"]
    
def displaygame(grille):
    print(grille[0], '|',grille[1],'|',grille[2])
    print("__"+"__"+"__"+"__"+"__")
    print(grille[3], '|',grille[4],'|',grille[5])
    print("__"+"__"+"__"+"__"+"__")
    print(grille[5], '|',grille[6],'|',grille[7])
    print("___"+"__"+"__"+"__"+"__")
displaygame(grille)

def jouer(joueur,grille):
    print("Le joueur")





player1=turn_x
player2=turn_o
def play(player1,player2):
    tour1=turn_x()
    tour2=turn_o()
    while victory() : False
    turn_x()
    turn_o()

print(play())






















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