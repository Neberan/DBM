from tkinter import *
import dbm

db = dbm.open('dbm', 'c')

    #Bouton ajouter
def on_button():
    ajouter(enter1.get())

    #Efface le champ entré
def reset(event):
    enter1.delete(0, 50)


def ajouter(nom):
    db[nom] = 'ITS'
    listbox1.insert(END, nom)

    #Bouton Supprimer
def on_button1():

    nom = enter1.get()
    del db[nom]
    listbox1.delete(index)

def get_list(event):

    global index
    index = listbox1.curselection()[0]
    seltext = listbox1.get(index)
        # Supprimer l'ancienne entré
    enter1.delete(0, 50)
        # Réafficher
    enter1.insert(0, seltext)


root = Tk()
    # Listbox
listbox1 = Listbox(root, width=80, height=6)
listbox1.grid(row=0, column=0)
    # Scrollbar
yscroll = Scrollbar(command=listbox1.yview, orient=VERTICAL)
yscroll.grid(row=0, column=1, sticky=N+S)
listbox1.configure(yscrollcommand=yscroll.set)
    # Créer les boutons et entré
enter1 = Entry(root, width=50, bg='red', fg='white')
enter1.insert(0, 'Cliquer pour choisir')
enter1.grid(row=1, column=0)
button1 = Button(root, text="Ajouter", command=on_button)
button1.grid(row=0, column=2)
button2 = Button(root, text="Supprimer", command=on_button1)
button2.grid(row=1, column=2)

    # Charger la listbox avec la database
for key in db.keys():
    for item in [key]:
        listbox1.insert(END, item)
    # Cliquer pour afficher
listbox1.bind('<ButtonRelease-1>', get_list)
    #Cliquer pour effacer la barre
enter1.bind('<Button-1>', reset)
root.mainloop()
