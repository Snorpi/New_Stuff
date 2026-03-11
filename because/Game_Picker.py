import tkinter as tk
import random

Games = ['Destiny 2', 'Palworld', 'Content Warning', 'Phasmophobia', 'Minecraft', 'Forza']

def pickOne():
    random_game = random.choice(Games)
    chosen_game_label.config(text=random_game)

def addGame():
    new_game = game_entry.get()
    if new_game:
        Games.append(new_game)
        game_entry.delete(0, tk.END)

def yoinkGame():
    if Games:
        Games.pop()


root = tk.Tk()
root.title('Tristan Can\'t Pick A Game')

root.geometry('400x200')
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) // 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) // 2
root.geometry('+%d+%d' % (x,y))

label = tk.Label(root, text='Too indecisive? Click the button. It wants you to.')
label.pack()

chosen_game_label = tk.Label(root, text='')
chosen_game_label.pack()

game_entry = tk.Entry(root)
game_entry.pack()

add_button = tk.Button(root, text="Add A Game", command=addGame)
add_button.pack()

remove_button = tk.Button(root, text="Yoink A Game", command=yoinkGame)
remove_button.pack()

button = tk.Button(root, text='Click me!!!!!', command=pickOne)
button.pack()

root.mainloop()