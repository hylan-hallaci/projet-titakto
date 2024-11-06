import tkinter
#detection des bouttons
def symbole(r,c):
    print("click",r,c)

    clicked_buttons = buttons[c][r]
    clicked_buttons.config(text="X")
    

#grille
def grille():
    for column in range(3):
        buttons_in_cols=[]
        for row in range (3):
            button=tkinter.Button(root,font=("arial",50),
                                  width=5, 
                                  command = lambda r = row, c=column :symbole(r,c))
            
            button.grid(row=row , column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)

#stockage
buttons= []



#fenetre 
root = tkinter.Tk()
#personnalisation 
root.title("jeu trop bien")
root.minsize(500,393)

grille()
root.mainloop()


#fonction qui permet de switch entre les joueur 

play()
while True:  
    case()   
    turn_o() 
    if victory(): 
        break
    case()   
    turn_x() 
    if victory():  
        break
