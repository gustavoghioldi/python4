from tkinter import *
from tkinter import ttk
from tkinter import messagebox, simpledialog
#####
def print_name():
    print(resp.get())
    lista.insert(END, resp.get())
    resp.delete(0, END)

def print_selection():
    print(lista.curselection())
    print(lista_desplegable.get())
    print(chk_box1_value.get())
    print(chk_box2_value.get())
####

window = Tk()
window.title("Hola Mundo")
window.geometry('350x800')
#texto
pregunta = Label(window, text="Cual es tu nombre?:")
pregunta.place(x=10, y=20)
#entrada
resp = Entry()
resp.place(x=150, y=20)
resp.insert(0, "HOLA")
resp.delete(2,4)
#btn
btn = Button(text="Imprimir Nombre", command=print_name)
btn.place(x=100, y=60)

#lista
lista = Listbox()
lista.insert(0, "Python", "Java", "C++", "Others")
lista.insert(2, "JS")
lista.place(x=10, y=100, height=100)

btn_lista = Button(text="Imprimir Seleccion", command=print_selection)
btn_lista.place(x=100, y=220)

#lista desplegables
lista_desplegable = ttk.Combobox(window, values=["HOLa", "Chau", "Hello", "Bye"]
    , state="readonly")
lista_desplegable.place(x=10, y=260)
#CHECKBOX
chk_box1_value = IntVar()
chk_box1_value.set(1)
chk_box1 = ttk.Checkbutton(text="opcion1", variable=chk_box1_value)
chk_box1.place(x=10, y=300)

chk_box2_value = BooleanVar()
chk_box2_value.set(False)
chk_box2 = ttk.Checkbutton(text="opcion2", variable=chk_box2_value)
chk_box2.place(x=10, y=330)

#altertas
def mensajes():
    messagebox.showinfo(title="soy un mensaje", message="bla bla bla")
    messagebox.showerror(message="ERROR!")
    messagebox.showwarning(message="Warning!")

btn_msj = Button(text="Mensajes", command=mensajes)
btn_msj.place(x=10, y=370)

def mensajes2():
    # yesorno = messagebox.askyesno(title="soy un mensaje", message="si no")
    # print(yesorno)
    # ync = messagebox.askyesnocancel(message="que quiere hacer")
    # print(ync)
    ask = messagebox.askquestion( message="si o no")
    print(ask)

btn_msj2 = Button(text="Mensajes", command=mensajes2)
btn_msj2.place(x=10, y=400)

### DEUDA de clase #####
# image = PhotoImage(file="gif.png")
# label = Label(image=image)
# label.place(x=10, y=400)


pregu = simpledialog.askstring(prompt="Di tu nombre", title="titulo")
print(pregu)
### DEUDA de clase END#####
window.mainloop()