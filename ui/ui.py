from tkinter import END, BooleanVar, Button, Entry, IntVar, Listbox, Tk, messagebox, simpledialog , ttk, Label

def print_e1():
    print(e1.get())
    lb1.insert(END, e1.get())

    messagebox.showinfo(title="soy un mensaje", message=cb1.get())

def print_lb1():
    print(lb1.curselection())
    print(lb1.size())
    print(lb1.get(lb1.curselection()[0]))
   


window = Tk()
window.geometry("450x900")
window.title("Educacion IT")

l1 = Label(window, text="HOLA MUNDO")
l1.place(x=20, y=10)

e1 = Entry(window)
e1.place(x=150, y=10)
e1.insert(0, "Valor por defecto")
#e1.delete(2,8)


b1 = Button(window, text="Imprimir", command=print_e1)
b1.place(x=85, y=80)

b2 = Button(window, text="ver seleccion", command=print_lb1)
b2.place(x=200, y=80)

lb1 = Listbox()
lb1.insert(0, "Python", "Java", "C++")
lb1.place(x=85, y=150)

cb1 = ttk.Combobox(window, values=["Hola", "Chau"], state="readonly")

cb1.place(x=85, y=350)


chk_box1_value = IntVar()
chk_box1_value.set(1)
chk_box1 = ttk.Checkbutton(text="opcion1", variable=chk_box1_value)
chk_box1.place(x=10, y=450)

chk_box2_value = BooleanVar()
chk_box2_value.set(False)
chk_box2 = ttk.Checkbutton(text="opcion2", variable=chk_box2_value)
chk_box2.place(x=10, y=490)

def print_cbx():
    print(chk_box1_value.get())
    print(chk_box2_value.get())

b3 = Button(window, text="ver seleccion", command=print_cbx)
b3.place(x=200, y=470)


# messagebox.showinfo(title="soy un mensaje", message="bla bla bla")
# messagebox.showerror(message="ERROR!")
# messagebox.showwarning(message="Warning!")

# pregu = simpledialog.askstring(prompt="Di tu nombre", title="titulo")
# print(pregu)
# ask = messagebox.askquestion( message="si o no")
# print(ask)

window.mainloop()