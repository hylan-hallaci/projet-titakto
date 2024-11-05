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